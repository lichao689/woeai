"""Exercise numbering through real Sphinx HTML, including generated contents."""
import io
import tempfile
import unittest
from pathlib import Path
from sphinx.application import Sphinx

ROOT = Path(__file__).resolve().parents[1]


class SectionNumberingTests(unittest.TestCase):
    def build(self, text, docname="Research"):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        source = root / "source"
        source.mkdir()
        (source / "conf.py").write_text(
            "import sys\nsys.path.insert(0, " + repr(str(ROOT / "docs/source")) + ")\n"
            "extensions=['body_section_numbering']\nmaster_doc='index'\nhtml_theme='basic'\n")
        (source / "index.rst").write_text("Home\n====\n\n.. toctree::\n\n   " + docname + "\n")
        page = source / (docname + ".rst")
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(text)
        app = Sphinx(str(source), str(source), str(root / "html"), str(root / "doctrees"),
                     "html", status=io.StringIO(), warning=io.StringIO(),
                     warningiserror=True, freshenv=True)
        app.build(force_all=True)
        return app, (root / "html" / (docname + ".html")).read_text()

    def test_two_body_levels_and_generated_local_contents_share_numbers(self):
        app, html = self.build("""Research
========

.. contents:: On this page
   :local:

Wind
----

Tunnel
~~~~~~

Details
^^^^^^^

Resistance
~~~~~~~~~~

Ocean
-----

Analysis
~~~~~~~~
""")
        self.assertIn('<span class="body-section-number">1 </span>Wind', html)
        self.assertIn('<span class="body-section-number">1.1 </span>Tunnel', html)
        self.assertIn('<span class="body-section-number">1.2 </span>Resistance', html)
        self.assertIn('<span class="body-section-number">2.1 </span>Analysis', html)
        self.assertNotIn('1.1.1', html)
        self.assertEqual(html.count('<span class="body-section-number">1.1 </span>'), 2)
        # Global navigation must keep the original labels, not the body counters.
        self.assertNotIn('body-section-number', app.env.tocs['Research'].pformat())
        app.build(force_all=True)
        rebuilt = (Path(app.outdir) / 'Research.html').read_text()
        self.assertEqual(rebuilt.count('<span class="body-section-number">1.1 </span>'), 2)

    def test_reference_section_is_excluded_without_shifting_following_sections(self):
        _, html = self.build("""A document
==========

First
-----

.. rst-class:: unnumbered-reference

Source paper
------------

Keep the citation [9] and DOI unchanged.

Second
------
""")
        self.assertIn('<span class="body-section-number">1 </span>First', html)
        self.assertIn('<span class="body-section-number">2 </span>Second', html)
        self.assertNotIn('</span>Source paper', html)
        self.assertIn('Keep the citation [9] and DOI unchanged.', html)

    def test_each_english_page_starts_at_one(self):
        for docname in ['en/Research', 'en/JoinUs']:
            with self.subTest(docname=docname):
                _, html = self.build('English page\n============\n\nFirst\n-----\n\nChild\n~~~~~\n', docname)
                self.assertIn('<span class="body-section-number">1 </span>First', html)
                self.assertIn('<span class="body-section-number">1.1 </span>Child', html)

    def test_home_indexes_and_original_paper_numbers_are_unchanged(self):
        for docname in ['index', 'Publications', 'PublicationsByYear', 'paper-notes/ref-example']:
            with self.subTest(docname=docname):
                _, html = self.build('Title\n=====\n\n1 Original\n----------\n\n1.1 Method\n~~~~~~~~~~\n', docname)
                self.assertNotIn('body-section-number', html)
                self.assertIn('1.1 Method', html)

    def test_manual_numbers_on_ordinary_headings_fail_the_build(self):
        from sphinx.errors import SphinxError
        for heading, underline in [('1 Manual', '-'), ('1.1.1 Manual', '^'), ('1、方法', '-'), ('1.1方法', '-'), ('1.方法', '-'), ('1）方法', '-')]:
            with self.subTest(heading=heading):
                text = 'Title\n=====\n\nParent\n------\n\nChild\n~~~~~\n\n' + heading + '\n' + underline * len(heading) + '\n'
                with self.assertRaisesRegex(SphinxError, 'manual section number'):
                    self.build(text)

    def test_generated_teaching_source_does_not_supply_its_own_counters(self):
        from test_update_publications_from_zotero import load_publication_script
        text = load_publication_script().build_teaching_rst([])
        self.assertIn('\n教学工作 Teaching\n', text)
        self.assertIn('\n本科生 Undergraduate\n', text)
        self.assertIn('\n博士生 PhD Students\n', text)
        self.assertNotRegex(text, r'(?m)^\d+(?:\.\d+)*\s+.+\n[-~]+$')

    def test_scientific_3d_heading_is_not_a_manual_number(self):
        _, html = self.build('Title\n=====\n\n3D geometry\n-----------\n')
        self.assertIn('<span class="body-section-number">1 </span>3D geometry', html)
