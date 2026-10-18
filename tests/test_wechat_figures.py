from __future__ import annotations

import importlib.util
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("wechat_figure_renderer", ROOT / "wechat/tools/render-copy-ready.py")
renderer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = renderer
spec.loader.exec_module(renderer)


class WeChatFigureTests(unittest.TestCase):
    def render(self, source: str, theme: str = "academic-clean") -> str:
        with tempfile.TemporaryDirectory() as directory:
            article = Path(directory) / "article.md"
            article.write_text(source, encoding="utf-8")
            return renderer.render_markdown(article, embed_images=False, theme=theme, math_renderer="lightweight")

    def test_explicit_figure_keeps_image_title_and_multiline_guide_together(self):
        output = self.render(
            "图前正文。\n\n::: figure 17\n\n"
            "![论文图 17 三个波向的比较](figure17.png)\n\n"
            "论文图 17 三个波向的比较\n\n"
            "上排为运动，\n下排为荷载。\n\n:::\n\n图后正文。\n"
        )
        self.assertIn('<section data-figure-number="17">', output)
        self.assertIn('alt="论文图 17 三个波向的比较"', output)
        self.assertIn('font-size:15px;', output)
        self.assertIn('font-size:13px;', output)
        self.assertIn('上排为运动， 下排为荷载。</p>\n</section>', output)
        self.assertNotIn('::: figure', output)
        self.assertTrue(output.endswith('>图后正文。</p>'))

    def test_historical_caption_forms_use_the_same_figure_template(self):
        for title in ["图17 波向比较", "Fig. 17 Comparison", "Figure 17 Comparison",
                      "论文图 17 波向比较（原图子图d–f）"]:
            with self.subTest(title=title):
                output = self.render(f"![{title}](image.png)\n\n{title}\n\n先看上排。\n再看下排。\n\n正文继续。")
                self.assertEqual(output.count('<section data-figure-number="17">'), 1)
                self.assertIn('font-size:15px;', output)
                self.assertIn('先看上排。 再看下排。</p>\n</section>', output)
                self.assertTrue(output.endswith('>正文继续。</p>'))

    def test_incomplete_or_conflicting_explicit_groups_report_the_source_line(self):
        image = "![论文图 17 波向比较](image.png)"
        cases = [
            (f"::: figure 17\n\n{image}\n\n说明。\n\n:::", "title"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 波向比较\n\n:::", "guide"),
            ("::: figure 17\n\n![论文图 18 比较](image.png)\n\n论文图 18 比较\n\n说明。\n\n:::", "number"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 另一图名\n\n说明。\n\n:::", "alt"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 波向比较\n\n## 正文标题\n\n:::", "guide"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 波向比较\n\n先看上排。\n## 正文标题\n\n:::", "guide"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 波向比较\n\n```python\nprint(1)\n```\n\n:::", "guide"),
            (f"::: figure 17\n\n{image}\n\n论文图 17 波向比较\n\n~~~python\nprint(1)\n~~~\n\n:::", "guide"),
            (f"::: figure 17\n\n{image}", "closing"),
            (f"::: figure\n\n{image}\n\n论文图 17 波向比较\n\n说明。\n\n:::", "number"),
        ]
        for source, diagnostic in cases:
            with self.subTest(source=source):
                with self.assertRaisesRegex(ValueError, f"line 1:.*{diagnostic}"):
                    self.render(source)

    def test_formula_images_and_body_cross_references_are_not_figure_groups(self):
        output = self.render(
            "![公式（9）](formula.svg)\n\n图17说明了周期的影响，这里仍是正文。\n\n"
            "正文第二段。\n\n$$\n::: figure 99\n$$\n"
        )
        self.assertNotIn('data-figure-number', output)
        self.assertIn('>图17说明了周期的影响，这里仍是正文。</p>', output)
        self.assertIn('>正文第二段。</p>', output)
        self.assertNotIn('font-size:15px;', output)

    def test_historical_missing_title_or_guide_is_diagnosed_without_consuming_a_heading(self):
        for source, diagnostic in [
            ("![论文图 7 校核](7.png)\n\n这是普通正文，不是图名。", "title"),
            ("![图7 校核](7.png)\n\n图7 校核\n\n## 后续正文", "guide"),
            ("![图7 校核](7.png)\n\n图7 校核\n\n```python\nprint(1)\n```", "guide"),
            ("![图7 校核](7.png)\n\n图7 校核\n\n~~~python\nprint(1)\n~~~", "guide"),
        ]:
            with self.subTest(source=source):
                with self.assertRaisesRegex(ValueError, f"line 1:.*{diagnostic}"):
                    self.render(source)

    def test_multiple_groups_and_subfigure_labels_keep_each_existing_theme(self):
        expected_colors = {
            "academic-clean": ("#1f3c56", "#586879", "#f4f8fb"),
            "engineering-note": ("#064a46", "#365d5b", "#eef8f6"),
            "recruitment-friendly": ("#5b3519", "#705d49", "#fff8eb"),
        }
        source = (
            "::: figure 17\n\n![论文图 17 校核（原图子图d–f）](17.png)\n\n"
            "论文图 17 校核（原图子图d–f）\n\n黑线为试验，红线为模拟。\n\n:::\n\n"
            "中间的普通正文。\n\n![Figure 21 Spectrum](21.png)\n\nFigure 21 Spectrum\n\n"
            "先看横轴，再看各频段。\n\n后续正文。"
        )
        for theme, (title, guide, background) in expected_colors.items():
            with self.subTest(theme=theme):
                output = self.render(source, theme)
                self.assertEqual(output.count('<section data-figure-number='), 2)
                self.assertIn('校核（原图子图d–f）', output)
                self.assertEqual(output.count('font-size:15px;line-height:1.55;text-align:center;font-style:italic;'), 2)
                self.assertEqual(output.count(f'color:{title};font-weight:500;'), 2)
                self.assertEqual(output.count('font-size:13px;line-height:1.7;text-align:center;'), 2)
                self.assertEqual(output.count(f'color:{guide};'), 2)
                self.assertEqual(output.count(f'background:{background};'), 4)
                self.assertIn('<p style="margin:0 0 16px;">中间的普通正文。</p>', output)

    def test_selected_article_check_reports_figure_errors_without_rendering_or_credentials(self):
        with tempfile.TemporaryDirectory() as directory:
            article = Path(directory) / 'article.md'
            article.write_text(
                '# 数值风洞 | 测试文章\n\n## 研究问题与解决思路\n\n研究正文。\n\n'
                '::: figure 7\n\n![图7 校核](7.png)\n\n图7 校核\n\n:::\n\n'
                '## 从论文到工程\n\n工程价值。\n\n点击阅读原文查看全文。\n\n本文由 AI 辅助整理与撰写\n',
                encoding='utf-8',
            )
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check-wechat-content.py'), str(article)],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('line 7: figure 7', result.stderr)
        self.assertIn('guide', result.stderr)

    def test_offline_draft_validation_checks_figures_before_any_live_delivery(self):
        draft_spec = importlib.util.spec_from_file_location('wechat_figure_draft', ROOT / 'wechat/tools/wechat_draft.py')
        draft = importlib.util.module_from_spec(draft_spec)
        sys.modules[draft_spec.name] = draft
        draft_spec.loader.exec_module(draft)
        with tempfile.TemporaryDirectory() as directory:
            article = Path(directory) / 'article.md'
            article.write_text('![图7 校核](7.png)\n\n图7 校核\n', encoding='utf-8')
            other = Path(directory) / 'review.md'
            other.write_text('', encoding='utf-8')
            problems = draft.validate_context(SimpleNamespace(article_path=article, review_path=other,
                                                               cover_path=other, body_images=[]))
        figure_problems = [p for p in problems if p['kind'] == 'figure_group']
        self.assertEqual(len(figure_problems), 1)
        self.assertIn('line 1: figure 7 missing guide', figure_problems[0]['message'])


if __name__ == "__main__":
    unittest.main()
