"""The existing draft API boundary must preserve everything except its title."""
import copy
import unittest


class TitleUpdateTests(unittest.TestCase):
    def article(self):
        return {'title': 'Secondary | Same question?', 'content': '<p>Latest user edit</p>',
                'author': 'Paper author', 'digest': 'Existing digest',
                'content_source_url': 'https://example.org/paper',
                'thumb_media_id': 'existing-cover', 'thumb_url': 'https://example.org/cover',
                'show_cover_pic': 1, 'article_type': 'news',
                'need_open_comment': 0, 'only_fans_can_comment': 0,
                'cover_info': {'crop': 'unchanged'}, 'url': 'private-preview-placeholder'}

    def test_title_update_preserves_latest_remote_body_cover_and_metadata(self):
        from woeai.wechat.title_update import update_title
        before = self.article()
        after = {**before, 'title': 'Primary | Same question?'}
        replies = iter([before, before, after])
        writes = []
        result = update_title(lambda: copy.deepcopy(next(replies)),
                              lambda payload: writes.append(copy.deepcopy(payload)),
                              expected_title='Secondary | Same question?',
                              desired_title='Primary | Same question?')
        self.assertEqual(result, {'updated': True, 'title_verified': True, 'non_title_unchanged': True})
        self.assertEqual(len(writes), 1)
        self.assertEqual(writes[0]['title'], 'Primary | Same question?')
        self.assertEqual(writes[0]['content'], '<p>Latest user edit</p>')
        self.assertEqual(writes[0]['thumb_media_id'], 'existing-cover')
        self.assertEqual(writes[0]['cover_info'], {'crop': 'unchanged'})
        for key in ('author', 'digest', 'content_source_url', 'show_cover_pic',
                    'article_type', 'need_open_comment', 'only_fans_can_comment'):
            self.assertEqual(writes[0][key], before[key])
        self.assertNotIn('url', writes[0])
        self.assertNotIn('thumb_url', writes[0])
        self.assertEqual(before['title'], 'Secondary | Same question?')

    def test_missing_body_or_cover_never_writes_a_partial_replacement(self):
        from woeai.wechat.title_update import update_title
        for field in ('content', 'thumb_media_id'):
            before = self.article()
            before.pop(field)
            after = {**before, 'title': 'Primary | Same question?'}
            replies = iter([before, before, after])
            writes = []
            with self.subTest(field=field), self.assertRaisesRegex(RuntimeError, 'incomplete_remote_article'):
                update_title(lambda: copy.deepcopy(next(replies)), writes.append,
                             expected_title='Secondary | Same question?', desired_title='Primary | Same question?')
            self.assertEqual(writes, [])

    def test_already_migrated_title_is_verified_without_another_write(self):
        from woeai.wechat.title_update import update_title
        before = {**self.article(), 'title': 'Primary | Same question?'}
        writes = []
        result = update_title(lambda: copy.deepcopy(before), writes.append,
                              expected_title='Secondary | Same question?', desired_title='Primary | Same question?')
        self.assertEqual(result, {'updated': False, 'title_verified': True, 'non_title_unchanged': True})
        self.assertEqual(writes, [])

    def test_unexpected_title_and_concurrent_remote_changes_never_write(self):
        from woeai.wechat.title_update import update_title
        before = self.article()
        cases = [([{**before, 'title': 'User changed this question'}], 'remote_title_conflict'),
                 ([before, {**before, 'content': '<p>Newer user edit</p>'}], 'remote_article_changed'),
                 ([before, {**before, 'cover_info': {'crop': 'user-changed'}}], 'remote_article_changed')]
        for replies, error in cases:
            with self.subTest(error=error):
                reads = iter(replies)
                writes = []
                with self.assertRaisesRegex(RuntimeError, error):
                    update_title(lambda: copy.deepcopy(next(reads)), writes.append,
                                 expected_title='Secondary | Same question?', desired_title='Primary | Same question?')
                self.assertEqual(writes, [])

    def test_failed_readback_is_marked_as_an_attempted_write_not_an_unexecuted_action(self):
        from woeai.wechat.title_update import update_title, TitleUpdateError
        before = self.article()
        after = {**before, 'title': 'Primary | Same question?', 'content': '<p>Changed</p>'}
        reads = iter([before, before, after])
        writes = []
        with self.assertRaises(TitleUpdateError) as error:
            update_title(lambda: copy.deepcopy(next(reads)), writes.append,
                         expected_title='Secondary | Same question?', desired_title='Primary | Same question?')
        self.assertEqual(error.exception.code, 'non_title_readback_changed')
        self.assertTrue(error.exception.write_attempted)
        self.assertEqual(len(writes), 1)


