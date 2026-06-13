"""Smoke tests for the woeai shared package layout.

These verify the package skeleton exists and is importable. They are the
tracer bullet for Stage 0 (establishing the shared package). They must stay
green across every later stage - if `import woeai...` ever breaks, every
consumer script breaks.
"""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE_PLAN = ROOT / "docs/superpowers/plans/2026-06-14-publication-and-article-architecture.md"


class PackageLayoutTests(unittest.TestCase):
    def test_root_package_imports(self) -> None:
        import woeai  # noqa: F401

    def test_publications_subpackage_imports(self) -> None:
        import woeai.publications  # noqa: F401

    def test_wechat_subpackage_imports(self) -> None:
        import woeai.wechat  # noqa: F401

    def test_architecture_plan_matches_docs_first_import_strategy(self) -> None:
        text = ARCHITECTURE_PLAN.read_text(encoding="utf-8")

        self.assertNotIn("pyproject.toml", text)
        self.assertIn("PYTHONPATH", text)

    def test_architecture_plan_matches_landed_wechat_options_module(self) -> None:
        text = ARCHITECTURE_PLAN.read_text(encoding="utf-8")

        self.assertNotIn("woeai/wechat/math.py", text)
        self.assertIn("woeai/wechat/options.py", text)


if __name__ == "__main__":
    unittest.main()
