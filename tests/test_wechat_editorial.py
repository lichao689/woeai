from pathlib import Path
import hashlib
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EngineeringEndingTests(unittest.TestCase):
    def test_ending_is_one_paragraph_before_reading_reminder(self):
        from woeai.wechat.editorial import article_structure_findings
        article = ('# 示例\n\n## 研究问题与解决思路\n\n问题和方法。\n\n'
                   '## 证据说明\n\n结果。\n\n## 从论文到工程\n\n'
                   '方法支持设计方案比较。应用前需针对项目验证。\n\n'
                   '点击“阅读原文”查看全文精解。\n\n本文由 AI 辅助整理与撰写\n')
        self.assertEqual(article_structure_findings(article), [])
        bad = article.replace('方法支持设计方案比较。', '方法支持设计方案比较。\n\n')
        self.assertTrue(article_structure_findings(bad))

    def test_invalid_heading_position_sections_and_footer_are_rejected(self):
        from woeai.wechat.editorial import article_structure_findings
        article = ('# 示例\n\n## 研究问题与解决思路\n\n研究切入。\n\n'
                   '## 从论文到工程\n\n支持工程方案比较。应用前需验证。\n\n'
                   '点击阅读原文查看精解。\n\n本文由 AI 辅助整理与撰写\n')
        mutations = [
            article.replace('## 从论文到工程', '## 工程价值'),
            article.replace('## 从论文到工程', '## 从论文到工程\n\n## 从论文到工程'),
            article.replace('支持工程方案比较。', '支持工程方案比较。\n\n## 其他论证\n\n'),
            article.replace('点击阅读原文查看精解。', ''),
            article.replace('## 研究问题与解决思路', '## 从论文到工程临时'),
            article + '\n另一个尾注。',
            article.replace('点击阅读原文', '本文由 AI 辅助整理与撰写\n\n点击阅读原文'),
            article.replace('点击阅读原文', '## 提前结束\n\n点击阅读原文'),
            article.replace('支持工程方案比较。', '- 支持工程方案比较。'),
            article.replace('点击阅读原文查看精解。', '点击阅读原文查看精解。\n\n## 另一科学章节\n\n内容。'),
        ]
        for index, text in enumerate(mutations):
            with self.subTest(mutation=index):
                self.assertTrue(article_structure_findings(text))
        extended = article.replace('本文由 AI', '## 延伸阅读\n\n[已发布文章](https://mp.weixin.qq.com/s/example)\n\n本文由 AI')
        self.assertEqual(article_structure_findings(extended), [])

    def test_selected_article_cli_reports_failure_without_touching_source(self):
        import subprocess
        import sys
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'article.md'
            path.write_text('# 旧稿\n\n没有迁移的旧结构。\n')
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check-wechat-content.py'), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('从论文到工程', result.stderr)
            self.assertEqual(path.read_bytes(), before)


class RegistryTitleTests(unittest.TestCase):
    def test_title_uses_its_own_primary_family_and_rejects_secondary_prefixes(self):
        from woeai.wechat.editorial import article_title_findings
        self.assertEqual(article_title_findings('# 海洋能源结构 | 平台怎样比较？\n', '海洋能源结构'), [])
        self.assertEqual(article_title_findings('# 工程结构抗风 | 风压怎样比较？\n', '工程结构抗风'), [])
        for title in ('# 平台怎样比较？', '# 一体化分析 | 平台怎样比较？',
                      '# 混凝土浮体 | 平台怎样比较？', '# 工程结构抗风 | 平台怎样比较？',
                      '# 海洋能源结构 | ', '# 海洋能源结构 | 平台怎样比较？\n# 海洋能源结构 | 重复标题'):
            with self.subTest(title=title):
                self.assertTrue(article_title_findings(title + '\n', '海洋能源结构'))
        self.assertTrue(article_title_findings('# 一体化分析 | 平台怎样比较？\n', '一体化分析'))

    def test_every_existing_article_h1_matches_its_registry_primary_family(self):
        from woeai.publications.registry import load_registry
        from woeai.wechat.editorial import article_title_findings
        checked = 0
        for row in load_registry(ROOT):
            custom = row['custom']
            path = ROOT / custom['wechat']['path']
            if not path.is_file():
                continue
            with self.subTest(publication_ref=custom['publication_ref']):
                self.assertEqual(article_title_findings(path.read_text(), custom['research_family']), [])
            checked += 1
        self.assertGreater(checked, 0)

    def test_cli_rejects_registry_title_mismatches_without_changing_article(self):
        from contextlib import redirect_stderr, redirect_stdout
        import importlib.util
        import io
        import sys
        import tempfile
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('wechat_content_check', ROOT / 'scripts/check-wechat-content.py')
        checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checker)
        source = (ROOT / 'wechat/articles/draft-public-safe/ref-zheng2025-QHDXXB.md').read_text()
        body = source.partition('\n')[2]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            article = root / 'wechat/articles/draft-public-safe/example.md'
            article.parent.mkdir(parents=True)
            registry = root / 'docs/data/publications.json'
            registry.parent.mkdir(parents=True)
            registry.write_text(json.dumps([{'custom': {
                'publication_ref': 'example', 'research_family': '海洋能源结构', 'subdirection': '一体化分析',
                'wechat': {'path': 'wechat/articles/draft-public-safe/example.md'},
            }}]))
            cases = [('# 海洋能源结构 | 平台怎样比较？', 0),
                     ('# 工程结构抗风 | 平台怎样比较？', 1),
                     ('# 一体化分析 | 平台怎样比较？', 1),
                     ('# 平台怎样比较？', 1),
                     ('# 漂浮风电 | 平台怎样比较？', 1),
                     ('# 混凝土浮体 | 平台怎样比较？', 1)]
            for title, expected_exit in cases:
                with self.subTest(title=title):
                    article.write_text(title + '\n' + body)
                    before = article.read_bytes()
                    stderr = io.StringIO()
                    with patch.object(checker, 'ROOT', root), patch.object(sys, 'argv', ['check-wechat-content.py', str(article)]), redirect_stderr(stderr), redirect_stdout(io.StringIO()):
                        self.assertEqual(checker.main(), expected_exit)
                    if expected_exit:
                        self.assertIn('custom.research_family', stderr.getvalue())
                    self.assertEqual(article.read_bytes(), before)


