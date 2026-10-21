"""Owner-authorized, credential-excluded snapshots in ignored local storage."""
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import stat
import uuid
from urllib.parse import parse_qsl, urlsplit

_SECRET_KEYS = {"access_token", "refresh_token", "token", "appsecret", "app_secret",
                "secret", "authorization", "password", "credential", "api_key",
                "tempkey", "ticket"}
_SECRET_KEYS = {key.replace("_", "") for key in _SECRET_KEYS}


def _sensitive(key):
    return re.sub(r"[^a-z0-9]", "", key.lower()) in _SECRET_KEYS


_URL = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)


class PrivateTitleEvidence:
    """An immutable artifact set with a safe index; never stores endpoint URLs."""
    def __init__(self, root, publication_ref, *, forbidden=()):
        root = Path(root)
        if root.is_symlink() or root.parent.is_symlink():
            raise RuntimeError("private_evidence_symlink")
        root.mkdir(parents=True, exist_ok=True, mode=0o700)
        if stat.S_IMODE(root.stat().st_mode) & 0o077:
            raise RuntimeError("private_evidence_permissions")
        self.receipt_id = uuid.uuid4().hex
        self.directory = root / self.receipt_id
        self.directory.mkdir(mode=0o700)
        self.forbidden = tuple(value for value in forbidden if value)
        self.manifest = {"publication_ref": publication_ref, "receipt_id": self.receipt_id,
                         "created_at": datetime.now(timezone.utc).isoformat(), "artifacts": {}}
        self._manifest()

    def _clean(self, value, path="", redactions=None):
        redactions = redactions if redactions is not None else []
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                child = path + "/" + key
                if _sensitive(key):
                    result[key] = "<redacted-credential>"; redactions.append(child)
                else:
                    result[key] = self._clean(item, child, redactions)
            return result
        if isinstance(value, list):
            return [self._clean(item, path + "/" + str(i), redactions) for i, item in enumerate(value)]
        if isinstance(value, str):
            def clean_url(match):
                url = match.group()
                parsed_url = urlsplit(html.unescape(url))
                keys = {key.lower() for key, _ in parse_qsl(parsed_url.query)}
                if (parsed_url.username is not None or parsed_url.password is not None
                        or any(_sensitive(key) for key in keys)
                        or any(secret in url for secret in self.forbidden)):
                    redactions.append(path); return "<redacted-credential-url>"
                return url
            value = _URL.sub(clean_url, value)
            for secret in self.forbidden:
                if secret in value:
                    value = value.replace(secret, "<redacted-credential>"); redactions.append(path)
        return value

    def record(self, name, value, *, raw_json=False):
        if not re.fullmatch(r"[a-z0-9-]+", name):
            raise ValueError("invalid_evidence_name")
        original = value if raw_json else json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        try:
            parsed = json.loads(original)
            valid_json = True
        except ValueError:
            # Unstructured errors may contain unknown credentials. Do not retain
            # their text; record the omission explicitly instead of guessing.
            parsed = {"unparsed_response_omitted": True, "utf8_bytes": len(original.encode())}
            valid_json = False
        redactions = [] if valid_json else ["/unparsed_response"]
        clean = self._clean(parsed, redactions=redactions)
        stored = json.dumps(clean, ensure_ascii=False, indent=2) + "\n" if redactions or not valid_json else original
        if any(secret in json.dumps(clean, ensure_ascii=False) for secret in self.forbidden):
            raise RuntimeError("credential_redaction_failed")
        filename = name + ".json"
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(self.directory / filename, flags, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(stored); stream.flush(); os.fsync(stream.fileno())
        self.manifest["artifacts"][name] = {"file": filename,
            "sha256": hashlib.sha256(stored.encode()).hexdigest(),
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "credential_redactions": sorted(set(redactions)),
            "exact_transport_text": raw_json and valid_json and not redactions,
            "source_json_valid": valid_json}
        self._manifest()

    def _manifest(self):
        temporary = self.directory / ("manifest-" + uuid.uuid4().hex + ".tmp")
        fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(self.manifest, stream, ensure_ascii=False, indent=2)
            stream.write("\n"); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, self.directory / "manifest.json")

    @property
    def complete(self):
        required = {"read-2-response", "prewrite-article", "update-request",
                    "update-response", "read-3-response", "postwrite-differences"}
        return (required <= self.manifest["artifacts"].keys()
                and all(self.manifest["artifacts"][name]["source_json_valid"] for name in required))
