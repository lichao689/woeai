"""Public registry -> optional reader navigation, entirely offline fixtures."""
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from woeai.publications.registry import validate_registry

ROOT = Path(__file__).resolve().parents[1]


class PublishedNavigationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.registry = self.root / 'docs/data/publications.json'
        self.registry.parent.mkdir(parents=True)
        spec = importlib.util.spec_from_file_location('published_navigation_fixture', ROOT / 'wechat/tools/wechat_draft.py')
        self.draft = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = self.draft
        spec.loader.exec_module(self.draft)
        for name, value in [('REPO_ROOT', self.root), ('WECHAT_ROOT', self.root / 'wechat')]:
            patcher = mock.patch.object(self.draft, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def paper(self, ref, *, published=False, sub='数值风洞', family='工程结构抗风', year=2026, url=None):
        url = url or 'https://mp.weixin.qq.com/s/' + ref
        workflow = {'selected': True, 'status': 'awaiting_review', 'issues': [], 'evidence': {},
                    'path': f'wechat/articles/draft-public-safe/{ref}.md',
                    'latest_published_url': url}
        row = {'id': ref, 'type': 'article-journal', 'title': '论文标题',
               'issued': {'date-parts': [[year]]},
               'custom': {'publication_ref': ref, 'research_family': family, 'subdirection': sub,
                          'rtd': {'status': 'unregistered', 'path': f'docs/source/paper-notes/{ref}.rst'},
                          'wechat': workflow}}
        if published:
            path = self.root / f'wechat/articles/review/{ref}.publication.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            title = '正式发表标题 ' + ref
            path.write_text(f'publication_ref: {ref}\nstatus: published\ntitle: {title}\nurl: {url}\nsource: official_publication_receipt\nsame_account: true\nverified_at: 2026-10-17\n')
            workflow['publication_record'] = {
                'status': 'published', 'url': url, 'title': title,
                'source': 'official_publication_receipt', 'same_account': True,
                'verified_at': '2026-10-17', 'evidence_path': str(path.relative_to(self.root)),
                'evidence_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        return row

    def write(self, rows):
        self.registry.write_text(json.dumps(rows, ensure_ascii=False))

    def test_unconfirmed_urls_do_not_take_the_three_slots_and_actual_published_title_is_used(self):
        target = self.paper('ref-target')
        unconfirmed = [self.paper('ref-unconfirmed' + str(i)) for i in range(3)]
        good = [self.paper('ref-published' + str(i), published=True) for i in range(4)]
        self.write([target, *unconfirmed, *good])
        links = self.draft.related_wechat_links('ref-target')
        self.assertEqual([x['publication_ref'] for x in links], ['ref-published0', 'ref-published1', 'ref-published2'])
        self.assertEqual(links[0]['title'], '正式发表标题 ref-published0')
        self.assertEqual(len(links), 3)


    def test_registry_rejects_unproved_publication_and_bad_manual_related_records(self):
        target = self.paper('ref-target')
        target['custom']['wechat']['related_articles'] = [
            {'publication_ref': 'ref-target', 'reason': 'self'},
            {'publication_ref': 'ref-missing', 'reason': ''},
        ]
        published = self.paper('ref-published', published=True)
        published['custom']['wechat']['publication_record']['same_account'] = False
        problems = validate_registry([target, published], self.root, check_evidence=False)
        self.assertTrue(any('publication record' in problem for problem in problems), problems)
        self.assertTrue(any('related_articles' in problem for problem in problems), problems)


    def test_direction_and_manual_relevance_rank_before_paper_year(self):
        target = self.paper('ref-target')
        target['custom']['wechat']['related_articles'] = [
            {'publication_ref': 'ref-old-relevant', 'reason': '同一入流方法的验证'},
            {'publication_ref': 'ref-cross-family', 'reason': '该入流方法用于平台载荷研究'},
        ]
        rows = [target, self.paper('ref-new-same', published=True),
                self.paper('ref-old-relevant', published=True, year=2010),
                self.paper('ref-other-sub', published=True, sub='结构抗风'),
                self.paper('ref-cross-family', published=True, sub='一体化分析', family='海洋能源结构')]
        self.write(rows)
        links = self.draft.related_wechat_links('ref-target')
        self.assertEqual([x['publication_ref'] for x in links], ['ref-old-relevant', 'ref-new-same', 'ref-cross-family'])

    def test_duplicate_and_current_article_urls_are_removed_before_limiting(self):
        target = self.paper('ref-target')
        own_url = target['custom']['wechat']['latest_published_url']
        rows = [target, self.paper('ref-self-alias', published=True, url=own_url),
                self.paper('ref-one', published=True),
                self.paper('ref-duplicate', published=True, url='https://mp.weixin.qq.com/s/ref-one'),
                self.paper('ref-two', published=True), self.paper('ref-three', published=True)]
        self.write(rows)
        self.assertEqual([x['publication_ref'] for x in self.draft.related_wechat_links('ref-target')], ['ref-one', 'ref-two', 'ref-three'])

    def test_missing_stale_wrong_account_and_preview_evidence_never_produce_links(self):
        target = self.paper('ref-target')
        for failure in ('missing', 'stale', 'wrong-account', 'preview', 'mismatched-url'):
            with self.subTest(failure=failure):
                row = self.paper('ref-article', published=True)
                w = row['custom']['wechat']; proof = w['publication_record']
                if failure == 'missing':
                    del w['publication_record']
                elif failure == 'stale':
                    (self.root / proof['evidence_path']).write_text('changed after review')
                elif failure == 'wrong-account':
                    proof['same_account'] = False
                elif failure == 'preview':
                    w['latest_published_url'] += '?tempkey=temporary-fixture'
                else:
                    w['latest_published_url'] = 'https://mp.weixin.qq.com/s/another'
                self.write([target, row])
                self.assertEqual(self.draft.related_wechat_links('ref-target'), [])

    def test_generated_navigation_is_clickable_text_and_ai_statement_remains_last(self):
        self.write([self.paper('ref-target'), self.paper('ref-article', published=True)])
        statement = '本文由 AI 辅助整理与撰写'
        body = self.draft.append_wechat_related_navigation('正文\n\n' + statement + '\n', self.draft.related_wechat_links('ref-target'))
        spec = importlib.util.spec_from_file_location('related_render_fixture', ROOT / 'wechat/tools/render-copy-ready.py')
        renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(renderer)
        path = self.root / 'sample.md'; path.write_text(body)
        rendered = renderer.render_markdown(path, embed_images=False, math_renderer='lightweight')
        self.assertIn('<a href="https://mp.weixin.qq.com/s/ref-article"', rendered)
        self.assertIn('正式发表标题 ref-article', rendered)
        self.assertNotIn('mp-common', rendered)
        self.assertTrue(body.rstrip().endswith(statement))


    def test_proof_fields_must_match_exactly_and_explicitly_confirm_publication_and_ownership(self):
        target = self.paper('ref-target')
        for before, after in [('publication_ref: ref-article', 'publication_ref: ref-article-other'),
                              ('url: https://mp.weixin.qq.com/s/ref-article', 'url: https://mp.weixin.qq.com/s/ref-article-other'),
                              ('status: published', 'status: draft'),
                              ('same_account: true', 'same_account: unchecked'),
                              ('source: official_publication_receipt', 'source: draft_receipt')]:
            with self.subTest(after=after):
                row = self.paper('ref-article', published=True)
                proof = row['custom']['wechat']['publication_record']
                path = self.root / proof['evidence_path']
                path.write_text(path.read_text().replace(before, after))
                proof['evidence_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
                self.write([target, row])
                self.assertEqual(self.draft.related_wechat_links('ref-target'), [])

    def test_malformed_source_is_reported_and_excluded_without_crashing(self):
        row = self.paper('ref-article', published=True)
        row['custom']['wechat']['publication_record']['source'] = []
        target = self.paper('ref-target')
        self.write([target, row])
        self.assertEqual(self.draft.related_wechat_links('ref-target'), [])
        self.assertTrue(any('publication record' in p for p in validate_registry([target, row], self.root, check_evidence=False)))


    def test_default_three_remains_configurable_and_assembly_does_not_add_a_hard_cap(self):
        self.write([self.paper('ref-target'), *[self.paper('ref-published' + str(i), published=True) for i in range(5)]])
        self.assertEqual(len(self.draft.related_wechat_links('ref-target')), 3)
        links = self.draft.related_wechat_links('ref-target', limit=5)
        self.assertEqual(len(links), 5)
        self.assertEqual(self.draft.related_wechat_links('ref-target', limit=0), [])
        statement = '本文由 AI 辅助整理与撰写'
        rendered = self.draft.append_wechat_related_navigation('正文\n\n' + statement + '\n', links)
        self.assertEqual(rendered.count('- ['), 5)
        self.assertTrue(rendered.rstrip().endswith(statement))
        self.assertEqual(self.draft.append_wechat_related_navigation(rendered, links), rendered)


if __name__ == '__main__':
    unittest.main()
