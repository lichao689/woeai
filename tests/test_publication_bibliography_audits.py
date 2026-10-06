"""Source-backed corresponding-author corrections cannot regress silently."""
import copy
import unittest
from woeai.publications.registry import validate_zotero_bibliography_audits

class PublicationBibliographyAuditTests(unittest.TestCase):
    def setUp(self):
        self.records = [self.record('V6PLJENN',['Wang Xiaolu']), self.record('3HGIR6QR',['Li Chao','Zhou Shengtao'])]

    @staticmethod
    def record(key,names):
        return {'id':key,'custom':{'bibliography_audit':{'field':'corresponding_authors','source_supported_value':names,
            'historical_value':['Li Chao'],'review_path':'wechat/articles/review/example.review.md',
            'evidence_locator':'PDF file page 1, corresponding-author footnote'}}}

    @staticmethod
    def item(key,extra):
        return {'key':key,'data':{'extra':extra,'creators':[
            {'creatorType':'author','firstName':'Chao','lastName':'Li'},
            {'creatorType':'author','firstName':'Xiaolu','lastName':'Wang'},
            {'creatorType':'author','firstName':'Shengtao','lastName':'Zhou'}]}}

    def test_known_conflicts_and_missing_markers_fail(self):
        for row in self.records:
            for extra in ('_通讯作者','corresponding authors: Chao Li','',None):
                with self.subTest(key=row['id'],extra=extra):
                    with self.assertRaisesRegex(ValueError,row['id']+'.*corresponding_authors') as caught:
                        validate_zotero_bibliography_audits(self.records,[self.item(row['id'],extra)])
                    self.assertIn('PDF file page 1',str(caught.exception))

    def test_aliases_and_order_agree_without_mutation(self):
        for one,multi in [('Wang Xiaolu','Li Chao; Zhou Shengtao'),('Xiaolu Wang','Shengtao Zhou; Chao Li'),('wANG-xIAOLU','zhou-shengtao; LI   CHAO; Li Chao')]:
            items=[self.item('V6PLJENN','通讯作者: '+one),self.item('3HGIR6QR','corresponding authors: '+multi)]
            before=copy.deepcopy((self.records,items));validate_zotero_bibliography_audits(self.records,items)
            self.assertEqual((self.records,items),before)

    def test_unrelated_records_and_other_fields_unchanged(self):
        rows=[{'id':'UNRELATED','custom':{}},self.record('OTHER',['Wang Xiaolu'])]
        rows[1]['custom']['bibliography_audit']['field']='title'
        validate_zotero_bibliography_audits(rows,[self.item('UNRELATED',None),self.item('OTHER',None)])

    def test_source_names_use_creator_aliases(self):
        self.records[0]['custom']['bibliography_audit']['source_supported_value']=['Xiaolu Wang']
        validate_zotero_bibliography_audits(self.records,[self.item('V6PLJENN','通讯作者: Wang Xiaolu')])

    def test_missing_evidence_fails_closed(self):
        for field in ('review_path','evidence_locator'):
            row=copy.deepcopy(self.records[0]);del row['custom']['bibliography_audit'][field]
            with self.assertRaisesRegex(ValueError,'review_path and evidence_locator'):
                validate_zotero_bibliography_audits([row],[self.item('V6PLJENN','通讯作者: Wang Xiaolu')])

    def test_guard_survives_completed_followup(self):
        self.records[0]['custom']['bibliography_audit']['upstream_followup_required']=False
        with self.assertRaises(ValueError):validate_zotero_bibliography_audits(self.records,[self.item('V6PLJENN','_通讯作者')])

    def test_malformed_author_evidence_fails_closed(self):
        for value in (None,[],'Wang Xiaolu',[''],[12]):
            self.records[0]['custom']['bibliography_audit']['source_supported_value']=value
            with self.assertRaisesRegex(ValueError,'source_supported_value'):
                validate_zotero_bibliography_audits(self.records,[self.item('V6PLJENN',None)])

    def test_matching_tag_cannot_hide_missing_creator(self):
        for creators in ([],[{'creatorType':'author','firstName':'Chao','lastName':'Li'}]):
            item=self.item('V6PLJENN','通讯作者: Wang Xiaolu');item['data']['creators']=creators
            with self.assertRaisesRegex(ValueError,'cannot identify audited creators'):
                validate_zotero_bibliography_audits(self.records,[item])
