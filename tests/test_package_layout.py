"""Smoke tests for the woeai shared package layout.

These verify the package skeleton exists and is importable. They are the
tracer bullet for Stage 0 (establishing the shared package). They must stay
green across every later stage - if `import woeai...` ever breaks, every
consumer script breaks.
"""

from __future__ import annotations

import unittest


class PackageLayoutTests(unittest.TestCase):
    def test_root_package_imports(self) -> None:
        import woeai  # noqa: F401

    def test_publications_subpackage_imports(self) -> None:
        import woeai.publications  # noqa: F401

    def test_wechat_subpackage_imports(self) -> None:
        import woeai.wechat  # noqa: F401


if __name__ == "__main__":
    unittest.main()
