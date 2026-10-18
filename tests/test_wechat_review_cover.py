"""Both channels use one current cover; retired selectors never fall back."""
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
        spec = importlib.util.spec_from_file_location("wechat_cover_selection_test", ROOT / "wechat/tools/wechat_draft.py")
        cls.draft = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = cls.draft
        spec.loader.exec_module(cls.draft)

    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name).resolve()
        self.review = self.root / "wechat/articles/review/ref-example.review.md"
        self.review.parent.mkdir(parents=True)
        self.cover = self.root / "wechat/assets/public-safe/ref-example/cover.png"
        self.cover.parent.mkdir(parents=True)
        self.cover.write_bytes(b"approved current image")

    def write_review(self, **fields):
        self.review.write_text("---\npublication_ref: ref-example\n" +
                               "".join(f"{key}: {value}\n" for key, value in fields.items()) +
                               "---\n- 封面素材: `old-cover.png`\n")

    def test_both_channels_and_wechat_entrypoint_use_the_same_current_source(self):
        self.write_review(cover_image="wechat/assets/public-safe/ref-example/cover.png")
        for channel in ("rtd", "wechat"):
            self.assertEqual(find_review_cover(self.review, channel=channel, root=self.root), self.cover)
        self.assertEqual(self.draft.parse_cover_path(self.review, root=self.root), self.cover)

    def test_retired_channel_fields_and_prose_are_never_fallback_sources(self):
        self.write_review(wechat_cover_image="wechat.png", rtd_cover_image="rtd.png")
        for channel in ("rtd", "wechat"):
            self.assertIsNone(find_review_cover(self.review, channel=channel, root=self.root))
        with self.assertRaisesRegex(RuntimeError, "Cannot find cover image"):
            self.draft.parse_cover_path(self.review, root=self.root)

    def test_missing_current_file_never_falls_back_to_an_old_image(self):
        self.write_review(cover_image="wechat/assets/public-safe/ref-example/cover.png")
        self.cover.unlink()
        with self.assertRaises(ValueError):
            find_review_cover(self.review, root=self.root)

    def test_current_cover_must_be_the_papers_canonical_public_path(self):
        for path in ("/tmp/private-cover.png", "../private-cover.png",
                     "wechat/assets/public-safe/ref-other/cover.png",
                     "wechat/assets/public-safe/ref-example/cover-old.png"):
            with self.subTest(path=path):
                self.write_review(cover_image=path)
                with self.assertRaises(ValueError):
                    find_review_cover(self.review, root=self.root)

    def test_symlink_redirects_are_rejected(self):
        self.cover.unlink()
        other = self.root / "other.png"
        other.write_bytes(b"other")
        self.cover.symlink_to(other)
        self.write_review(cover_image="wechat/assets/public-safe/ref-example/cover.png")
        with self.assertRaises(ValueError):
            find_review_cover(self.review, root=self.root)

if __name__ == "__main__":
    unittest.main()
