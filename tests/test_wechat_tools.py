from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
PNG_1X1 = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108020000009077"
    "53de0000000c4944415408d763f8ffff3f0005fe02fea73581e10000000049"
    "454e44ae426082"
)


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
        self.assertIn(".. role:: student-first-author", rst)
        self.assertIn("**英文摘要**\n\nPlain text.", rst)
        self.assertNotIn("**英文摘要** ", rst)

    def test_markdown_to_rtd_converts_author_markers_like_publications(self) -> None:
        converter = load_script(ROOT / "wechat/tools/markdown_to_rtd.py", "woeai_markdown_to_rtd_author_test")

        rst = converter.convert_inline("- 作者: <u>Zhao Peisheng</u>; **Li Chao**\\*; Wang Xiaolu")

        self.assertEqual(rst, "- 作者: :student-first-author:`Zhao Peisheng`; **Li Chao**\\*; Wang Xiaolu")

    def test_wechat_renderer_shows_corresponding_star_and_underlined_author(self) -> None:
        renderer = load_script(ROOT / "wechat/tools/render-copy-ready.py", "woeai_render_copy_ready_author_test")

        rendered = renderer.render_inline("<u>Zhao Peisheng</u>; **Li Chao**\\*", math_renderer="lightweight")

        self.assertIn("text-decoration:underline", rendered)
        self.assertIn("Zhao Peisheng", rendered)
        self.assertIn("<strong>Li Chao</strong>*", rendered)
        self.assertNotIn("\\*", rendered)

    def test_wechat_draft_defaults_content_source_url_to_empty(self) -> None:
        draft = load_script(ROOT / "wechat/tools/wechat_draft.py", "woeai_wechat_draft_test")

        ctx = draft.build_context("ref-zhao2026-BS", "academic-clean", "lightweight")

        self.assertEqual(ctx.content_source_url, "")

    def test_wechat_draft_uses_first_paper_author_when_review_author_is_legacy_woeai(self) -> None:
        draft = load_script(ROOT / "wechat/tools/wechat_draft.py", "woeai_wechat_draft_author_test")

        with mock.patch.object(
            draft,
            "parse_front_matter",
            return_value={"body_images_upload_approved": "true", "wechat_author": "WOEAI"},
        ):
            ctx = draft.build_context("ref-zhao2026-BS", "academic-clean", "lightweight")

        self.assertEqual(ctx.author, "Zhao Peisheng")

    def test_cover_preview_renders_candidate_labels_and_small_thumbnail(self) -> None:
        preview = load_script(
            ROOT / ".agents/skills/wechat-cover/scripts/cover_preview.py",
            "woeai_cover_preview_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            cover = root / "candidate.png"
            output = root / "preview.html"
            cover.write_bytes(PNG_1X1)

            with contextlib.redirect_stdout(io.StringIO()):
                result = preview.main([str(cover), "--label", "候选 A", "--output", str(output)])
            payload = json.loads(preview.LAST_JSON_OUTPUT)
            html = output.read_text(encoding="utf-8")

        self.assertEqual(result, 0)
        self.assertEqual(payload["covers"][0]["label"], "候选 A")
        self.assertIn("候选 A", html)
        self.assertIn("Small Thumbnail", html)

    def test_cover_text_overlay_reports_missing_pillow_as_json_error(self) -> None:
        overlay = load_script(
            ROOT / ".agents/skills/wechat-cover/scripts/cover_text_overlay.py",
            "woeai_cover_text_overlay_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base = root / "base.png"
            output = root / "cover.png"
            base.write_bytes(PNG_1X1)

            with contextlib.redirect_stdout(io.StringIO()):
                result = overlay.main(
                    [
                        str(base),
                        str(output),
                        "--category",
                        "数值风洞",
                        "--hook",
                        "让城市风场更快可算",
                    ]
                )
            payload = json.loads(overlay.LAST_JSON_OUTPUT)

        self.assertEqual(result, 1)
        self.assertEqual(payload["stage"], "dependency_check")
        self.assertIn("Pillow", payload["message"])

    def test_cover_preview_records_candidate_scores(self) -> None:
        preview = load_script(
            ROOT / ".agents/skills/wechat-cover/scripts/cover_preview.py",
            "woeai_cover_preview_scores_test",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            cover = root / "candidate.png"
            output = root / "preview.html"
            cover.write_bytes(PNG_1X1)

            with contextlib.redirect_stdout(io.StringIO()):
                result = preview.main(
                    [
                        str(cover),
                        "--label",
                        "候选 A",
                        "--score",
                        "article_specificity=4,click_appeal=5",
                        "--output",
                        str(output),
                    ]
                )
            payload = json.loads(preview.LAST_JSON_OUTPUT)
            html = output.read_text(encoding="utf-8")

        self.assertEqual(result, 0)
        self.assertEqual(payload["covers"][0]["scores"]["article_specificity"], "4")
        self.assertEqual(payload["covers"][0]["scores"]["click_appeal"], "5")
        self.assertIn("article_specificity", html)


if __name__ == "__main__":
    unittest.main()
