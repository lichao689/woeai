"""Private nonsecret account settings, separate from credential material.

Network-secret delivery is deliberately unavailable until the platform's URL
substitution and returned-token handling have been verified for this client.
"""
from __future__ import annotations

import json
import re
from pathlib import Path


class ConfigurationError(RuntimeError):
    CODES = {"invalid_account_config", "account_mismatch", "network_secret_unverified", "draft_account_unbound", "draft_article_index_unverified"}

    def __init__(self, code: str):
        self.code = code if code in self.CODES else "invalid_account_config"
        super().__init__(self.code)


def load_account(path: Path) -> dict[str, str]:
    """Read only the allowlisted account metadata; never look up env secrets."""
    if not path.exists():
        return {"credential_source": "legacy-file"}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        raise ConfigurationError("invalid_account_config") from None
    if (
        not isinstance(data, dict)
        or set(data) - {"app_id", "credential_source", "public_draft_mapping_app_id"}
        or not isinstance(data.get("app_id"), str)
        or re.fullmatch(r"wx[0-9a-f]{16}", data["app_id"]) is None
        or data.get("credential_source") not in {"legacy-file", "network-secret"}
        or ("public_draft_mapping_app_id" in data and (
            not isinstance(data["public_draft_mapping_app_id"], str)
            or re.fullmatch(r"wx[0-9a-f]{16}", data["public_draft_mapping_app_id"]) is None
        ))
    ):
        raise ConfigurationError("invalid_account_config")
    return data


def require_supported_source(account: dict[str, str]) -> None:
    if account["credential_source"] == "network-secret":
        # No heuristic placeholder recognition or fallback to raw env values.
        raise ConfigurationError("network_secret_unverified")


def effective_app_id(account: dict[str, str], values: dict[str, str]) -> str:
    configured = account.get("app_id", "")
    supplied = values.get("WECHAT_OFFICIAL_ACCOUNT_APP_ID", "")
    if configured and supplied and supplied != configured:
        raise ConfigurationError("account_mismatch")
    return configured or supplied
