"""Public citation contracts for every Chinese note and English highlight."""
from copy import deepcopy
from pathlib import Path
import json
import tempfile
import unittest

from woeai.publications.citations import citation_for_record

ROOT = Path(__file__).resolve().parents[1]


class PaperCitationTests(unittest.TestCase):
    def test_checked_citation_keeps_full_bibliography_and_adds_known_doi(self):
        rows = json.loads((ROOT / "docs/data/publications.json").read_text())
        row = next(r for r in rows if r["custom"]["publication_ref"] == "ref-zheng2025-QHDXXB")
        text = citation_for_record(row)
        self.assertIn("郑舜云; 周盛涛; 石兵; 李朝; 胡钢; 曾宇; 李利孝", text)
        self.assertIn("中心与偏心布置半潜风机动力特性的模型试验", text)
        self.assertIn("清华大学学报（自然科学版）, 2025", text)
        self.assertIn("https://doi.org/10.16511/j.cnki.qhdxxb.2025.27.037", text)

    def test_missing_placeholder_or_inconsistent_fields_are_hard_errors(self):
        rows = json.loads((ROOT / "docs/data/publications.json").read_text())
        original = next(r for r in rows if r["custom"]["publication_ref"] == "ref-zhao2026-BE")
        cases = {
            "title": "", "publicationTitle": "TODO", "creators": [], "year": None,
            "rendered": "See the publication record", "doi": "TBD",
        }
        for field, value in cases.items():
            with self.subTest(field=field):
                row = deepcopy(original)
                row["custom"]["legacy_bibliography"][field] = value
                with self.assertRaisesRegex(ValueError, "ref-zhao2026-BE.*" + field):
                    citation_for_record(row)
        for value in [
            "A novel framework for urban geometry rapid reconstruction utilizing high-resolution stereo satellite imagery for wind environment assessment[J]. Building and Environment, 2026.",
            "Wrong Author, " + original["custom"]["legacy_bibliography"]["rendered"].split(", ", 1)[1],
        ]:
            with self.subTest(rendered=value):
                row = deepcopy(original)
                row["custom"]["legacy_bibliography"]["rendered"] = value
                with self.assertRaisesRegex(ValueError, "ref-zhao2026-BE.*rendered"):
                    citation_for_record(row)

    def test_all_existing_reading_pages_have_complete_registered_citation_data(self):
        rows = json.loads((ROOT / "docs/data/publications.json").read_text())
        by_ref = {r["custom"]["publication_ref"]: r for r in rows}
        pages = list((ROOT / "docs/source/paper-notes").glob("*.rst")) + list((ROOT / "docs/source/en/highlights").glob("*.rst"))
        for page in pages:
            with self.subTest(page=page):
                text = citation_for_record(by_ref[page.stem])
                self.assertNotIn("影响因子", text)
                self.assertNotIn("中科院分区", text)
                self.assertTrue(text.strip())

    def test_sphinx_populates_empty_citation_bodies_in_both_reader_languages(self):
        import io
        from sphinx.application import Sphinx
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "docs/source"
            source.mkdir(parents=True)
            rows = json.loads((ROOT / "docs/data/publications.json").read_text())
            row = next(r for r in rows if r["custom"]["publication_ref"] == "ref-zhao2026-BE")
            (root / "docs/data").mkdir()
            (root / "docs/data/publications.json").write_text(json.dumps([row]))
            (source / "conf.py").write_text(
                "import sys\nsys.path.insert(0, " + repr(str(ROOT / "docs/source")) + ")\n"
                "sys.path.insert(0, " + repr(str(ROOT)) + ")\n"
                "extensions=['paper_citations']\nmaster_doc='index'\nhtml_theme='basic'\n")
            (source / "index.rst").write_text("Reader test\n===========\n\n.. toctree::\n\n   paper-notes/ref-zhao2026-BE\n   en/highlights/ref-zhao2026-BE\n")
            for folder, heading in [("paper-notes", "完整引用"), ("en/highlights", "Source paper")]:
                path = source / folder / "ref-zhao2026-BE.rst"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("A reader\n========\n\nScientific body must stay.\n\n" + heading + "\n" + "-" * 20 + "\n\nOnly a record link, no citation.\n")
            out = root / "html"
            app = Sphinx(str(source), str(source), str(out), str(root / "doctrees"), "html",
                         status=io.StringIO(), warning=io.StringIO(), warningiserror=True, freshenv=True)
            app.build(force_all=True)
            for folder in ("paper-notes", "en/highlights"):
                html = (out / folder / "ref-zhao2026-BE.html").read_text()
                self.assertIn('class="paper-full-citation"', html)
                self.assertIn("Zhao Peisheng; Li Chao; Chen Lingwei", html)
                self.assertIn("Scientific body must stay.", html)
                self.assertNotIn("Only a record link, no citation.", html)

    def test_structured_registry_changes_cannot_leave_stale_compatibility_citations(self):
        row = next(r for r in json.loads((ROOT / "docs/data/publications.json").read_text())
                   if r["custom"]["publication_ref"] == "ref-zhao2026-BE")
        for field, value in [("title", "A different checked title"),
                             ("container-title", "Different Journal"),
                             ("DOI", "10.1000/changed"),
                             ("issued", {"date-parts": [[2030]]}),
                             ("author", [{"literal": "Different Author"}])]:
            with self.subTest(field=field):
                changed = deepcopy(row)
                changed[field] = value
                with self.assertRaisesRegex(ValueError, "ref-zhao2026-BE.*inconsistent"):
                    citation_for_record(changed)

    def test_built_html_gate_rejects_missing_empty_wrong_or_hidden_citations(self):
        from html import escape
        from woeai.publications.citations import check_built_citations
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row = next(r for r in json.loads((ROOT / "docs/data/publications.json").read_text())
                       if r["custom"]["publication_ref"] == "ref-zhao2026-BE")
            (root / "docs/data").mkdir(parents=True)
            (root / "docs/data/publications.json").write_text(json.dumps([row]))
            source = root / "docs/source/paper-notes/ref-zhao2026-BE.rst"
            source.parent.mkdir(parents=True)
            source.write_text("Reader\n======\n")
            out = root / "html"
            target = out / "paper-notes/ref-zhao2026-BE.html"
            target.parent.mkdir(parents=True)
            self.assertTrue(check_built_citations(root, out))
            citation = citation_for_record(row)
            doi = row["custom"]["legacy_bibliography"]["doi"]
            valid = '<p class="paper-full-citation">' + escape(citation) + '</p>'
            valid = valid.replace(doi, '<a href="https://doi.org/' + doi + '">' + doi + '</a>')
            target.write_text(valid)
            self.assertEqual(check_built_citations(root, out), [])
            for html in ["<p>Only the record link</p>", '<p class="paper-full-citation"> </p>',
                         '<p class="paper-full-citation">TODO</p>',
                         '<div hidden>' + valid + '</div>', '<div style="display:none">' + valid + '</div>',
                         valid + valid]:
                with self.subTest(html=html):
                    target.write_text(html)
                    problems = check_built_citations(root, out)
                    self.assertTrue(problems)
                    self.assertIn("ref-zhao2026-BE", problems[0])

    def test_obvious_placeholder_metadata_is_not_a_valid_full_citation(self):
        row = next(r for r in json.loads((ROOT / "docs/data/publications.json").read_text())
                   if r["custom"]["publication_ref"] == "ref-zhao2026-BE")
        for placeholder in ("N/A", "None", "Unknown"):
            changed = deepcopy(row)
            title = changed["custom"]["legacy_bibliography"]["title"]
            changed["title"] = changed["custom"]["legacy_bibliography"]["title"] = placeholder
            changed["custom"]["legacy_bibliography"]["rendered"] = changed["custom"]["legacy_bibliography"]["rendered"].replace(title, placeholder)
            with self.subTest(placeholder=placeholder):
                with self.assertRaisesRegex(ValueError, "ref-zhao2026-BE.*title"):
                    citation_for_record(changed)

    def test_source_version_notes_are_preserved_in_full_citations(self):
        rows = json.loads((ROOT / "docs/data/publications.json").read_text())
        for ref in ("ref-zheng2025-QHDXXB", "ref-zhao2023-GYJZ"):
            row = next(r for r in rows if r["custom"]["publication_ref"] == ref)
            self.assertIn("网络首发稿", citation_for_record(row))
            self.assertIn("不代表", citation_for_record(row))
