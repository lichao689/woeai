from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RegistryTests(unittest.TestCase):
    def setUp(self):
        # Workflow fixtures do not inherit live audit approvals.
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

    def test_inventory_preserves_records_and_current_evidence_gates(self):
        from woeai.publications.registry import load_registry, validate_registry, workflow_verified, workflow_fingerprint, BOARD_CHECKS
        rows = load_registry(ROOT)
        self.assertEqual(len(rows), 75)
        self.assertEqual(len({r['id'] for r in rows}), 75)
        self.assertEqual(sum(r['custom']['wechat']['selected'] for r in rows), 17)
        self.assertEqual(validate_registry(rows, ROOT), [])
        for row in rows:
            with self.subTest(publication=row['id']):
                custom = row['custom']
                if custom['rtd']['kind'] == 'legacy_intro':
                    self.assertNotEqual(custom['rtd']['status'], 'verified')
                    self.assertFalse(workflow_verified(row, 'rtd', ROOT))
                for channel, completed in (('rtd', {'verified'}), ('wechat', {'ready_to_publish', 'published'})):
                    workflow = custom[channel]
                    if workflow['status'] in completed:
                        self.assertTrue(workflow_verified(row, channel, ROOT))
                        evidence = workflow['evidence']['verified']
                        self.assertEqual(evidence['fingerprint'], workflow_fingerprint(row, channel, ROOT))
                        for key, _ in BOARD_CHECKS[channel]:
                            self.assertIs(evidence['checks'].get(key), True)
                checks = custom['wechat'].get('evidence', {}).get('verified', {}).get('checks', {})
                if not all(checks.get(key) is True for key in ('formula_preview', 'figure_preview', 'cover_preview')):
                    self.assertNotIn(custom['wechat']['status'], {'ready_to_publish', 'published'})
                    self.assertFalse(workflow_verified(row, 'wechat', ROOT))

    def test_verified_requires_current_source_and_channel_evidence(self):
        import copy
        import tempfile
        from woeai.publications.registry import load_registry, workflow_fingerprint, workflow_verified
        row=copy.deepcopy(self.row)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); rtd=row['custom']['rtd']; path=root/rtd['path']; path.parent.mkdir(parents=True); path.write_text('body')
            review=root/'review.md'; review.write_text('coverage record')
            row['custom']['source']={'sha256':'a'*64,'status':'verified'}
            rtd['kind']='full_paper'; rtd['status']='verified'
            self.assertFalse(workflow_verified(row,'rtd',root))
            rtd['evidence']['verified']={'recorded_at':'2026-10-05T00:00:00Z','review_path':'review.md',
                'checks':{'source_identity':True,'full_paper_coverage':True,'public_safety':True},'fingerprint':''}
            rtd['evidence']['verified']['fingerprint']=workflow_fingerprint(row,'rtd',root)
            self.assertTrue(workflow_verified(row,'rtd',root))
            row['custom']['wechat']['selected']=False
            self.assertTrue(workflow_verified(row,'rtd',root))
            path.write_text('changed body')
            self.assertFalse(workflow_verified(row,'rtd',root))

    def test_supplemental_source_identity_is_validated_and_fingerprinted(self):
        import copy
        import tempfile
        from woeai.publications.registry import workflow_fingerprint, workflow_verified, validate_registry
        row = copy.deepcopy(self.row)
        source = row['custom']['source']
        source.update(status='verified', sha256='a' * 64, supplements=[{
            'id': 'appendix-a', 'title': 'Appendix A', 'status': 'verified',
            'sha256': 'b' * 64, 'sha256_scope': 'current_audited_copy', 'pages': 3,
        }])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rtd = row['custom']['rtd']
            body = root / rtd['path']; body.parent.mkdir(parents=True); body.write_text('body')
            (root / 'review.md').write_text('Main paper and appendix reviewed')
            rtd.update(status='verified', kind='full_paper')
            evidence = {'recorded_at': '2026-10-06', 'review_path': 'review.md',
                        'checks': {'source_identity': True, 'full_paper_coverage': True, 'public_safety': True}}
            rtd['evidence']['verified'] = evidence
            evidence['fingerprint'] = workflow_fingerprint(row, 'rtd', root)
            self.assertTrue(workflow_verified(row, 'rtd', root))
            for field, replacement in [('sha256', 'c' * 64), ('pages', 4), ('title', 'Replacement appendix')]:
                changed = copy.deepcopy(row)
                changed['custom']['source']['supplements'][0][field] = replacement
                self.assertFalse(workflow_verified(changed, 'rtd', root))
            for replacement in [None, {}, [{}], [dict(source['supplements'][0], sha256='bad')],
                                [dict(source['supplements'][0], status='awaiting_audit')],
                                [dict(source['supplements'][0], pages=0)], source['supplements'] * 2]:
                changed = copy.deepcopy(row)
                changed['custom']['source']['supplements'] = replacement
                # A fresh hash cannot bless invalid or unaudited source identity.
                changed['custom']['rtd']['evidence']['verified']['fingerprint'] = workflow_fingerprint(changed, 'rtd', root)
                self.assertFalse(workflow_verified(changed, 'rtd', root))
                self.assertTrue(any('supplemental source identity' in p for p in validate_registry([changed], root)))

    def test_issue_urls_are_links_not_completion_authority(self):
        import copy
        from woeai.publications.registry import load_registry, validate_registry
        rows=copy.deepcopy(load_registry(ROOT)); rows[0]['custom']['rtd']['issues']=['https://github.com/acme/woeai/issues/12']
        self.assertEqual(validate_registry(rows,ROOT),[])
        rows[0]['custom']['rtd']['issues']=['https://github.com.evil.test/acme/woeai/issues/12']
        self.assertTrue(validate_registry(rows,ROOT))

    def test_zotero_merge_preserves_workflows_and_unfetched_records(self):
        import copy
        from woeai.publications.registry import load_registry, merge_zotero_items
        rows=load_registry(ROOT); previous=copy.deepcopy(rows)
        rows[0]['custom']['rtd']['issues']=['https://github.com/acme/woeai/issues/2']
        oldcustom=copy.deepcopy(rows[0]['custom'])
        merged=merge_zotero_items(rows,[{'key':rows[0]['id'],'data':{'title':'Updated title','publicationTitle':'Journal',
            'date':'2026-07-03','creators':[{'creatorType':'author','firstName':'Chao','lastName':'Li'}], 'volume':'12','pages':'1-9'}}])
        self.assertEqual(len(merged),75)
        self.assertEqual(merged[0]['title'],'Updated title')
        self.assertEqual(merged[0]['author'],[{'given':'Chao','family':'Li'}])
        self.assertEqual(merged[0]['issued'],{'date-parts':[[2026,7,3]]})
        self.assertEqual(merged[0]['custom'],oldcustom)
        self.assertEqual(rows[0]['title'],previous[0]['title'])

    def test_generated_views_cover_all_records_and_are_checked(self):
        import tempfile
        from woeai.publications.registry import load_registry, write_views, check_views, DASHBOARD_PATH
        rows=load_registry(ROOT)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); write_views(root,rows)
            self.assertEqual(check_views(root,rows),[])
            text=(root/DASHBOARD_PATH).read_text()
            self.assertIn('75',text)
            self.assertIn('未登记',text)
            self.assertNotIn('media_id',text)
            (root/DASHBOARD_PATH).write_text('manual conflicting authority')
            self.assertTrue(check_views(root,rows))

    def test_selection_requires_boolean_and_false_strings_never_select(self):
        import copy
        from woeai.publications.registry import load_registry, validate_registry, generated_views, BACKLOG_PATH
        rows=copy.deepcopy(load_registry(ROOT)); row=next(r for r in rows if not r['custom']['wechat']['selected'])
        row['custom']['wechat']['selected']='false'
        self.assertTrue(validate_registry(rows,ROOT))
        self.assertNotIn(row['custom']['publication_ref'],generated_views(ROOT,rows)[BACKLOG_PATH])

    def test_source_review_assets_invalidate_but_other_channel_body_does_not(self):
        import copy
        import tempfile
        from woeai.publications.registry import load_registry, workflow_fingerprint
        row=copy.deepcopy(self.row)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); rtd=row['custom']['rtd']; wc=row['custom']['wechat']
            rtd['review_path']='review.md'
            for p in (rtd['path'],wc['path'],'review.md'):
                path=root/p; path.parent.mkdir(parents=True,exist_ok=True); path.write_text('original')
            original=workflow_fingerprint(row,'rtd',root)
            (root/wc['path']).write_text('wechat-only change')
            self.assertEqual(workflow_fingerprint(row,'rtd',root),original)
            row['custom']['source']['sha256']='a'*64
            self.assertNotEqual(workflow_fingerprint(row,'rtd',root),original)
            row['custom']['source'].pop('sha256')
            (root/'review.md').write_text('changed review')
            self.assertNotEqual(workflow_fingerprint(row,'rtd',root),original)
            (root/'review.md').write_text('original')
            asset=root/'wechat/assets/public-safe'/row['custom']['publication_ref']/'figure.png'
            asset.parent.mkdir(parents=True); asset.write_bytes(b'image')
            self.assertNotEqual(workflow_fingerprint(row,'rtd',root),original)

    def test_registry_rejects_private_material_and_escaping_paths(self):
        import copy
        from woeai.publications.registry import load_registry, validate_registry
        rows=copy.deepcopy(load_registry(ROOT)); rows[0]['custom']['source']['path']='/tmp/private/source.pdf'
        self.assertTrue(validate_registry(rows,ROOT))
        rows=copy.deepcopy(load_registry(ROOT)); rows[0]['custom']['rtd']['path']='../outside.rst'
        self.assertTrue(validate_registry(rows,ROOT))

    def test_registry_is_standard_csl_json(self):
        import json
        from jsonschema import Draft7Validator
        from woeai.publications.registry import load_registry
        schema=json.loads((ROOT/'docs/data/schemas/csl-data.json').read_text())
        self.assertEqual(list(Draft7Validator(schema).iter_errors(load_registry(ROOT))),[])

    def test_referenced_shared_images_invalidate_approval(self):
        import copy
        import tempfile
        from woeai.publications.registry import load_registry, workflow_fingerprint
        row=copy.deepcopy(self.row)
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); body=root/row['custom']['rtd']['path']; body.parent.mkdir(parents=True)
            body.write_text('.. figure:: ../_static/shared.png\n')
            image=root/'docs/source/_static/shared.png'; image.parent.mkdir(); image.write_bytes(b'first image')
            before=workflow_fingerprint(row,'rtd',root)
            image.write_bytes(b'replaced image')
            self.assertNotEqual(workflow_fingerprint(row,'rtd',root),before)

    def test_real_registered_bodies_have_fingerprintable_dependencies(self):
        from woeai.publications.registry import load_registry, workflow_fingerprint
        for row in load_registry(ROOT):
            if row['custom']['wechat']['selected']:
                for channel in ('rtd','wechat'):
                    with self.subTest(publication=row['id'],channel=channel):
                        self.assertRegex(workflow_fingerprint(row,channel,ROOT),r'^[a-f0-9]{64}$')

    def test_wechat_each_backend_preview_requires_explicit_true(self):
        import tempfile
        from woeai.publications.registry import BOARD_CHECKS, workflow_fingerprint, workflow_verified
        row = self.row
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row['custom']['source'] = {'status': 'verified', 'sha256': 'a' * 64}
            workflow = row['custom']['wechat']; workflow['status'] = 'ready_to_publish'
            for key in ('path', 'review_path'):
                path = root / workflow[key]; path.parent.mkdir(parents=True, exist_ok=True); path.write_text('public content')
            checks = {key: True for key, _ in BOARD_CHECKS['wechat']}
            workflow['evidence'] = {'verified': {'recorded_at': '2026-10-05T00:00:00Z', 'review_path': workflow['review_path'], 'checks': checks}}
            workflow['evidence']['verified']['fingerprint'] = workflow_fingerprint(row, 'wechat', root)
            self.assertTrue(workflow_verified(row, 'wechat', root))
            for key in ('formula_preview', 'figure_preview', 'cover_preview'):
                for value in (None, False, 'true', 1):
                    with self.subTest(key=key, value=value):
                        if value is None: checks.pop(key)
                        else: checks[key] = value
                        self.assertFalse(workflow_verified(row, 'wechat', root)); checks[key] = True
            self.assertTrue(workflow_verified(row, 'wechat', root))
