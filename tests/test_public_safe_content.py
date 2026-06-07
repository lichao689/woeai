from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check-public-safe-content.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("public_safe_content", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load public-safety checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PublicSafeContentTests(unittest.TestCase):
    def run_checker(self, root: Path, wechat_root: Path) -> tuple[int, str, str]:
        checker = load_checker()
        checker.ROOT = root
        checker.SCAN_ROOTS = [wechat_root]
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = checker.main()
        return result, stdout.getvalue(), stderr.getvalue()

    def test_parent_private_directory_does_not_skip_wechat_scan(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "private" / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "draft.md").write_text(
                "appsecret = abcdefgh12345678\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("wechat/draft.md:1: possible secret pattern (appsecret)", stderr)

    def test_policy_text_without_secret_assignment_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "README.md").write_text(
                "Do not commit WeChat AppSecret, access tokens, or Zotero API keys.\n",
                encoding="utf-8",
            )

            result, stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 0)
            self.assertIn("Public-safety check passed", stdout)
            self.assertEqual(stderr, "")

    def test_failure_output_includes_line_and_pattern_label(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "draft.md").write_text(
                "title: draft\naccess_token = abcdefghijklmnop\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("Public-safety check failed:", stderr)
            self.assertIn("wechat/draft.md:2: possible secret pattern (access_token)", stderr)

    def test_scans_json_and_env_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "repo"
            wechat_root = root / "wechat"
            wechat_root.mkdir(parents=True)
            (wechat_root / "token.json").write_text(
                '{"refresh_token": "abcdefghijklmnop"}\n',
                encoding="utf-8",
            )
            (wechat_root / ".env").write_text(
                "ZOTERO_API_KEY=abcdefgh\n",
                encoding="utf-8",
            )

            result, _stdout, stderr = self.run_checker(root, wechat_root)

            self.assertEqual(result, 1)
            self.assertIn("wechat/token.json:1: possible secret pattern (refresh_token)", stderr)
            self.assertIn("wechat/.env:1: possible secret pattern (zotero_api_key)", stderr)


if __name__ == "__main__":
    unittest.main()
