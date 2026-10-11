"""Content selection is an editorial decision, not authorship or completion."""
import copy
import unittest
from pathlib import Path
from woeai.publications import registry

ROOT = Path(__file__).resolve().parents[1]

class ContentProductionTests(unittest.TestCase):
    def test_inventory_has_explicit_decisions(self):
        rows = registry.load_registry(ROOT)
        values = [r['custom']['content_production'] for r in rows]
        self.assertEqual(len(values), 75)
        self.assertTrue(set(values) <= {'pending', 'included', 'excluded'})
        self.assertGreaterEqual(values.count('included'), 17)
        self.assertTrue(all(r['custom']['wechat']['selected'] == (r['custom']['content_production'] == 'included') for r in rows))

    def test_exclusion_preserves_history_but_removes_production_queue(self):
        row = copy.deepcopy(registry.load_registry(ROOT)[0])
        before = copy.deepcopy(row['custom']['rtd'])
        row['custom']['content_production'] = 'excluded'
        row['custom']['wechat']['selected'] = False
        self.assertFalse(registry.content_is_selected(row))
        self.assertEqual(row['custom']['rtd'], before)
        self.assertTrue(registry.workflow_verified(row, 'rtd', ROOT))
        board = registry.publication_board(ROOT, [row])['papers'][0]
        self.assertEqual(board['content_production'], 'excluded')
        self.assertEqual(board['rtd']['status'], 'verified')
        self.assertEqual(registry.validate_registry([row], ROOT), [])

    def test_invalid_selection_and_conflicting_legacy_mirror_are_rejected(self):
        row = copy.deepcopy(registry.load_registry(ROOT)[0])
        for value in ['rtd_only', 'wechat_only', True, {}, None]:
            row['custom']['content_production'] = value
            self.assertTrue(any('content_production' in p for p in registry.validate_registry([row], ROOT, check_evidence=False)))
        row['custom']['content_production'] = 'pending'
        self.assertTrue(any('selected' in p for p in registry.validate_registry([row], ROOT, check_evidence=False)))

    def test_zotero_refresh_does_not_change_editorial_choice(self):
        row = copy.deepcopy(registry.load_registry(ROOT)[0])
        row['custom']['content_production'] = 'excluded'
        result = registry.merge_zotero_items([row], [{'key': row['id'], 'data': {'title': 'Updated bibliography', 'creators': [{'creatorType': 'author', 'firstName': 'Chao', 'lastName': 'Li'}]}}])
        self.assertEqual(result[0]['custom']['content_production'], 'excluded')
