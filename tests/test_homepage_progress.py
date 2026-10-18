"""Latest homepage papers are selected by publication date in both languages."""
from copy import deepcopy
from html import escape
from pathlib import Path
import unittest

from woeai.publications.homepage import recent_publications, render_home_progress, publication_date
from woeai.publications.registry import load_registry

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "工程结构抗风": ["ref-zhao2026-BE", "ref-he2026-OE", "ref-zhao2026-BS"],
    "海洋能源结构": ["ref-he2026-OE-structural", "ref-zhang2025-CSICM", "ref-zheng2025-OE"],
}

class HomepageProgressTests(unittest.TestCase):
    def test_latest_three_per_family_include_papers_without_reading_notes(self):
        groups = recent_publications(load_registry(ROOT))
        self.assertEqual({family: [r["custom"]["publication_ref"] for r in rows] for family, rows in groups}, EXPECTED)

    def test_date_precision_and_stable_ties_do_not_follow_manual_highlight_order(self):
        rows = load_registry(ROOT)
        base = deepcopy(rows[0])
        candidates = []
        for ref, issued, date, order in [
            ("year-only", [2025], "2025", 0),
            ("early", [2025], "2025/2/1", 1),
            ("late", [2025], "2025-12-02", 20),
            ("same-date", [2025], "2025/12/2", 21),
            ("explicit", [2025, 12, 3], "2025/1", 99),
        ]:
            row = deepcopy(base)
            row["issued"] = {"date-parts": [issued]}
            row["custom"].update(publication_ref=ref, order=order)
            row["custom"]["legacy_bibliography"]["date"] = date
            candidates.append(row)
        groups = recent_publications(list(reversed(candidates)))
        self.assertEqual([r["custom"]["publication_ref"] for r in groups[0][1]], ["explicit", "late", "same-date"])
        self.assertEqual(publication_date(candidates[0]), (2025, 0, 0))

    def test_both_languages_keep_sources_and_never_link_missing_notes(self):
        for english in [False, True]:
            rendered = render_home_progress(ROOT, english=english)
            self.assertEqual(rendered.count('class="work-card"'), 6)
            self.assertEqual(rendered.count('class="progress-family"'), 2)
            self.assertEqual(rendered.count('class="paper-citation"'), 6)
            self.assertNotIn('<details', rendered)
            self.assertNotIn('<summary', rendered)
            self.assertNotIn('原论文题目与作者', rendered)
            for _, rows in recent_publications(load_registry(ROOT)):
                for row in rows:
                    bib = row["custom"]["legacy_bibliography"]
                    self.assertIn(escape(bib["title"]), rendered)
                    self.assertIn(escape(bib["rendered"]), rendered)
                    self.assertIn("https://doi.org/" + bib["doi"], rendered)
            self.assertNotIn('paper-notes/ref-zhang2025-CSICM.html', rendered)
            self.assertIn('Publications.html#' + ('en-' if english else '') + 'ref-zhang2025-csicm', rendered)
            self.assertNotIn('en/highlights/ref-zhao2026-BE', rendered)
            self.assertNotIn('source_audit', rendered)
            unreviewed = rendered.split('data-publication-ref="ref-zhang2025-CSICM"', 1)[1].split('</article>', 1)[0]
            self.assertNotIn('<figure', unreviewed)
            self.assertNotIn('<strong>Problem', unreviewed)
            self.assertNotIn('<strong>问题', unreviewed)
            self.assertNotIn('Chinese reading notes', unreviewed)

if __name__ == "__main__":
    unittest.main()
