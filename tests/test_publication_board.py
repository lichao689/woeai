"""The browser gets a small, public-safe projection, never raw registry state."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from woeai.publications import registry


ROOT = Path(__file__).resolve().parents[1]


class PublicationBoardTests(unittest.TestCase):
    def setUp(self):
        # Explicit baseline, independent of legitimate progress in live data.
        self.row = {
            'id': 'EXAMPLE', 'type': 'article-journal', 'title': 'Example paper',
            'issued': {'date-parts': [[2026]]}, 'DOI': '10.1016/j.buildenv.2026.114811',
            'custom': {
                'publication_ref': 'ref-zhao2026-BE',
                'research_family': '建筑结构抗风', 'subdirection': '数值风洞与湍动入流',
                'source': {'status': 'unregistered'},
                'rtd': {'path': 'docs/source/paper-notes/ref-zhao2026-BE.rst',
                        'status': 'awaiting_audit', 'kind': 'legacy_intro', 'issues': [], 'evidence': {}},
                'wechat': {'path': 'wechat/articles/draft-public-safe/ref-zhao2026-BE.md',
                           'review_path': 'wechat/articles/review/ref-zhao2026-BE.review.md',
                           'selected': True, 'status': 'draft_created', 'issues': [], 'evidence': {}},
            },
        }

    def board(self, root=ROOT):
        return registry.publication_board(root, [self.row])['papers'][0]

    def test_inventory_projects_current_registry_without_false_completion(self):
        rows = registry.load_registry(ROOT); board = registry.publication_board(ROOT, rows)
        self.assertEqual(board['schema_version'], 1)
        papers = board['papers']; self.assertEqual(len(papers), 75)
        self.assertEqual(len({p['ref'] for p in papers}), 75)
        self.assertEqual(sum(p['wechat']['selected'] for p in papers), 17)
        self.assertEqual(json.loads((ROOT / registry.BOARD_PATH).read_text()), board)
        by_ref = {p['ref']: p for p in papers}
        for row in rows:
            custom = row['custom']; paper = by_ref[custom['publication_ref']]
            self.assertEqual(paper['source']['status'], custom['source']['status'])
            self.assertEqual(paper['rtd']['kind'], custom['rtd']['kind'])
            for channel in ('rtd', 'wechat'):
                workflow = custom[channel]; projected = paper[channel]
                self.assertEqual(projected['status'], workflow['status'])
                evidence = workflow.get('evidence', {})
                for check in projected['checks']:
                    expected_value = expected_stage = None
                    for stage in dict.fromkeys(['verified', workflow['status'], *registry.BOARD_STAGES]):
                        value = evidence.get(stage, {}).get('checks', {}).get(check['key'])
                        if type(value) is bool:
                            expected_value, expected_stage = value, stage; break
                    self.assertIs(check['value'], expected_value)
                    self.assertEqual(check['stage'], expected_stage)
                complete = workflow['status'] in ({'verified'} if channel == 'rtd' else {'ready_to_publish', 'published'})
                if complete:
                    self.assertTrue(registry.workflow_verified(row, channel, ROOT))
                    self.assertIs(projected['verification_current'], True)
                elif 'verified' not in evidence:
                    self.assertIsNone(projected['verification_current'])
            if custom['rtd']['kind'] == 'legacy_intro':
                self.assertIsNot(paper['rtd']['verification_current'], True)

    def engineering_blocker_fixture(self, root):
        row = copy.deepcopy(self.row)
        row['custom']['source'].update(status='verified', sha256='a' * 64)
        workflow = row['custom']['rtd']
        workflow.update(status='blocked', kind='full_paper',
                        blocker_code='source_engineering_conflict',
                        blocking_reason='PRIVATE_SENTINEL_DO_NOT_EXPOSE',
                        review_path='wechat/articles/review/ref-zhao2026-BE.review.md')
        for name in (workflow['path'], workflow['review_path'], 'project/guides/paper-deep-dive-rst.md'):
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Public source-backed content')
        evidence = {'recorded_at': '2026-10-06T07:00:00+00:00',
                    'review_path': workflow['review_path'],
                    'checks': {'source_identity': True, 'public_safety': True,
                               'full_paper_coverage': True, 'source_fidelity': True,
                               'engineering_facts': False}}
        workflow['evidence'] = {'awaiting_audit': evidence}
        evidence['fingerprint'] = registry.workflow_fingerprint(row, 'rtd', root)
        return row

    def test_current_coverage_and_engineering_conflict_are_separate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = self.engineering_blocker_fixture(root)
            track = registry.publication_board(root, [row])['papers'][0]['rtd']
            self.assertEqual(track['status'], 'blocked')
            self.assertIsNone(track['verification_current'])
            self.assertFalse(registry.workflow_verified(row, 'rtd', root))
            self.assertIn('全文覆盖已核对；原文工程结论与数值限值存在待澄清冲突', track['gaps'])
            self.assertNotIn('全文型页面仍需完整覆盖核验', track['gaps'])
            self.assertNotIn('PRIVATE_SENTINEL_DO_NOT_EXPOSE', json.dumps(track))

    def test_source_verified_concept_design_does_not_certify_engineering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = self.engineering_blocker_fixture(root)
            workflow = row['custom']['rtd']
            workflow['status'] = 'verified'
            workflow.pop('blocker_code')
            workflow.pop('blocking_reason')
            workflow['evidence']['verified'] = copy.deepcopy(workflow['evidence']['awaiting_audit'])
            self.assertIs(workflow['evidence']['verified']['checks']['engineering_facts'], False)
            self.assertTrue(registry.workflow_verified(row, 'rtd', root))
            track = registry.publication_board(root, [row])['papers'][0]['rtd']
            self.assertEqual(track['status'], 'verified')
            self.assertIs(track['verification_current'], True)
            self.assertNotIn('全文覆盖已核对；原文工程结论与数值限值存在待澄清冲突', track['gaps'])
            workflow['evidence']['verified']['checks']['full_paper_coverage'] = False
            self.assertFalse(registry.workflow_verified(row, 'rtd', root))
            workflow['evidence']['verified']['checks']['full_paper_coverage'] = True
            (root / workflow['path']).write_text('Changed after source review')
            self.assertFalse(registry.workflow_verified(row, 'rtd', root))

    def test_engineering_reason_cannot_bypass_missing_or_stale_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = self.engineering_blocker_fixture(root)
            mutations = (
                lambda w: w.update(blocker_code='missing_source_appendices'),
                lambda w: w.update(blocker_code='PRIVATE_SENTINEL_DO_NOT_EXPOSE'),
                lambda w: w['evidence']['awaiting_audit']['checks'].update(full_paper_coverage=False),
                lambda w: w['evidence']['awaiting_audit']['checks'].update(source_fidelity=False),
                lambda w: w['evidence']['awaiting_audit']['checks'].update(engineering_facts=True),
                lambda w: w['evidence']['awaiting_audit'].update(fingerprint='0' * 64),
                lambda w: w['evidence']['awaiting_audit'].update(recorded_at=''),
            )
            for mutate in mutations:
                row = copy.deepcopy(original)
                mutate(row['custom']['rtd'])
                track = registry.publication_board(root, [row])['papers'][0]['rtd']
                self.assertIn('全文型页面仍需完整覆盖核验', track['gaps'])
                self.assertNotIn('全文覆盖已核对；原文工程结论与数值限值存在待澄清冲突', track['gaps'])
                self.assertNotIn('PRIVATE_SENTINEL_DO_NOT_EXPOSE', json.dumps(track))
                self.assertFalse(registry.workflow_verified(row, 'rtd', root))
            (root / original['custom']['rtd']['path']).write_text('Changed after review')
            track = registry.publication_board(root, [original])['papers'][0]['rtd']
            self.assertIn('全文型页面仍需完整覆盖核验', track['gaps'])

    def test_projection_uses_explicit_field_allowlists(self):
        marker = 'PRIVATE_SENTINEL_DO_NOT_EXPOSE'
        self.row['custom']['extra'] = marker
        self.row['custom']['source'].update(sha256='a' * 64, private_id=marker, path=marker)
        for channel in ('rtd', 'wechat'):
            workflow = self.row['custom'][channel]
            workflow['private_id'] = marker
            workflow['legacy_backlog'] = {'media_id': marker}
            workflow['conflicts'] = [{'field': marker, 'resolution': 'unresolved'}]
            workflow['evidence'] = {'verified': {
                'fingerprint': 'b' * 64, 'private_id': marker,
                'checks': {'source_identity': True, marker: True},
            }, marker: {'checks': {'public_safety': True}}}
        paper = self.board()
        self.assertEqual(set(paper), {'ref', 'title', 'year', 'doi', 'family', 'subdirection', 'source', 'links', 'rtd', 'wechat'})
        self.assertEqual(paper['source'], {'status': 'unregistered'})
        self.assertEqual(set(paper['rtd']), {'status', 'kind', 'checks', 'gaps', 'issues', 'links', 'verification_current'})
        self.assertEqual(set(paper['wechat']), {'status', 'selected', 'checks', 'gaps', 'issues', 'links', 'verification_current'})
        encoded = json.dumps(paper)
        for forbidden in (marker, 'sha256', 'fingerprint', 'media_id', 'a' * 64, 'b' * 64):
            self.assertNotIn(forbidden, encoded)

    def test_checks_distinguish_false_unrecorded_and_evidence_stage(self):
        self.row['custom']['wechat']['evidence'] = {
            'draft_created': {'checks': {'facts': False, 'source_identity': True, 'formula_preview': 'true'}},
            'verified': {'checks': {'facts': True, 'figure_preview': False, 'cover_preview': 1}},
        }
        checks = {c['key']: c for c in self.board()['wechat']['checks']}
        self.assertEqual(checks['facts']['value'], True)
        self.assertEqual(checks['facts']['stage'], 'verified')
        self.assertEqual(checks['source_identity']['value'], True)
        self.assertEqual(checks['source_identity']['stage'], 'draft_created')
        self.assertEqual(checks['figure_preview']['value'], False)
        self.assertEqual(checks['figure_preview']['stage'], 'verified')
        for key in ('public_safety', 'formula_preview', 'cover_preview'):
            self.assertIsNone(checks[key]['value'])
        self.row['custom']['wechat']['evidence'] = {'draft_created': {'checks': {'facts': False}}}
        checks = {c['key']: c for c in self.board()['wechat']['checks']}
        self.assertIs(checks['facts']['value'], False)
        self.assertEqual(checks['facts']['stage'], 'draft_created')

    def test_links_only_use_existing_approved_public_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(self.board(root)['rtd']['links'], [])
            self.assertEqual(self.board(root)['wechat']['links'], [])
            for channel in ('rtd', 'wechat'):
                path = root / self.row['custom'][channel]['path']
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('public body')
            review = root / self.row['custom']['wechat']['review_path']
            review.parent.mkdir(parents=True, exist_ok=True)
            review.write_text('public review')
            paper = self.board(root)
            rtd_urls = {link['url'] for link in paper['rtd']['links']}
            wc_urls = {link['url'] for link in paper['wechat']['links']}
            self.assertIn('paper-notes/ref-zhao2026-BE.html', rtd_urls)
            self.assertIn('https://github.com/lichao689/woeai/blob/main/docs/source/paper-notes/ref-zhao2026-BE.rst', rtd_urls)
            self.assertIn('https://github.com/lichao689/woeai/blob/main/wechat/articles/draft-public-safe/ref-zhao2026-BE.md', wc_urls)
            self.assertIn('https://github.com/lichao689/woeai/blob/main/wechat/articles/review/ref-zhao2026-BE.review.md', wc_urls)

    def test_malicious_urls_and_private_paths_are_not_projected(self):
        malicious = (
            'javascript:alert(1)', 'https://mp.weixin.qq.com.evil.test/s/unsafe',
            'https://mp.weixin.qq.com@evil.test/s/unsafe', '//evil.test/s/unsafe',
            'https://mp.weixin.qq.com:443/s/unsafe',
            'https://mp.weixin.qq.com/s/unsafe\n',
        )
        for value in malicious:
            with self.subTest(value=value):
                self.row['URL'] = value
                self.row['DOI'] = value
                self.row['custom']['wechat']['latest_published_url'] = value
                self.row['custom']['rtd']['issues'] = [value]
                self.row['custom']['rtd']['path'] = value
                self.row['custom']['wechat']['review_path'] = value
                self.assertNotIn(value, json.dumps(self.board(), ensure_ascii=False))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            private = root / 'wechat/.local/private.md'
            private.parent.mkdir(parents=True)
            private.write_text('private')
            self.row['custom']['wechat']['path'] = 'wechat/.local/private.md'
            self.row['custom']['wechat']['review_path'] = 'wechat/.local/private.md'
            self.assertEqual(self.board(root)['wechat']['links'], [])
            public = root / 'wechat/articles/review/linked.md'
            public.parent.mkdir(parents=True)
            public.symlink_to(private)
            self.row['custom']['wechat']['review_path'] = public.relative_to(root).as_posix()
            self.assertEqual(self.board(root)['wechat']['links'], [])

    def test_only_known_url_fields_are_links_and_issue_closure_is_not_completion(self):
        self.row['custom']['rtd']['issues'] = ['https://github.com/lichao689/woeai/issues/12']
        self.row['custom']['wechat']['latest_published_url'] = 'https://mp.weixin.qq.com/s/public-slug?access_token=PRIVATE_SENTINEL'
        paper = self.board()
        self.assertEqual(paper['rtd']['issues'], ['https://github.com/lichao689/woeai/issues/12'])
        self.assertIsNone(paper['rtd']['verification_current'])
        self.assertNotIn('access_token', json.dumps(paper))
        self.assertIn('https://doi.org/10.1016/j.buildenv.2026.114811', [link['url'] for link in paper['links']])

    def test_published_permalink_keeps_only_public_locator_parameters(self):
        url = 'https://mp.weixin.qq.com/s?__biz=ABC123%3D%3D&mid=123456&idx=1&sn=' + 'a' * 32
        self.row['custom']['wechat']['latest_published_url'] = url + '&access_token=PRIVATE_SENTINEL#secret'
        urls = [link['url'] for link in self.board()['wechat']['links']]
        self.assertIn(url, urls)
        self.assertNotIn('PRIVATE_SENTINEL', json.dumps(urls))
        self.row['custom']['wechat']['latest_published_url'] = 'https://mp.weixin.qq.com/s?__biz=ABC&mid=1&idx=1'
        self.assertFalse(any(link['url'].startswith('https://mp.weixin.qq.com/') for link in self.board()['wechat']['links']))

    def test_unknown_enum_values_and_nonboolean_selection_do_not_leak_or_select(self):
        self.row['custom']['source']['status'] = 'PRIVATE_SENTINEL'
        self.row['custom']['rtd'].update(status='PRIVATE_SENTINEL', kind='PRIVATE_SENTINEL')
        self.row['custom']['wechat'].update(status='PRIVATE_SENTINEL', selected='false')
        paper = self.board()
        self.assertNotIn('PRIVATE_SENTINEL', json.dumps(paper))
        self.assertEqual(paper['source']['status'], 'unregistered')
        self.assertEqual(paper['rtd']['status'], 'unregistered')
        self.assertEqual(paper['rtd']['kind'], 'unregistered')
        self.assertIs(paper['wechat']['selected'], False)

    def test_full_paper_file_and_historical_checks_do_not_upgrade_workflow(self):
        self.row['custom']['rtd'].update(kind='full_paper', status='awaiting_audit')
        self.row['custom']['rtd']['evidence'] = {'drafting': {'checks': {
            'source_identity': True, 'full_paper_coverage': True, 'public_safety': True,
        }}}
        paper = self.board()
        self.assertEqual(paper['rtd']['status'], 'awaiting_audit')
        self.assertIsNone(paper['rtd']['verification_current'])
        self.assertEqual(paper['wechat']['status'], 'draft_created')
        self.assertIsNone(paper['wechat']['verification_current'])
        self.assertTrue(all(check['stage'] == 'drafting' for check in paper['rtd']['checks']))
        self.assertIn('全文型页面仍需完整覆盖核验', paper['rtd']['gaps'])

    def test_fact_audit_without_previews_cannot_inherit_rtd_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); custom = self.row['custom']
            custom['source'] = {'status': 'verified', 'sha256': 'a' * 64}
            review_path = custom['wechat']['review_path']
            for value in (custom['rtd']['path'], custom['wechat']['path'], review_path):
                path = root / value; path.parent.mkdir(parents=True, exist_ok=True); path.write_text('audited content')
            rtd = custom['rtd']; rtd.update(status='verified', kind='full_paper')
            rtd['evidence'] = {'verified': {'recorded_at': '2026-10-05T00:00:00Z', 'review_path': review_path,
                'checks': {key: True for key, _ in registry.BOARD_CHECKS['rtd']}}}
            rtd['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, 'rtd', root)
            wc = custom['wechat']; wc['status'] = 'awaiting_review'
            for facts in (True, False):
                wc['evidence'] = {'awaiting_review': {'checks': {'source_identity': True, 'facts': facts, 'public_safety': True}}}
                paper = self.board(root)
                self.assertIs(paper['rtd']['verification_current'], True)
                self.assertEqual(paper['wechat']['status'], 'awaiting_review')
                self.assertFalse(registry.workflow_verified(self.row, 'wechat', root))
                checks = {c['key']: c for c in paper['wechat']['checks']}
                self.assertIs(checks['facts']['value'], facts)
                for key in ('formula_preview', 'figure_preview', 'cover_preview'):
                    self.assertIsNone(checks[key]['value'])
                if facts is False: self.assertIn('事实核验：未通过', paper['wechat']['gaps'])

    def test_wechat_readiness_publication_and_rtd_are_independent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = self.row['custom']['wechat']
            for field in ('path', 'review_path'):
                path = root / workflow[field]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('public content')
            self.row['custom']['source'] = {'sha256': 'a' * 64, 'status': 'verified'}
            workflow['selected'] = False
            workflow['evidence'] = {'verified': {
                'recorded_at': '2026-10-05T00:00:00Z', 'review_path': workflow['review_path'],
                'checks': {key: True for key, _ in registry.BOARD_CHECKS['wechat']},
            }}
            workflow['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, 'wechat', root)
            for status in ('ready_to_publish', 'published'):
                workflow['status'] = status
                workflow['latest_published_url'] = 'https://mp.weixin.qq.com/s/example' if status == 'published' else ''
                paper = self.board(root)
                self.assertEqual(paper['wechat']['status'], status)
                self.assertIs(paper['wechat']['verification_current'], True)
                self.assertEqual(paper['rtd']['status'], 'awaiting_audit')
                self.assertIsNone(paper['rtd']['verification_current'])
            workflow['status'] = 'draft_created'
            self.assertEqual(self.board(root)['wechat']['status'], 'draft_created')
            self.assertIs(self.board(root)['wechat']['verification_current'], True)

    def test_downgraded_states_preserve_evidence_freshness_without_upgrading_status(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.row['custom']['source'] = {'sha256': 'a' * 64, 'status': 'verified'}
            review_path = 'wechat/articles/review/ref-example.review.md'
            review = root / review_path
            review.parent.mkdir(parents=True)
            review.write_text('coverage record')
            for channel, status in (('rtd', 'awaiting_audit'), ('wechat', 'awaiting_review')):
                with self.subTest(channel=channel):
                    workflow = self.row['custom'][channel]
                    workflow['status'] = status
                    if channel == 'rtd':
                        workflow['kind'] = 'full_paper'
                    body = root / workflow['path']
                    body.parent.mkdir(parents=True, exist_ok=True)
                    body.write_text('verified content')
                    workflow['evidence'] = {'verified': {
                        'recorded_at': '2026-10-05T00:00:00Z', 'review_path': review_path,
                        'checks': {key: True for key, _ in registry.BOARD_CHECKS[channel]},
                    }}
                    workflow['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, channel, root)
                    before = self.board(root)[channel]
                    self.assertEqual(before['status'], status)
                    self.assertIs(before['verification_current'], True)
                    self.assertFalse(registry.workflow_verified(self.row, channel, root))
                    body.write_text('edited after verification')
                    after = self.board(root)[channel]
                    self.assertEqual(after['status'], status)
                    self.assertIs(after['verification_current'], False)
                    self.assertIn('核验证据已失效或不完整，需重新核验', after['gaps'])
                    self.assertTrue(all(check['value'] is True for check in after['checks']))
                    self.assertEqual(workflow['status'], status)

    def test_downgraded_evidence_still_requires_source_identity_and_full_paper_kind(self):
        workflow = self.row['custom']['rtd']
        workflow.update(status='awaiting_audit', kind='full_paper')
        workflow['evidence'] = {'verified': {
            'recorded_at': '2026-10-05T00:00:00Z',
            'review_path': self.row['custom']['wechat']['review_path'],
            'checks': {key: True for key, _ in registry.BOARD_CHECKS['rtd']},
        }}
        workflow['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, 'rtd', ROOT)
        self.assertIs(self.board()['rtd']['verification_current'], False)
        self.row['custom']['source'] = {'status': 'verified', 'sha256': 'a' * 64}
        workflow['kind'] = 'legacy_intro'
        workflow['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, 'rtd', ROOT)
        self.assertIs(self.board()['rtd']['verification_current'], False)

    def test_stale_verification_is_not_rendered_as_completed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rtd = self.row['custom']['rtd']
            body = root / rtd['path']
            body.parent.mkdir(parents=True)
            body.write_text('body')
            review = root / 'wechat/articles/review/ref-example.review.md'
            review.parent.mkdir(parents=True)
            review.write_text('coverage record')
            self.row['custom']['source'] = {'sha256': 'a' * 64, 'status': 'verified'}
            rtd.update(status='verified', kind='full_paper')
            rtd['evidence'] = {'verified': {
                'recorded_at': '2026-10-05T00:00:00Z',
                'review_path': review.relative_to(root).as_posix(),
                'checks': {'source_identity': True, 'full_paper_coverage': True, 'public_safety': True},
            }}
            rtd['evidence']['verified']['fingerprint'] = registry.workflow_fingerprint(self.row, 'rtd', root)
            self.assertIs(self.board(root)['rtd']['verification_current'], True)
            body.write_text('changed body')
            stale = self.board(root)['rtd']
            self.assertEqual(stale['status'], 'verified')
            self.assertIs(stale['verification_current'], False)
            self.assertIn('核验证据已失效或不完整，需重新核验', stale['gaps'])
            self.assertTrue(all(check['value'] is True for check in stale['checks']))

    def test_board_is_deterministic_generated_and_stale_gate_rejects_edits(self):
        rows = registry.load_registry(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry.write_views(root, rows)
            original = (root / registry.BOARD_PATH).read_text()
            self.assertEqual(json.loads(original), registry.publication_board(root, rows))
            self.assertEqual(registry.check_views(root, rows), [])
            registry.write_views(root, rows)
            self.assertEqual((root / registry.BOARD_PATH).read_text(), original)
            (root / registry.BOARD_PATH).write_text('{}\n')
            self.assertIn(f'{registry.BOARD_PATH}: generated view out of sync', registry.check_views(root, rows))


if __name__ == '__main__':
    unittest.main()