class TitleCommandTests(unittest.TestCase):
    def setUp(self):
        import importlib.util
        import json
        import sys
        import tempfile
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location('title_command_test', root / 'wechat/tools/wechat_draft.py')
        self.tool = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = self.tool
        spec.loader.exec_module(self.tool)
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.workspace = Path(directory.name)
        self.article = self.workspace / 'wechat/articles/draft-public-safe/ref-example.md'
        self.article.parent.mkdir(parents=True)
        self.article.write_text('# 海洋能源结构 | Same question?\n\nUnchanged body.\n')
        registry = self.workspace / 'docs/data/publications.json'
        registry.parent.mkdir(parents=True)
        registry.write_text(json.dumps([{'custom': {'publication_ref': 'ref-example',
            'research_family': '海洋能源结构', 'subdirection': '混凝土浮体',
            'wechat': {'path': 'wechat/articles/draft-public-safe/ref-example.md', 'selected': True}}}]))
        self.local = self.workspace / 'wechat/.local'
        self.local.mkdir()
        (self.local / 'account.json').write_text(json.dumps({'app_id': 'wx0000000000000000', 'credential_source': 'legacy-file'}))
        self.mapping = {'media_id': 'fake-existing-draft', 'article_index': 1, 'app_id': 'wx0000000000000000'}
        self.set_mapping(self.mapping)
        self.remote = {'title': '混凝土浮体 | Same question?', 'content': '<p>Latest backend edit</p>',
                       'thumb_media_id': 'fake-current-cover', 'thumb_url': 'https://example.org/cover',
                       'cover_info': {'crop': 'keep'}, 'author': 'Original author',
                       'digest': 'Original digest', 'url': 'private-preview-placeholder'}
        self.writes = []

    def set_mapping(self, mapping):
        import json
        data = {'ref-example': mapping} if mapping else {}
        (self.local / 'registry-drafts.json').write_text(json.dumps(data))

    def invoke(self, *extra, api=None):
        import contextlib
        import io
        import json
        from unittest.mock import patch
        output = io.StringIO()
        with patch.object(self.tool, 'WECHAT_ROOT', self.workspace / 'wechat'), \
             patch.object(self.tool, 'fetch_access_token', **({'return_value': {'access_token': 'test-only'}} if api else {'side_effect': AssertionError('no credential access')})), \
             patch.object(self.tool, 'api_post_json', side_effect=api or AssertionError('no network access')), \
             patch.object(self.tool, 'api_post_multipart', side_effect=AssertionError('no uploads')), \
             contextlib.redirect_stdout(output):
            code = self.tool.main(['update-title', '--publication-ref', 'ref-example', *extra])
        return code, json.loads(output.getvalue())

    def backend(self, response=None, changed_readback=False):
        def api(url, token, payload):
            if url == self.tool.DRAFT_GET_URL:
                return {'news_item': [{'title': 'Different article'}, copy.deepcopy(self.remote)]}
            self.assertEqual(url, self.tool.DRAFT_UPDATE_URL)
            self.assertEqual(payload['index'], 1)
            self.assertEqual(payload['media_id'], 'fake-existing-draft')
            self.writes.append(copy.deepcopy(payload['articles']))
            if response is not None:
                return response
            self.remote.update(payload['articles'])
            if changed_readback:
                self.remote['content'] = '<p>Changed after request</p>'
            return {'errcode': 0}
        return api

    def test_command_defaults_offline_without_touching_credentials_or_article(self):
        before = self.article.read_bytes()
        code, summary = self.invoke()
        self.assertEqual(code, 0)
        self.assertFalse(summary['will_contact_wechat'])
        self.assertFalse(summary['will_read_credentials'])
        self.assertEqual(summary['title'], '海洋能源结构 | Same question?')
        self.assertEqual(summary['expected_remote_title'], '混凝土浮体 | Same question?')
        self.assertNotIn('media_id', summary)
        self.assertEqual(self.article.read_bytes(), before)

    def test_live_command_preserves_the_bound_nonzero_article(self):
        original = copy.deepcopy(self.remote)
        before = self.article.read_bytes()
        code, summary = self.invoke('--live', api=self.backend())
        self.assertEqual(code, 0)
        self.assertTrue(summary['title_verified'])
        self.assertTrue(summary['non_title_unchanged'])
        self.assertEqual(len(self.writes), 1)
        self.assertEqual({k:v for k,v in self.remote.items() if k != 'title'},
                         {k:v for k,v in original.items() if k != 'title'})
        self.assertEqual(self.article.read_bytes(), before)

    def test_invalid_binding_or_index_is_not_attempted_before_credentials(self):
        for mapping, expected in [
            ({'media_id': 'fake-existing-draft', 'app_id': 'wx0000000000000000'}, 'draft_article_index_unverified'),
            ({'media_id': 'fake-existing-draft', 'article_index': 1, 'app_id': 'wx1111111111111111'}, 'account_mismatch'),
        ]:
            self.set_mapping(mapping)
            code, summary = self.invoke('--live')
            self.assertEqual(code, 1)
            self.assertEqual(summary['configuration_error'], expected)
            self.assertEqual(summary['outcome'], 'not_attempted')
            self.assertFalse(summary['write_attempted'])

    def test_missing_mapping_never_creates_a_replacement(self):
        self.set_mapping(None)
        code, summary = self.invoke('--live')
        self.assertEqual(code, 1)
        self.assertEqual(summary['outcome'], 'not_attempted')
        self.assertFalse(summary['write_attempted'])

    def test_missing_or_malformed_acknowledgment_is_uncertain_without_retry(self):
        for response in ({}, {'errcode': False}, {'errcode': 0.0}, {'errcode': None}):
            with self.subTest(response=response):
                self.writes.clear()
                code, summary = self.invoke('--live', api=self.backend(response=response))
                self.assertEqual(code, 1)
                self.assertEqual(summary['outcome'], 'uncertain')
                self.assertTrue(summary['write_attempted'])
                self.assertFalse(summary['write_acknowledged'])
                self.assertEqual(len(self.writes), 1)

    def test_explicit_nonzero_official_error_is_rejected_without_payload_leak(self):
        code, summary = self.invoke('--live', api=self.backend(response={'errcode': 48001, 'errmsg': 'UNSAFE_RAW_RESPONSE'}))
        self.assertEqual(code, 1)
        self.assertEqual(summary['outcome'], 'rejected')
        self.assertEqual(summary['errcode'], 48001)
        self.assertFalse(summary['write_acknowledged'])
        self.assertNotIn('UNSAFE_RAW_RESPONSE', str(summary))
        self.assertEqual(len(self.writes), 1)

    def test_acknowledged_write_with_changed_readback_is_verification_failed(self):
        code, summary = self.invoke('--live', api=self.backend(changed_readback=True))
        self.assertEqual(code, 1)
        self.assertEqual(summary['outcome'], 'verification_failed')
        self.assertTrue(summary['write_acknowledged'])
        self.assertEqual(summary['reason'], 'non_title_readback_changed')
        self.assertEqual(len(self.writes), 1)
