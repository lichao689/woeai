"""Integration boundaries for the standalone read-only Sphinx page."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicationBoardPageTests(unittest.TestCase):
    def test_page_is_orphan_and_absent_from_academic_navigation(self):
        page = ROOT / 'docs/source/PublicationProgress.rst'
        self.assertTrue(page.read_text().startswith(':orphan:'))
        for source in (ROOT / 'docs/source').rglob('*.rst'):
            if source != page:
                self.assertNotIn('PublicationProgress', source.read_text(), source.as_posix())

    def test_page_has_local_assets_and_accessible_readonly_controls(self):
        source = (ROOT / 'docs/source/PublicationProgress.rst').read_text()
        for asset in ('publication-board.css', 'publication-board.js', 'publication-board-data.json'):
            if asset.endswith('.json'):
                self.assertIn('_static/' + asset, source)
            self.assertTrue((ROOT / 'docs/_static' / asset).is_file())
        self.assertIn('aria-live="polite"', source)
        self.assertIn('<noscript>', source)
        self.assertIn('role="region" aria-label="论文进度表，可横向滚动" tabindex="0"', source)
        self.assertIn('按 RTD 筛选', source)
        self.assertIn('按公众号筛选', source)
        for name in ('query', 'year', 'direction', 'status', 'unfinished'):
            self.assertIn('name="' + name + '"', source)
        self.assertNotRegex(source, r'(?i)contenteditable|draggable|type="(?:password|file)"')
        scripts = re.findall(r'<script\s+src="([^"]+)"', source)
        self.assertEqual(scripts, [])

    def test_compact_header_keeps_explanations_in_native_disclosure(self):
        source = (ROOT / 'docs/source/PublicationProgress.rst').read_text()
        self.assertIn('<details class="board-help">', source)
        self.assertIn('<summary>状态与筛选说明</summary>', source)
        help_body = source.split('<details class="board-help">', 1)[1].split('</details>', 1)[0]
        for meaning in ('独立记录', '未登记不等于未开始', '草稿不等于发布', '按所选渠道计算'):
            self.assertIn(meaning, help_body)
        self.assertNotIn('<details class="board-help" open', source)
        self.assertIn('class="board-toolbar"', source)

    def test_generated_progress_has_stable_board_entry(self):
        self.assertIn('PublicationProgress.html', (ROOT / 'project/publication-progress.md').read_text())
        self.assertIn('PublicationProgress.html', (ROOT / 'README.rst').read_text())

    def test_build_versions_assets_only_on_board_page(self):
        import hashlib
        import runpy
        from types import SimpleNamespace
        from unittest.mock import Mock
        config = runpy.run_path(str(ROOT / 'docs/source/conf.py'))
        app = SimpleNamespace(confdir=ROOT / 'docs/source', add_css_file=Mock(), add_js_file=Mock())
        hook = config['_add_publication_board_assets']
        context = {'body': '<div data-source="_static/publication-board-data.json"></div>'}
        hook(app, 'index', 'page.html', context, None)
        app.add_css_file.assert_not_called()
        app.add_js_file.assert_not_called()
        self.assertNotIn('?v=', context['body'])
        hook(app, 'PublicationProgress', 'page.html', context, None)
        app.add_css_file.assert_called_once_with('publication-board.css')
        app.add_js_file.assert_called_once_with('publication-board.js', loading_method='defer')
        digest = hashlib.sha256((ROOT / 'docs/_static/publication-board-data.json').read_bytes()).hexdigest()[:16]
        self.assertIn('publication-board-data.json?v=' + digest, context['body'])

    def test_data_cache_version_changes_with_generated_bytes(self):
        import runpy
        import tempfile
        from types import SimpleNamespace
        from unittest.mock import Mock
        hook = runpy.run_path(str(ROOT / 'docs/source/conf.py'))['_add_publication_board_assets']
        with tempfile.TemporaryDirectory() as folder:
            docs = Path(folder)
            (docs / '_static').mkdir()
            data = docs / '_static/publication-board-data.json'
            app = SimpleNamespace(confdir=docs / 'source', add_css_file=Mock(), add_js_file=Mock())
            def render(payload):
                data.write_text(payload)
                context = {'body': '<div data-source="_static/publication-board-data.json"></div>'}
                hook(app, 'PublicationProgress', 'page.html', context, None)
                return context['body']
            original = render('{"papers": []}')
            self.assertEqual(original, render('{"papers": []}'))
            self.assertNotEqual(original, render('{"papers": [{"status": "drafting"}]}'))
            with self.assertRaisesRegex(ValueError, 'exactly one'):
                hook(app, 'PublicationProgress', 'page.html', {'body': ''}, None)
