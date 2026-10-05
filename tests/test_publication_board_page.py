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
            self.assertIn('_static/' + asset, source)
            self.assertTrue((ROOT / 'docs/_static' / asset).is_file())
        self.assertIn('aria-live="polite"', source)
        self.assertIn('<noscript>', source)
        for name in ('query', 'year', 'direction', 'status', 'unfinished'):
            self.assertIn('name="' + name + '"', source)
        self.assertNotRegex(source, r'(?i)contenteditable|draggable|type="(?:password|file)"')
        scripts = re.findall(r'<script\s+src="([^"]+)"', source)
        self.assertEqual(scripts, ['_static/publication-board.js'])

    def test_generated_progress_has_stable_board_entry(self):
        self.assertIn('PublicationProgress.html', (ROOT / 'project/publication-progress.md').read_text())
        self.assertIn('PublicationProgress.html', (ROOT / 'README.rst').read_text())
