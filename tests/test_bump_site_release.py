from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/bump-site-release.py"


class BumpSiteReleaseTests(unittest.TestCase):
    def test_updates_sphinx_release_and_version_from_fixed_beijing_time(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            conf_path = Path(tmpdir) / "conf.py"
            conf_path.write_text(
                "\n".join(
                    [
                        "project = 'Wind and Ocean Engineering with AI'",
                        "release = '0.1'",
                        "version = '0.1.0'",
                        "html_title = 'Wind and Ocean Engineering with AI'",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--conf-path",
                    str(conf_path),
                    "--datetime",
                    "2026-06-07T15:30:00+08:00",
                ],
                check=True,
                cwd=ROOT,
            )

            self.assertEqual(
                conf_path.read_text(encoding="utf-8"),
                "\n".join(
                    [
                        "project = 'Wind and Ocean Engineering with AI'",
                        "release = '2026.06.07-1530'",
                        "version = '2026.06.07'",
                        "html_title = 'Wind and Ocean Engineering with AI'",
                        "",
                    ]
                ),
            )

    def test_converts_aware_datetimes_to_beijing_time_and_leaves_rtd_config_alone(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            conf_path = root / "conf.py"
            rtd_path = root / ".readthedocs.yaml"
            conf_path.write_text("release = '0.1'\nversion = '0.1.0'\n", encoding="utf-8")
            rtd_path.write_text('version: "2"\n', encoding="utf-8")

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--conf-path",
                    str(conf_path),
                    "--datetime",
                    "2026-06-07T07:30:00+00:00",
                ],
                check=True,
                cwd=ROOT,
            )

            self.assertEqual(
                conf_path.read_text(encoding="utf-8"),
                "release = '2026.06.07-1530'\nversion = '2026.06.07'\n",
            )
            self.assertEqual(rtd_path.read_text(encoding="utf-8"), 'version: "2"\n')

    def test_does_not_rewrite_untouched_crlf_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            conf_path = Path(tmpdir) / "conf.py"
            conf_path.write_bytes(
                b"# Sphinx config\r\nrelease = '0.1'\r\nversion = '0.1.0'\r\nhtml_title = 'WOEAI'\r\n"
            )

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--conf-path",
                    str(conf_path),
                    "--datetime",
                    "2026-06-07T15:30:00+08:00",
                ],
                check=True,
                cwd=ROOT,
            )

            self.assertEqual(
                conf_path.read_bytes(),
                b"# Sphinx config\r\n"
                b"release = '2026.06.07-1530'\n"
                b"version = '2026.06.07'\n"
                b"html_title = 'WOEAI'\r\n",
            )


if __name__ == "__main__":
    unittest.main()
