"""Offline CLI contracts: fixtures only, never a real account or network."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parents[1]


class RuntimeSafetyTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("draft_runtime_safety", ROOT / "wechat/tools/wechat_draft.py")
        self.draft = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = self.draft
        spec.loader.exec_module(self.draft)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name, value in {
            "CONFIG_PATH": self.root / "credentials.env",
            "TOKEN_CACHE_PATH": self.root / "cache.json",
            "REPO_ROOT": self.root,
            "WECHAT_ROOT": self.root / "wechat",
        }.items():
            patcher = mock.patch.object(self.draft, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        patcher = mock.patch.object(self.draft, "urlopen", side_effect=AssertionError("unexpected network"))
        self.http = patcher.start()
        self.addCleanup(patcher.stop)

    def cli(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = self.draft.main(list(args))
        return code, json.loads(out.getvalue())

    def test_errors_never_echo_arbitrary_payload_or_exception_text(self):
        for error in [
            RuntimeError("secret=FAKE_ONLY access_token=FAKE_ONLY"),
            self.draft.WeChatError("fetch_access_token", {
                "errcode": 40013, "errmsg": "FAKE_ONLY", "access_token": "FAKE_ONLY",
                "extra": {"secret": "FAKE_ONLY"},
            }),
        ]:
            with self.subTest(error_type=type(error).__name__), mock.patch.object(
                self.draft, "command_dry_run", side_effect=error
            ):
                code, output = self.cli("dry-run")
                self.assertEqual(code, 1)
                self.assertNotIn("FAKE_ONLY", json.dumps(output))
                self.assertFalse(output["ok"])

    def test_cached_token_does_not_claim_current_network_verification(self):
        self.draft.TOKEN_CACHE_PATH.write_text(json.dumps({
            "access_token": "FAKE_CACHED_TOKEN", "expires_at": int(time.time()) + 3600,
            "network_verified": True,
        }))
        code, output = self.cli("token-check")
        self.assertEqual(code, 0)
        self.assertTrue(output["from_cache"])
        self.assertFalse(output["network_verified"])
        self.assertNotIn("FAKE_CACHED_TOKEN", json.dumps(output))
        self.http.assert_not_called()

    def test_refreshed_token_reports_network_verification_without_printing_token(self):
        self.draft.CONFIG_PATH.write_text("WECHAT_OFFICIAL_ACCOUNT_APP_ID=wx0000000000000000\nWECHAT_OFFICIAL_ACCOUNT_APP_SECRET=FAKE_SECRET\n")
        response = mock.MagicMock()
        response.__enter__.return_value.read.return_value = b'{"access_token":"FAKE_NEW_TOKEN","expires_in":7200}'
        self.http.side_effect = None
        self.http.return_value = response
        code, output = self.cli("token-check", "--force-refresh")
        self.assertEqual(code, 0)
        self.assertFalse(output["from_cache"])
        self.assertTrue(output["network_verified"])
        self.assertNotIn("FAKE_", json.dumps(output))
        self.http.assert_called_once()

    def test_rejected_ip_only_comes_from_strict_40164_message(self):
        valid = "invalid ip 192.0.2.1 ipv6 ::ffff:192.0.2.1, not in whitelist rid: synthetic-id"
        for code, message, expected in [
            (40164, valid, "192.0.2.1"),
            (40164, "invalid ip 2001:db8::1, not in whitelist rid: synthetic-id", "2001:db8::1"),
            (40013, valid, None), ("40164", valid, None), (True, valid, None),
            (40164, valid + " secret=FAKE_ONLY", None),
            (40164, valid.replace("192.0.2.1", "999.1.1.1"), None),
            (40164, valid.replace("::ffff:192.0.2.1", "::ffff:192.0.2.2"), None),
            (40164, "FAKE_ONLY 192.0.2.1", None),
        ]:
            with self.subTest(code=code, expected=expected), mock.patch.object(
                self.draft, "command_dry_run", side_effect=self.draft.WeChatError(
                    "fetch_access_token", {"errcode": code, "errmsg": message}
                )
            ):
                status, output = self.cli("dry-run")
                self.assertEqual(status, 1)
                self.assertEqual(output.get("wechat_rejected_ip"), expected)
                self.assertNotIn("FAKE_ONLY", json.dumps(output))

    def account(self, data):
        path = self.root / "wechat/.local/account.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data))
        return path

    def test_account_check_is_nonsecret_and_network_secret_fails_closed_even_with_cache(self):
        self.account({"app_id": "wx0000000000000000", "credential_source": "network-secret"})
        self.draft.TOKEN_CACHE_PATH.write_text(json.dumps({"access_token": "FAKE_ONLY", "expires_at": int(time.time()) + 3600}))
        code, output = self.cli("account-check")
        self.assertEqual(code, 0)
        self.assertFalse(output["will_read_credentials"])
        self.assertFalse(output["network_secret_verified"])
        code, output = self.cli("token-check")
        self.assertEqual(code, 1)
        self.assertEqual(output["configuration_error"], "network_secret_unverified")
        self.assertNotIn("FAKE_ONLY", json.dumps(output))
        self.http.assert_not_called()

    def test_account_rejects_secret_fields_without_echoing_keys_or_values(self):
        self.account({"app_id": "wx0000000000000000", "app_secret_FAKE_ONLY": "FAKE_ONLY"})
        code, output = self.cli("account-check")
        self.assertEqual(code, 1)
        self.assertNotIn("FAKE_ONLY", json.dumps(output))

    def test_config_check_does_not_echo_unrecognized_keys(self):
        self.draft.CONFIG_PATH.write_text("FAKE_ONLY_KEY=FAKE_ONLY_VALUE\n")
        code, output = self.cli("config-check")
        self.assertEqual(code, 0)
        self.assertNotIn("FAKE_ONLY", json.dumps(output))

    def test_config_check_resolves_private_account_id_and_rejects_conflicts(self):
        self.account({"app_id": "wx0000000000000000", "credential_source": "legacy-file"})
        self.draft.CONFIG_PATH.write_text("WECHAT_OFFICIAL_ACCOUNT_APP_SECRET=FAKE_ONLY\n")
        code, output = self.cli("config-check")
        self.assertEqual(code, 0)
        self.assertTrue(output["app_id_present"])
        self.draft.CONFIG_PATH.write_text("WECHAT_OFFICIAL_ACCOUNT_APP_ID=wx1111111111111111\nWECHAT_OFFICIAL_ACCOUNT_APP_SECRET=FAKE_ONLY\n")
        code, output = self.cli("config-check")
        self.assertEqual(code, 1)
        self.assertEqual(output["configuration_error"], "account_mismatch")
        self.http.assert_not_called()

    def test_http_and_url_errors_do_not_expose_urls_or_reasons(self):
        for error in [
            HTTPError("https://example.invalid/?secret=FAKE_ONLY", 403, "FAKE_ONLY", {}, None),
            URLError("https://example.invalid/?access_token=FAKE_ONLY"),
            self.draft.WeChatError("FAKE_ONLY", {"errcode": "FAKE_ONLY", "errmsg": "FAKE_ONLY"}),
            self.draft.WeChatError("draft_add", {"errcode": True}),
        ]:
            with self.subTest(error_type=type(error).__name__), mock.patch.object(self.draft, "command_dry_run", side_effect=error):
                code, output = self.cli("dry-run")
                self.assertEqual(code, 1)
                self.assertNotIn("FAKE_ONLY", json.dumps(output))
                self.assertNotIn("errcode", output)

    def test_invalid_cached_expiration_cannot_leak_through_status(self):
        self.draft.TOKEN_CACHE_PATH.write_text(json.dumps({"access_token": "FAKE_ONLY", "expires_at": "FAKE_ONLY"}))
        code, output = self.cli("token-check")
        self.assertEqual(code, 1)
        self.assertNotIn("FAKE_ONLY", json.dumps(output))
        self.http.assert_not_called()

    def test_account_switch_does_not_reuse_another_accounts_cached_token(self):
        self.account({"app_id": "wx1111111111111111", "credential_source": "legacy-file"})
        self.draft.TOKEN_CACHE_PATH.write_text(json.dumps({
            "app_id": "wx0000000000000000", "access_token": "FAKE_ONLY",
            "expires_at": int(time.time()) + 3600,
        }))
        self.draft.CONFIG_PATH.write_text("WECHAT_OFFICIAL_ACCOUNT_APP_ID=wx0000000000000000\nWECHAT_OFFICIAL_ACCOUNT_APP_SECRET=FAKE_ONLY\n")
        code, output = self.cli("token-check")
        self.assertEqual(code, 1)
        self.assertEqual(output["configuration_error"], "account_mismatch")
        self.http.assert_not_called()

    def test_private_draft_mapping_rejects_unknown_fields_before_use_or_write(self):
        path = self.root / "wechat/.local/registry-drafts.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"ref-example": {"media_id": "fake-draft", "access_token": "FAKE_ONLY"}}))
        original = path.read_bytes()
        backlog = self.root / "wechat/backlog/selected-papers.yml"
        with self.assertRaises(ValueError):
            self.draft.existing_draft_media_id(backlog, "ref-example")
        with self.assertRaises(ValueError):
            self.draft.save_private_draft(backlog, "ref-example", "other-draft", "2026-10-07")
        self.assertEqual(path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
