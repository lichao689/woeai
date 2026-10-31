"""Research narratives stay bilingual, source-bounded and separately navigable."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/source'
STORIES = {
    'StructuralWindEngineering': ['ref-chen2024-JCP', 'ref-zhao2026-BS', 'ref-tang2025-JBE'],
    'MarineEnergyStructures': ['ref-zhou2023-AE', 'ref-he2026-OE-structural', 'ref-zheng2023-JRSE'],
}

class ResearchStoryPagesTests(unittest.TestCase):
    def test_both_languages_have_matching_evidence_and_narrative_sections(self):
        for doc, refs in STORIES.items():
            for prefix, headings in [('', ['研究背景', '核心问题', '方法与创新', '代表成果与验证', '仍待解决的问题', '论文与项目']),
                                     ('en/', ['Background', 'Research questions', 'Methods and contributions', 'Evidence in practice', 'Open questions', 'Publications and projects'])]:
                text = (SOURCE / f'{prefix}{doc}.rst').read_text()
                for heading in headings:
                    self.assertRegex(text, rf'(?m)^{re.escape(heading)}\n-+')
                for ref in refs:
                    self.assertIn(ref, text)
                self.assertIn(':figclass: research-method', text)
                self.assertIn(':width: 100%', text)
                self.assertNotIn('仅使用水动力软件不构成本方向', text)
                self.assertNotIn('在公开页面中归入本子方向', text)

    def test_the_overviews_link_to_local_topics_and_preserve_highlights(self):
        for prefix in ['', 'en/']:
            text = (SOURCE / f'{prefix}Research.rst').read_text()
            for doc in STORIES:
                self.assertIn(doc, text)
        english = (SOURCE / 'en/Research.rst').read_text()
        for refs in STORIES.values():
            for ref in refs:
                self.assertIn(f'highlights/{ref}', english)

    def test_existing_technical_figures_remain_available_in_details(self):
        text = (SOURCE / 'MarineEnergyStructures.rst').read_text()
        for name in ['sea_floating_wind_turbine_optimization', 'concrete_structure_floating_wind_turbine_optimization', 'multiphysics_multibody_model_floating_wind_turbine_optimization']:
            self.assertIn(name+'.png', text)
        self.assertIn('<details', text)

if __name__ == '__main__':
    unittest.main()
