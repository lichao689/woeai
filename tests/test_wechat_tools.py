from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]


def load_script(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load script: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class WeChatToolTests(unittest.TestCase):
    def test_lightweight_formula_renderer_does_not_call_mathjax(self) -> None:
        renderer = load_script(ROOT / "wechat/tools/render-copy-ready.py", "woeai_render_copy_ready_test")

        with mock.patch.object(renderer, "render_mathjax_svg", side_effect=AssertionError("unexpected MathJax call")):
            inline = renderer.render_inline_math(r"H_{\mathrm{max}}", math_renderer="lightweight")
            display = renderer.render_display_math(r"K_{\mathrm{CFD}}", math_renderer="lightweight")

        self.assertIn("<sub>", inline)
        self.assertIn("max", inline)
        self.assertIn("<div", display)
        self.assertIn("CFD", display)

    def test_markdown_to_rtd_preserves_blank_line_after_list(self) -> None:
        converter = load_script(ROOT / "wechat/tools/markdown_to_rtd.py", "woeai_markdown_to_rtd_test")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            article = root / "ref-example.md"
            review = root / "ref-example.review.md"
            output = root / "ref-example.rst"
            article.write_text(
                "# 示例标题\n\n"
                "## 论文信息\n\n"
                "- DOI: https://doi.org/10.1000/example\n"
                "- WOEAI 相关方向: 建筑结构抗风\n\n"
                "## 摘要\n\n"
                "**英文摘要**\n\n"
                "Plain text.\n",
                encoding="utf-8",
            )
            review.write_text("", encoding="utf-8")

            rst = converter.convert_markdown_to_rst(article, review, output)

        self.assertIn("- WOEAI 相关方向: 建筑结构抗风\n\n摘要\n--", rst)
        self.assertIn("**英文摘要**\n\nPlain text.", rst)
        self.assertNotIn("**英文摘要** ", rst)

    def test_wechat_draft_defaults_content_source_url_to_empty(self) -> None:
        draft = load_script(ROOT / "wechat/tools/wechat_draft.py", "woeai_wechat_draft_test")

        ctx = draft.build_context("ref-zhao2026-BS", "academic-clean", "lightweight")

        self.assertEqual(ctx.content_source_url, "")


if __name__ == "__main__":
    unittest.main()
