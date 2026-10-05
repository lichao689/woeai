"""Cover previews report geometry without claiming visual/backend acceptance."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ('.agents/skills/wechat-cover/scripts/cover_preview.py',
           'wechat/tools/cover_preview.py')


def load_module(relative):
    spec = importlib.util.spec_from_file_location('preview_under_test', ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CoverPreviewTests(unittest.TestCase):
    def test_exact_dimensions_are_distinct_from_ratio(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'sample.png'
            for script in SCRIPTS:
                module = load_module(script)
                for width, height, expected in ((900, 383, True), (1800, 766, False)):
                    with self.subTest(script=script, width=width):
                        # Header-only parser intentionally needs no imaging dependency.
                        path.write_bytes(b'\x89PNG\r\n\x1a\n' + b'\0' * 8 +
                                         width.to_bytes(4, 'big') + height.to_bytes(4, 'big'))
                        summary = module.cover_summary(path, 900, 383, 1000)
                        self.assertTrue(summary['target_ratio_match'])
                        self.assertEqual(summary['target_dimensions_match'], expected)
                        self.assertEqual(summary['series_v2_dimensions_match'], expected)
                        self.assertFalse(summary['visual_contract_checked'])
                        self.assertFalse(summary['backend_preview_checked'])

    def test_square_crop_matches_landscape_geometry(self):
        for script in SCRIPTS:
            module = load_module(script)
            with self.subTest(script=script):
                rendered = module.render_card({'path': 'sample.png', 'width': 900, 'height': 383})
                self.assertIn('left: 28.7222%; top: 0.0000%; width: 42.5556%; height: 100.0000%', rendered)
                self.assertIn('Mobile wide (360 px)', rendered)
                self.assertIn('does not preserve the entire left title', rendered)

    def test_full_source_and_square_overlay_support_nonstandard_portrait(self):
        for script in SCRIPTS:
            module = load_module(script)
            for width, height, ratio, rectangle in (
                (400, 800, '0.50000000', 'left: 0.0000%; top: 25.0000%; width: 100.0000%; height: 50.0000%'),
                (800, 400, '2.00000000', 'left: 25.0000%; top: 0.0000%; width: 50.0000%; height: 100.0000%'),
            ):
                with self.subTest(script=script, width=width):
                    page = module.render_page([{'path': 'sample.png', 'width': width, 'height': height}])
                    self.assertIn('Full source (uncropped)', page)
                    self.assertIn(f'class="frame wide" style="aspect-ratio: {ratio}"', page)
                    self.assertIn(rectangle, page)
                    self.assertIn('.frame.wide img { object-fit: contain; }', page)

    def test_invalid_target_dimensions_fail_explicitly(self):
        for script in SCRIPTS:
            module = load_module(script)
            with self.subTest(script=script), self.assertRaises(ValueError):
                module.cover_summary(Path('unused.png'), 900, 0, 1000)


if __name__ == '__main__':
    unittest.main()
