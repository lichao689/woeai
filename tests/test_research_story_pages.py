"""Research pages follow the five canonical subdirections in both languages."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/source'
FAMILIES = {'StructuralWindEngineering': ['NumericalWindTunnel', 'StructuralWindResistance'],
            'MarineEnergyStructures': ['IntegratedAnalysis', 'ConcreteFloatingStructures', 'NumericalWaveBasin']}
STORIES = {'NumericalWindTunnel': ['ref-chen2024-JCP', 'ref-zhao2026-BS'],
           'StructuralWindResistance': ['ref-tang2025-JBE'],
           'IntegratedAnalysis': ['ref-zhou2023-AE', 'ref-zheng2023-JRSE'],
           'ConcreteFloatingStructures': ['ref-he2026-OE-structural']}

class ResearchStoryPagesTests(unittest.TestCase):
    def test_five_real_subdirections_have_bilingual_pages_and_heading_free_openings(self):
        for parent, children in FAMILIES.items():
            for prefix in ['', 'en/']:
                overview = (SOURCE / f'{prefix}{parent}.rst').read_text()
                for doc in children:
                    self.assertIn(doc, overview)
                    text = (SOURCE / f'{prefix}{doc}.rst').read_text()
                    self.assertIn(parent, text)
                    self.assertRegex(text, r'(?m)^- .+')
                for doc in [parent, *children]:
                    text = (SOURCE / f'{prefix}{doc}.rst').read_text()
                    self.assertNotRegex(text, r'(?m)^(研究背景|核心问题|Background|Research questions)\n[-~]+')

    def test_stories_have_one_primary_page_and_preserve_complete_evidence(self):
        for doc, refs in STORIES.items():
            for prefix in ['', 'en/']:
                text = (SOURCE / f'{prefix}{doc}.rst').read_text()
                for ref in refs:
                    self.assertIn(f'.. _{ "en-" if prefix else ""}story-{ref}:', text)
                    for other in set(STORIES) - {doc}:
                        self.assertNotIn(f'.. _{ "en-" if prefix else ""}story-{ref}:', (SOURCE / f'{prefix}{other}.rst').read_text())
        for prefix in ['', 'en/']:
            wave = (SOURCE / f'{prefix}NumericalWaveBasin.rst').read_text()
            self.assertNotIn('.. _story-', wave)
            self.assertNotIn('.. _en-story-', wave)
            self.assertIn('IntegratedAnalysis', wave)
        english = (SOURCE / 'en/Research.rst').read_text()
        for refs in STORIES.values():
            for ref in refs:
                self.assertIn(f'highlights/{ref}', english)

    def test_existing_technical_figures_remain_available_under_their_own_subjects(self):
        for doc, names in {'IntegratedAnalysis': ['sea_floating_wind_turbine_optimization', 'multiphysics_multibody_model_floating_wind_turbine_optimization'],
                           'ConcreteFloatingStructures': ['concrete_structure_floating_wind_turbine_optimization']}.items():
            text = (SOURCE / f'{doc}.rst').read_text()
            self.assertIn('<details', text)
            for name in names:
                self.assertIn(name+'.png', text)
            self.assertIn(':width: 100%', text)

if __name__ == '__main__':
    unittest.main()