class SkillPackageTests(unittest.TestCase):
    def test_canonical_rules_and_templates_have_one_entry_and_valid_links(self):
        import re
        from urllib.parse import urlsplit, unquote
        package = ROOT / '.agents/skills/wechat-paper'
        standards = package / 'references/writing-standards.md'
        self.assertTrue(standards.is_file())
        files = [package / 'SKILL.md', standards, package / 'references/natural-scientific-writing.md']
        for name in ('paper-explainer.md', 'paper-review.md', 'review-checklist.md'):
            destination = package / 'templates' / name
            files.append(destination)
            self.assertFalse((ROOT / 'wechat/templates' / name).exists())
        for path in files:
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
                url = urlsplit(target)
                if url.scheme or not url.path or '<' in target:
                    continue
                with self.subTest(file=path.name, link=target):
                    self.assertTrue((path.parent / unquote(url.path)).is_file())
        self.assertFalse((ROOT / 'wechat/STYLE.md').exists())
        for path in (ROOT / 'AGENTS.md', ROOT / 'wechat/README.md', ROOT / 'project/README.md'):
            self.assertIn('.agents/skills/wechat-paper/references/writing-standards.md', path.read_text())

    def test_legacy_archive_is_inactive_and_preserves_original_bytes(self):
        from woeai.publications.registry import WECHAT_SPECIFICATIONS
        archive = ROOT / 'project/archive/wechat-paper-legacy-bd3c34c'
        manifest = json.loads((archive / 'manifest.json').read_text())
        self.assertTrue(manifest['inactive'])
        self.assertEqual(manifest['source_commit'], 'bd3c34cae6a308ecc7cf46ec2d55f3b0972a76e3')
        self.assertEqual(len(manifest['files']), 4)
        for entry in manifest['files']:
            with self.subTest(source=entry['source_path']):
                self.assertFalse((ROOT / entry['source_path']).exists())
                self.assertTrue((ROOT / entry['canonical_path']).is_file())
                data = (ROOT / entry['archive_path']).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry['sha256'])
                self.assertEqual(len(data), entry['bytes'])
                self.assertNotIn(entry['archive_path'], WECHAT_SPECIFICATIONS)
        self.assertIn('非活跃历史归档', (archive / 'README.md').read_text())
        self.assertFalse((archive / 'SKILL.md').exists())
        for path in (ROOT / '.agents/skills/wechat-paper').rglob('*.md'):
            if 'vendor' not in path.parts:
                self.assertNotIn('project/archive/', path.read_text())

    def test_body_template_places_engineering_ending_and_exact_ai_line(self):
        package = ROOT / '.agents/skills/wechat-paper'
        text = (package / 'templates/paper-explainer.md').read_text()
        self.assertEqual(text.count('## 从论文到工程'), 1)
        self.assertLess(text.index('## 研究问题与解决思路'), text.index('## 从论文到工程'))
        self.assertLess(text.index('## 从论文到工程'), text.index('点击阅读原文'))
        self.assertEqual(text.count('本文由 AI 辅助整理与撰写'), 1)
        self.assertTrue(text.rstrip().endswith('本文由 AI 辅助整理与撰写'))
        self.assertIn('从论文到工程的价值主线', (package / 'templates/paper-review.md').read_text())

    def test_review_template_retains_parseable_metadata_at_the_start(self):
        from woeai.wechat.review import parse_front_matter
        path = ROOT / '.agents/skills/wechat-paper/templates/paper-review.md'
        metadata = parse_front_matter(path)
        self.assertEqual(metadata.get('wechat_status'), 'drafting')
        self.assertEqual(metadata.get('formula_preview_checked'), 'false')


if __name__ == '__main__':
    unittest.main()
