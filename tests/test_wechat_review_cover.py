"""Cover selection keeps WeChat and RTD delivery independent."""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

from woeai.wechat.review import find_review_cover

ROOT = Path(__file__).resolve().parents[1]


class ReviewCoverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location(
            "wechat_cover_selection_test", ROOT / "wechat/tools/wechat_draft.py"
        )
        cls.draft = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = cls.draft
        spec.loader.exec_module(cls.draft)

    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name).resolve()
        self.review = self.directory / "example.review.md"
        self.rtd = self.directory / "rtd.png"
        self.wechat = self.directory / "wechat.png"
        self.generic = self.directory / "generic.png"
        self.legacy = self.directory / "legacy.png"

    def write_review(self, **fields):
        self.review.write_text(
            "---\n"
            + "".join(f"{key}: {value}\n" for key, value in fields.items())
            + f"---\n- 封面素材: `{self.legacy}`\n",
            encoding="utf-8",
        )

    def test_wechat_entrypoint_selects_wechat_cover_when_channels_differ(self):
        self.write_review(rtd_cover_image=self.rtd, wechat_cover_image=self.wechat)
        self.assertEqual(self.draft.parse_cover_path(self.review), self.wechat)

    def test_default_and_explicit_rtd_keep_original_cover(self):
        self.write_review(wechat_cover_image=self.wechat, rtd_cover_image=self.rtd)
        self.assertEqual(find_review_cover(self.review), self.rtd)
        self.assertEqual(find_review_cover(self.review, channel="rtd"), self.rtd)

    def test_missing_channel_field_falls_back_to_other_channel_before_generic(self):
        for channel, other, expected in (
            ("wechat", "rtd_cover_image", self.rtd),
            ("rtd", "wechat_cover_image", self.wechat),
        ):
            with self.subTest(channel=channel):
                self.write_review(**{other: expected, "cover_image": self.generic})
                self.assertEqual(find_review_cover(self.review, channel=channel), expected)
        self.write_review(rtd_cover_image=self.rtd)
        self.assertEqual(self.draft.parse_cover_path(self.review), self.rtd)

    def test_blank_channel_fields_fall_back_to_generic_before_legacy(self):
        self.write_review(rtd_cover_image="", wechat_cover_image="", cover_image=self.generic)
        for channel in ("rtd", "wechat"):
            with self.subTest(channel=channel):
                self.assertEqual(find_review_cover(self.review, channel=channel), self.generic)
        self.assertEqual(self.draft.parse_cover_path(self.review), self.generic)

    def test_legacy_cover_line_still_works_for_both_channels(self):
        self.write_review()
        for channel in ("rtd", "wechat"):
            with self.subTest(channel=channel):
                self.assertEqual(find_review_cover(self.review, channel=channel), self.legacy)
        self.assertEqual(self.draft.parse_cover_path(self.review), self.legacy)

    def test_missing_cover_keeps_optional_rtd_and_required_wechat_behavior(self):
        for content in (None, "---\n---\n"):
            with self.subTest(content=content):
                if content is not None:
                    self.review.write_text(content, encoding="utf-8")
                self.assertIsNone(find_review_cover(self.review))
                with self.assertRaisesRegex(RuntimeError, "Cannot find cover image"):
                    self.draft.parse_cover_path(self.review)


if __name__ == "__main__":
    unittest.main()
