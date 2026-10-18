"""Bilingual preview contracts: shared metadata and honest language destinations."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('english_site', ROOT / 'docs/source/english_site.py')
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


class EnglishSiteTests(unittest.TestCase):
    def setUp(self):
        self.app = SimpleNamespace(confdir=ROOT / 'docs/source', env=SimpleNamespace(note_dependency=lambda path: None))

    def test_registry_projection_has_only_public_bibliography(self):
        rows = site.records(self.app)
        self.assertEqual(len(rows), 75)
        self.assertEqual(len({r['ref'] for r in rows}), 75)
        self.assertEqual(set(rows[0]), {'ref', 'title', 'authors', 'year', 'journal', 'doi', 'family', 'topic'})
        self.assertEqual({r['family'] for r in rows}, {'Structural Wind Engineering', 'Marine Energy Structures'})
        self.assertEqual(len(site.SELECTED), 6)
        self.assertTrue({r[0] for r in site.SELECTED}.issubset({r['ref'] for r in rows}))

    def test_home_cards_share_dates_and_show_full_references_without_folding(self):
        context = {}
        site.page_context(self.app, 'en/index', '', context, None)
        rendered = context['recent_progress']
        self.assertEqual(rendered.count('class="work-card"'), 6)
        self.assertEqual(rendered.count('class="paper-citation"'), 6)
        self.assertNotIn('<details', rendered)
        self.assertNotIn('Paper title & authors', rendered)
        self.assertIn('ref-zhang2025-CSICM', rendered)

    def test_group_identity_and_contact_advice_remain_distinct_from_admissions(self):
        template = (ROOT / 'docs/source/_templates/en-home.html').read_text()
        self.assertIn('id="profile-name">Research group', template)
        self.assertIn('Group leader</strong> Chao Li · Professor · PhD Supervisor', template)
        self.assertIn('{{ recent_progress|safe }}', template)
        self.assertNotIn('SELECTED RESEARCH', template)
        join = (ROOT / 'docs/source/en/JoinUs.rst').read_text()
        self.assertIn('International Master’s and PhD applicants', join)
        self.assertIn('not school admission requirements', join)
        self.assertIn('Academic contact', join)
        self.assertIn('Official application', join)
        self.assertIn('Application Portal', join)

    def test_language_switch_only_claims_existing_pairs(self):
        for page, target, label in [('Research', 'en/Research', 'EN'), ('en/JoinUs', 'Recruitment', '中文'), ('paper-notes/ref-tang2025-JBE', 'en/index', 'EN home'), ('en/highlights/ref-tang2025-JBE', 'index', '中文首页')]:
            context = {}
            site.page_context(self.app, page, '', context, None)
            self.assertEqual(context['language_target'], target)
            self.assertEqual(context['language_label'], label)

    def test_sources_gain_original_citation_and_explicit_chinese_link(self):
        text = ['Preview\n=======\n']
        site.source_read(self.app, 'en/highlights/ref-tang2025-JBE', text)
        self.assertIn('10.1016/j.jobe.2025.112131', text[0])
        self.assertIn('Chinese reading notes </paper-notes/ref-tang2025-JBE>', text[0])
        self.assertIn('Training and application of graph neural networks', text[0])
        original = ['中文原有正文']
        site.source_read(self.app, 'paper-notes/ref-tang2025-JBE', original)
        self.assertEqual(original, ['中文原有正文'])

    def test_highlights_are_short_original_accounts_without_paper_figures(self):
        for ref, heading, _ in site.SELECTED:
            source = (ROOT / f'docs/source/en/highlights/{ref}.rst').read_text()
            words = source.split('\n\n', 1)[1].split()
            self.assertTrue(150 <= len(words) <= 250, (ref, len(words)))
            self.assertIn('The problem', source)
            self.assertIn('The contribution', source)
            self.assertIn('Engineering significance', source)
            self.assertNotIn('.. image::', source)
            self.assertNotIn('.. figure::', source)


if __name__ == '__main__':
    unittest.main()
