"""Latest homepage papers are selected by publication date in both languages."""
from html import escape
from pathlib import Path
import unittest
import json
import tempfile
import hashlib

from woeai.wechat.review import parse_front_matter

from woeai.publications.homepage import recent_publications, render_home_progress, publication_date, copy_home_progress_covers
from woeai.publications.registry import load_registry, workflow_fingerprint

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "工程结构抗风": ["ref-zhao2026-BE", "ref-he2026-OE", "ref-zhao2026-BS"],
    "海洋能源结构": ["ref-he2026-OE-structural", "ref-zheng2025-OE", "ref-zheng2025-QHDXXB"],
}

class HomepageProgressTests(unittest.TestCase):
    def test_latest_three_per_family_only_include_produced_reviewed_introductions(self):
        groups = recent_publications(load_registry(ROOT), ROOT)
        self.assertEqual({family: [r["custom"]["publication_ref"] for r in rows] for family, rows in groups}, EXPECTED)

    def test_homepage_covers_are_generated_from_the_single_current_source(self):
        with tempfile.TemporaryDirectory() as directory:
            outdir = Path(directory)
            target = outdir / "_static/home"
            target.mkdir(parents=True)
            (target / "progress-retired.png").write_bytes(b"stale generated output")
            (target / "other-image.png").write_bytes(b"unrelated output")
            copy_home_progress_covers(ROOT, outdir)
            self.assertFalse((target / "progress-retired.png").exists())
            self.assertEqual((target / "other-image.png").read_bytes(), b"unrelated output")
            for _, rows in recent_publications(load_registry(ROOT), ROOT):
                for row in rows:
                    ref = row["custom"]["publication_ref"]
                    with self.subTest(publication_ref=ref):
                        review = ROOT / row["custom"]["wechat"]["review_path"]
                        cover = parse_front_matter(review)["cover_image"]
                        self.assertEqual(cover, f"wechat/assets/public-safe/{ref}/cover.png")
                        homepage = target / f"progress-{ref}.png"
                        self.assertEqual(hashlib.sha256(homepage.read_bytes()).hexdigest(),
                                         hashlib.sha256((ROOT / cover).read_bytes()).hexdigest())
                        self.assertFalse((ROOT / "docs/_static/home" / homepage.name).exists())
        for english in (False, True):
            rendered = render_home_progress(ROOT, english=english)
            self.assertEqual(rendered.count('<figure>'), 6)
            self.assertEqual(rendered.count('.png?v='), 6)

    def test_each_produced_paper_has_only_one_current_cover_source(self):
        rows = [r for r in load_registry(ROOT)
                if any((ROOT / "wechat/assets/public-safe" / r["custom"]["publication_ref"]).glob("cover*.png"))]
        for row in rows:
            ref = row["custom"]["publication_ref"]
            folder = ROOT / "wechat/assets/public-safe" / ref
            with self.subTest(publication_ref=ref):
                images = sorted(p.name for p in folder.glob("cover*")
                                if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"})
                self.assertEqual(images, ["cover.png"])
                front = parse_front_matter(ROOT / row["custom"]["wechat"]["review_path"])
                self.assertNotIn("wechat_cover_image", front)
                self.assertNotIn("rtd_cover_image", front)
                self.assertEqual(front["cover_image"], f"wechat/assets/public-safe/{ref}/cover.png")

    def test_cover_migration_did_not_approve_previously_stale_content(self):
        stale = {"ref-chen2024-POF", "ref-li2024-POF", "ref-chen2024-JCP", "ref-yang2022-AS"}
        for row in load_registry(ROOT):
            if row["custom"]["publication_ref"] in stale:
                checks = row["custom"]["wechat"]["evidence"]["cover_single_source_equivalence_20261018"]["checks"]
                self.assertFalse(checks["facts"])
                self.assertFalse(checks["public_safety"])
                self.assertFalse(checks["figure_preview"])

    def test_date_precision_and_stable_ties_do_not_follow_manual_highlight_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            candidates = []
            for ref, issued, date, order in [
                ("year-only", [2025], "2025", 0),
                ("early", [2025], "2025/2/1", 1),
                ("late", [2025], "2025-12-02", 20),
                ("same-date", [2025], "2025/12/2", 21),
                ("explicit", [2025, 12, 3], "2025/1", 99),
            ]:
                candidates.append(self.candidate(root, ref, issued, date, order))
            groups = recent_publications(list(reversed(candidates)), root)
            self.assertEqual([r["custom"]["publication_ref"] for r in groups[0][1]],
                             ["explicit", "late", "same-date"])
            self.assertEqual(publication_date(candidates[0]), (2025, 0, 0))

    def candidate(self, root, ref, issued=None, date="2025", order=0, selected=True):
        """A produced public article reviewed without uploading or phone preview."""
        article = f"wechat/articles/draft-public-safe/{ref}.md"
        review = f"wechat/articles/review/{ref}.md"
        for path, content in [(article, "# Reviewed introduction"), (review, "# Content review"),
                              (".agents/skills/wechat-paper/references/writing-standards.md", "Writing rules"),
                              (".agents/skills/wechat-paper/references/natural-scientific-writing.md", "Style rules")]:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        evidence = {"recorded_at": "2026-10-18", "review_path": review,
                    "checks": {"source_identity": True, "facts": True, "public_safety": True,
                               "formula_preview": False, "figure_preview": False, "cover_preview": False}}
        row = {"id": ref, "issued": {"date-parts": [issued or [2025]]}, "custom": {
            "publication_ref": ref, "order": order, "research_family": "工程结构抗风",
            "legacy_bibliography": {"date": date}, "content_production": "included",
            "source": {"status": "verified", "sha256": "a" * 64},
            "wechat": {"status": "awaiting_review", "path": article, "review_path": review,
                       "latest_published_url": "", "evidence": {"content_review": evidence}}}}
        evidence["fingerprint"] = workflow_fingerprint(row, "wechat", root)
        manifest = root / "docs/data/home-progress-selection.json"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        refs = json.loads(manifest.read_text())["publication_refs"] if manifest.exists() else []
        if selected:
            refs.append(ref)
        manifest.write_text(json.dumps({"publication_refs": refs}))
        return row

    def test_filter_precedes_limit_and_never_fills_with_unproduced_articles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            older = self.candidate(root, "eligible-older", [2024], "2024", 1)
            newer = self.candidate(root, "eligible-newer", [2025], "2025", 2)
            invalid = []
            for case in ("pending", "planned", "missing-body", "empty-body", "stale", "missing-review", "failed-check"):
                row = self.candidate(root, case, [2026], "2026")
                workflow = row["custom"]["wechat"]
                if case == "pending":
                    row["custom"]["content_production"] = "pending"
                elif case == "planned":
                    workflow["status"] = "planned"
                elif case == "missing-body":
                    (root / workflow["path"]).unlink()
                elif case == "empty-body":
                    (root / workflow["path"]).write_text(" ")
                elif case == "stale":
                    (root / workflow["path"]).write_text("Changed after review")
                elif case == "missing-review":
                    (root / workflow["review_path"]).unlink()
                else:
                    workflow["evidence"]["content_review"]["checks"]["facts"] = False
                invalid.append(row)
            groups = recent_publications(invalid + [older, newer], root)
            self.assertEqual([r["custom"]["publication_ref"] for r in groups[0][1]],
                             ["eligible-newer", "eligible-older"])
            self.assertEqual(groups[1][1], [])

    def test_produced_content_needs_neither_public_url_nor_phone_preview_or_draft_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = self.candidate(root, "reviewed")
            for status in ("awaiting_review", "draft_created", "ready_to_publish", "published"):
                with self.subTest(status=status):
                    row["custom"]["wechat"]["status"] = status
                    self.assertEqual(recent_publications([row], root)[0][1], [row])

    def test_new_produced_external_interpretation_is_not_automatically_selected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = self.candidate(root, "external", selected=False)
            self.assertEqual(recent_publications([row], root)[0][1], [])

    def test_both_languages_keep_sources_and_never_link_missing_notes(self):
        for english in [False, True]:
            rendered = render_home_progress(ROOT, english=english)
            self.assertEqual(rendered.count('class="work-card"'), 6)
            self.assertEqual(rendered.count('class="progress-family"'), 2)
            self.assertEqual(rendered.count('class="paper-citation"'), 6)
            self.assertNotIn('<details', rendered)
            self.assertNotIn('<summary', rendered)
            self.assertNotIn('原论文题目与作者', rendered)
            for _, rows in recent_publications(load_registry(ROOT), ROOT):
                for row in rows:
                    bib = row["custom"]["legacy_bibliography"]
                    self.assertIn(escape(bib["title"]), rendered)
                    self.assertIn(escape(bib["rendered"]), rendered)
                    self.assertIn("https://doi.org/" + bib["doi"], rendered)
            self.assertNotIn('paper-notes/ref-zhang2025-CSICM.html', rendered)
            self.assertNotIn('data-publication-ref="ref-zhang2025-CSICM"', rendered)
            self.assertIn('data-publication-ref="ref-zheng2025-QHDXXB"', rendered)
            self.assertNotIn('en/highlights/ref-zhao2026-BE', rendered)
            self.assertNotIn('source_audit', rendered)

if __name__ == "__main__":
    unittest.main()
