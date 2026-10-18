"""Private-only draft lookup and public metadata boundaries; fixtures, no live I/O."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

class PrivateRuntimePrivacyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.backlog = self.root / 'wechat/backlog/selected-papers.yml'
        self.backlog.parent.mkdir(parents=True)
        self.backlog.write_text('items:\n  - publication_ref: ref-example\n    title: Example\n')
        self.draft = load('privacy_draft_fixture', ROOT / 'wechat/tools/wechat_draft.py')
        for name, value in [('WECHAT_ROOT', self.root / 'wechat'), ('REPO_ROOT', self.root)]:
            patcher = mock.patch.object(self.draft, name, value)
            patcher.start(); self.addCleanup(patcher.stop)
        patcher = mock.patch.object(self.draft, 'urlopen', side_effect=AssertionError('unexpected network'))
        patcher.start(); self.addCleanup(patcher.stop)

    def test_legacy_public_file_is_not_a_runtime_fallback(self):
        path = self.root / 'wechat/data/draft-map.json'
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps([{'publication_ref': 'ref-example', 'wechat_draft_media_id': 'synthetic-old-target'}]))
        mapping = self.draft.resolve_draft_mapping(self.backlog, 'ref-example')
        self.assertEqual(mapping['media_id'], '')
        self.assertEqual(mapping['source'], 'none')

    def test_private_record_without_index_does_not_confirm_zero(self):
        self.draft.save_private_draft(self.backlog, 'ref-example', 'synthetic-target', 'fixture-time')
        self.assertIsNone(self.draft.resolve_draft_mapping(self.backlog, 'ref-example')['article_index'])

    def test_existing_target_requires_explicit_private_account_binding(self):
        ctx = SimpleNamespace(existing_media_id='synthetic-target', draft_mapping_source='private', draft_mapping_app_id='')
        with self.assertRaisesRegex(self.draft.ConfigurationError, 'draft_account_unbound'):
            self.draft.require_draft_account(ctx)

    def test_duplicate_private_json_fields_fail_instead_of_selecting_last_target(self):
        path = self.root / 'wechat/.local/registry-drafts.json'
        path.parent.mkdir(parents=True)
        path.write_text('{"ref-example":{"media_id":"synthetic-a","media_id":"synthetic-b"}}')
        with self.assertRaises(ValueError):
            self.draft.read_private_drafts(self.backlog)

    def test_remote_reader_requires_confirmed_index_before_request(self):
        for index in [None, True, -1]:
            with self.subTest(index=index), mock.patch.object(self.draft, 'api_post_json', side_effect=AssertionError('request before validation')) as request:
                with self.assertRaisesRegex(self.draft.ConfigurationError, 'draft_article_index_unverified'):
                    self.draft.fetch_remote_draft_article('synthetic-token', 'synthetic-target', index)
                request.assert_not_called()

    def test_public_repository_does_not_ship_real_draft_correspondence(self):
        self.assertFalse((ROOT / 'wechat/data/draft-map.json').exists())

    def test_public_zotero_snapshot_omits_machine_style_paths(self):
        updater = load('privacy_zotero_fixture', ROOT / 'scripts/update-publications-from-zotero.py')
        with mock.patch.object(updater, 'read_style_sha256', return_value='synthetic-style-hash'):
            style = updater.snapshot([], {}, {})['csl_style']
        self.assertFalse(any(key.endswith('_path') for key in style))
        self.assertEqual(style['id'], updater.CSL_STYLE_ID)
        self.assertEqual(style['sha256'], 'synthetic-style-hash')

    def test_style_path_can_be_selected_without_publishing_it(self):
        updater = load('privacy_zotero_cli_fixture', ROOT / 'scripts/update-publications-from-zotero.py')
        selected = Path('private-config/style.csl')
        with mock.patch.object(updater, 'CSL_SOURCE_PATH', None), mock.patch.object(updater, 'write_outputs') as write, mock.patch.object(sys, 'argv', ['updater', '--csl-style', str(selected), '--dry-run']):
            self.assertEqual(updater.main(), 0)
            self.assertEqual(updater.CSL_SOURCE_PATH, selected)
            self.assertTrue(write.call_args.args[0].dry_run)

if __name__ == '__main__':
    unittest.main()
