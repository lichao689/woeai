"""Owner-approved, bounded formatting equivalence at the title-update boundary."""
import copy
import io
import unittest


class TitleEquivalenceTests(unittest.TestCase):
    def setUp(self):
        from PIL import Image
        image = Image.new('RGBA', (3, 2), (20, 40, 60, 255))
        data = io.BytesIO(); image.save(data, format='PNG'); self.image = data.getvalue()
        self.before = {'title': 'Secondary | Same hook?',
            'content': '<p>Exact text &amp; spacing.</p><img src="https://example.org/figure.png" alt="Figure"><svg><path d="M0 0L1 1"></path></svg>',
            'thumb_media_id': 'fixture-existing-cover',
            'thumb_url': 'http://mmbiz.qpic.cn/fixture-before/0?wx_fmt=png',
            'cover_info': {'crop_percent_list': [{'ratio': '1_1', 'x1': '0', 'x2': '1'}]},
            'show_cover_pic': 1, 'author': 'Original author', 'digest': 'Original digest',
            'content_source_url': 'https://example.org/paper', 'need_open_comment': 0,
            'url': 'https://mp.weixin.qq.com/s?tempkey=fixture-before'}
        self.after = {**copy.deepcopy(self.before), 'title': 'Primary | Same hook?',
            'content': self.before['content'].replace('alt="Figure">', 'alt="Figure"  />'),
            'thumb_url': 'http://mmbiz.qpic.cn/fixture-after/0?wx_fmt=png',
            'url': 'https://mp.weixin.qq.com/s?tempkey=fixture-after'}

    def test_explicit_opt_in_accepts_only_img_closure_and_verified_identical_cover(self):
        from woeai.wechat.title_update import update_title
        replies = iter([copy.deepcopy(self.before), copy.deepcopy(self.before), copy.deepcopy(self.after)])
        writes = []; fetched = []; evidence = {}
        def fetch(url): fetched.append(url); return self.image
        result = update_title(lambda: next(replies), writes.append,
            expected_title=self.before['title'], desired_title=self.after['title'],
            allow_platform_formatting=True, fetch_cover_image=fetch,
            observe=lambda name, data: evidence.update({name: copy.deepcopy(data)}))
        self.assertTrue(result['non_title_unchanged'])
        self.assertTrue(result['platform_equivalence_used'])
        self.assertEqual(writes[0]['content'], self.before['content'])
        self.assertEqual(writes[0]['cover_info'], self.before['cover_info'])
        self.assertEqual(fetched, [self.before['thumb_url'], self.after['thumb_url']])
        self.assertTrue(evidence['platform-equivalence']['body']['equivalent'])
        self.assertTrue(evidence['platform-equivalence']['cover']['bytes_equal'])
        self.assertTrue(evidence['platform-equivalence']['cover']['pixels_equal'])
        self.assertTrue(evidence['postwrite-differences']['all_protected_equal'])

    def run_change(self, after, *, enabled=True, fetch=None):
        from woeai.wechat.title_update import update_title
        replies = iter([copy.deepcopy(self.before), copy.deepcopy(self.before), copy.deepcopy(after)])
        writes = []; evidence = {}
        try:
            result = update_title(lambda: next(replies), writes.append,
                expected_title=self.before['title'], desired_title='Primary | Same hook?',
                allow_platform_formatting=enabled,
                fetch_cover_image=fetch or (lambda url: self.image),
                observe=lambda name, data: evidence.update({name: copy.deepcopy(data)}))
            return result, evidence, writes
        except RuntimeError:
            return None, evidence, writes

    def test_default_remains_strict_and_does_not_fetch_cover(self):
        result, report, writes = self.run_change(self.after, enabled=False,
            fetch=lambda url: self.fail('strict mode must not fetch covers'))
        self.assertIsNone(result)
        self.assertFalse(report['postwrite-differences']['all_protected_equal'])
        self.assertEqual(len(writes), 1)

    def test_no_other_body_cleaning_or_image_attribute_change_is_accepted(self):
        original = self.before['content']
        for content in [original.replace('Exact text', 'Different text'),
                        original + ' ', original.replace('Figure', 'Different alt'),
                        original.replace('figure.png', 'different.png'),
                        original.replace('M0 0L1 1', 'M0 0L2 2'),
                        original.replace('src=', 'class="extra" src='),
                        original.replace('<img', '<IMG'),
                        '<svg><img src="x"></svg>',
                        original.replace('alt="Figure"', 'alt="Figure" width="99"')]:
            after = {**self.after, 'content': content}
            with self.subTest(content=content):
                result, report, writes = self.run_change(after,
                    fetch=lambda url: self.fail('unexpected body must stop before CDN reads'))
                self.assertIsNone(result)
                self.assertFalse(report['postwrite-differences']['all_protected_equal'])
                self.assertEqual(len(writes), 1)

    def test_cover_material_crop_display_and_unknown_metadata_remain_strict(self):
        for changed in [{'thumb_media_id': 'different'}, {'cover_info': {'different': True}},
                        {'show_cover_pic': True}, {'author': 'Changed'},
                        {'content_source_url': 'https://example.org/different'}, {'unknown_field': 1}]:
            with self.subTest(changed=changed):
                result, report, writes = self.run_change({**self.after, **changed},
                    fetch=lambda url: self.fail('metadata differences must stop before CDN reads'))
                self.assertIsNone(result)
                self.assertFalse(report['postwrite-differences']['all_protected_equal'])
                self.assertEqual(len(writes), 1)

    def test_changed_corrupt_or_unreadable_cover_stops_without_retry(self):
        from urllib.error import HTTPError
        calls = []
        def reject(url):
            calls.append(url)
            raise HTTPError(url, 403, 'fixture denied', {}, None)
        for fetch in [lambda url: b'not-an-image',
                      lambda url: self.image if 'before' in url else self.image + b'changed', reject]:
            result, report, writes = self.run_change(self.after, fetch=fetch)
            self.assertIsNone(result)
            self.assertFalse(report['platform-equivalence']['cover']['equivalent'])
            self.assertEqual(len(writes), 1)
        self.assertEqual(calls, [self.before['thumb_url']])

    def test_unknown_or_credential_url_is_not_downloaded(self):
        from woeai.wechat.title_equivalence import cover_url_equivalence
        for url in ['https://example.org/cover', 'http://user:pass@mmbiz.qpic.cn/cover',
                    'http://mmbiz.qpic.cn/cover?access_token=fixture',
                    'http://mmbiz.qpic.cn:invalid/cover']:
            with self.subTest(url=url):
                proof = cover_url_equivalence(url, self.after['thumb_url'],
                    lambda value: self.fail('unapproved URL must not be fetched'))
                self.assertFalse(proof['equivalent'])

    def test_no_unquoted_attribute_value_can_be_changed_as_closing_syntax(self):
        from woeai.wechat.title_equivalence import image_closing_equivalence
        self.assertFalse(image_closing_equivalence('<img src=https://example.org/x>',
                                                    '<img src=https://example.org/x/>')['equivalent'])
