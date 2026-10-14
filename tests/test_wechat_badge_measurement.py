"""Pixel-derived badge evidence rejects ambiguity and never approves a cover."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.util
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/wechat-cover/scripts/measure_badge.py"
spec = importlib.util.spec_from_file_location("badge_measurement_under_test", SCRIPT)
badge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(badge)


class BadgeMeasurementTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name)
        self.path = self.directory / "candidate.png"
        self.roi = (12, 8, 390, 150)

    def fixture(self, size=(160, 40), origin=(80, 50), palette="numerical", canvas=(900, 383), text=True):
        fill, ink = badge.PALETTES[palette]
        image = Image.new("RGB", canvas, "#EFF6FC" if palette != "offshore" else "#062B4F")
        draw = ImageDraw.Draw(image)
        x, y = origin
        width, height = size
        draw.rounded_rectangle((x, y, x + width - 1, y + height - 1), radius=6, fill=fill)
        if text:
            # Actual glyph ink does not occupy the nominal 24 px font box.
            draw.text((x + 40, y + 6), "ABCD", fill=ink, font=ImageFont.load_default(size=24))
        image.save(self.path)
        return image

    def measure(self, **kwargs):
        return badge.measure_badge(self.path, roi=kwargs.pop("roi", self.roi), palette=kwargs.pop("palette", "numerical"), **kwargs)

    def assertRejected(self, result, reason):
        self.assertEqual(result["status"], "reject", result)
        self.assertFalse(result["raster_gate_passed"])
        self.assertTrue(any(reason in r for r in result["rejection_reasons"]), result)
        self.assertFalse(result["cover_approved"])

    def test_actual_pixels_pass_at_alternate_position_in_all_series_palettes(self):
        for palette in badge.PALETTES:
            with self.subTest(palette=palette):
                self.fixture(palette=palette)
                result = self.measure(palette=palette)
                self.assertEqual(result["status"], "pass", result)
                self.assertEqual(result["badge_bbox_xyxy"], [80, 50, 240, 90])
                self.assertEqual((result["badge_width"], result["badge_height"]), (160, 40))
                self.assertNotEqual(result["badge_bbox_xyxy"], list(self.roi))
                self.assertFalse(result["search_roi_is_measurement"])
                self.assertEqual(result["image_sha256"], hashlib.sha256(self.path.read_bytes()).hexdigest())
                self.assertFalse(result["cover_approved"])
                self.assertFalse(result["backend_preview_checked"])
                self.assertTrue(result["manual_checks_pending"])

    def test_ink_height_is_measured_and_not_misrepresented_as_nominal_font_size(self):
        self.fixture()
        result = self.measure()
        self.assertEqual(result["status"], "pass", result)
        self.assertTrue(result["text_ink_contained"])
        self.assertGreater(result["text_ink_height"], 0)
        self.assertNotEqual(result["text_ink_height"], 24)
        box = result["text_ink_bbox_xyxy"]
        self.assertEqual(result["text_ink_height"], box[3] - box[1])
        self.assertIn("nominal 24 px", result["manual_checks_pending"][0])

    def test_oversized_and_old_128_width_are_measured_then_rejected(self):
        for size in ((200, 60), (128, 40), (160, 60), (200, 40), (207, 53), (208, 53)):
            with self.subTest(size=size):
                self.fixture(size=size)
                result = self.measure()
                self.assertRejected(result, "dimensions_outside")
                self.assertEqual((result["badge_width"], result["badge_height"]), size)

    def test_dimension_tolerance_is_closed_on_both_ends(self):
        for size in ((158, 38), (158, 42), (162, 38), (162, 42)):
            with self.subTest(size=size):
                self.fixture(size=size)
                self.assertEqual(self.measure()["status"], "pass", self.measure())
        for size in ((157, 40), (163, 40), (160, 37), (160, 43), (161, 37), (161, 44)):
            with self.subTest(size=size):
                self.fixture(size=size)
                self.assertRejected(self.measure(), "dimensions_outside")

    def test_wrong_canvas_cannot_pass_even_with_correct_ratio_or_badge(self):
        for canvas in ((1800, 766), (900, 384)):
            with self.subTest(canvas=canvas):
                self.fixture(canvas=canvas)
                self.assertRejected(self.measure(), "incorrect_canvas")

    def test_roi_crop_is_not_a_way_to_claim_a_smaller_badge(self):
        self.fixture(size=(200, 60))
        result = self.measure(roi=(90, 55, 250, 95))
        self.assertRejected(result, "clipped")
        self.assertEqual((result["badge_width"], result["badge_height"]), (160, 40))

    def test_canvas_clipping_and_tight_roi_fail_closed(self):
        self.fixture(origin=(0, 30))
        self.assertRejected(self.measure(roi=(0, 0, 300, 110)), "clipped")
        self.fixture()
        self.assertRejected(self.measure(roi=(79, 49, 241, 91)), "insufficient_search_padding")

    def test_missing_pixels_and_missing_text_reject(self):
        Image.new("RGB", (900, 383), "#EFF6FC").save(self.path)
        self.assertRejected(self.measure(), "no_badge_pixels")
        self.fixture(text=False)
        self.assertRejected(self.measure(), "no_text_ink_pixels")

    def test_two_plausible_badges_reject_instead_of_selecting_best_size(self):
        image = self.fixture()
        ImageDraw.Draw(image).rounded_rectangle((260, 50, 379, 89), radius=6, fill=badge.PALETTES["numerical"][0])
        image.save(self.path)
        self.assertRejected(self.measure(), "ambiguous_badge_components")

    def test_touching_decoration_is_not_accepted_as_badge(self):
        image = self.fixture()
        ImageDraw.Draw(image).rectangle((150, 90, 153, 110), fill=badge.PALETTES["numerical"][0])
        image.save(self.path)
        self.assertRejected(self.measure(), "irregular_badge_shape")

    def test_gradient_and_low_contrast_need_manual_evidence(self):
        image = self.fixture()
        draw = ImageDraw.Draw(image)
        for x in range(82, 238):
            draw.line((x, 53, x, 57), fill=(11 + (x - 82) // 8, 111, 211))
        image.save(self.path)
        self.assertRejected(self.measure(), "nonuniform_fill")
        image = self.fixture()
        image.paste((40, 120, 220), (0, 0, 900, 45))
        image.save(self.path)
        self.assertRejected(self.measure(), "nonuniform_surround")

    def test_text_crossing_boundary_rejects_containment(self):
        image = self.fixture(palette="offshore")
        ImageDraw.Draw(image).rectangle((100, 80, 110, 94), fill=badge.PALETTES["offshore"][1])
        image.save(self.path)
        self.assertRejected(self.measure(palette="offshore"), "text_ink_not_safely_contained")

    def test_antialiasing_uses_documented_pixel_support_not_claimed_box(self):
        for palette in badge.PALETTES:
            with self.subTest(palette=palette):
                fill, ink = badge.PALETTES[palette]
                image = Image.new("RGB", (3600, 1532), "#EFF6FC" if palette != "offshore" else "#062B4F")
                draw = ImageDraw.Draw(image)
                draw.rounded_rectangle((320, 200, 959, 359), radius=24, fill=fill)
                # Deliberately 18 px actual ink, not nominal 24 px.
                for x in (100, 125, 150, 175):
                    draw.rectangle((x * 4, 60 * 4, (x + 12) * 4 - 1, 78 * 4 - 1), fill=ink)
                image.resize((900, 383), Image.Resampling.LANCZOS).save(self.path)
                result = self.measure(palette=palette)
                self.assertEqual(result["status"], "pass", result)
                self.assertEqual(result["badge_bbox_xyxy"], [80, 50, 240, 90])
                self.assertEqual(result["text_ink_height"], 18)
                self.assertEqual(result["thresholds"]["antialias_min_coverage"], 0.5)

    def test_five_character_chinese_direction_does_not_enlarge_fixed_badge(self):
        font_path = Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
        if not font_path.exists():
            self.skipTest("Optional real-CJK-font check; no system CJK font installed")
        image = self.fixture(palette="offshore", text=False)
        ImageDraw.Draw(image).text((100, 52), "混凝土浮体", fill=badge.PALETTES["offshore"][1],
                                   font=ImageFont.truetype(str(font_path), 24))
        image.save(self.path)
        result = self.measure(palette="offshore")
        self.assertEqual(result["status"], "pass", result)
        self.assertEqual((result["badge_width"], result["badge_height"]), (160, 40))
        self.assertTrue(result["text_ink_contained"])

    def test_low_contrast_background_rejects_even_when_badge_is_detectable(self):
        image = Image.new("RGB", (900, 383), (45, 140, 230))
        draw = ImageDraw.Draw(image)
        fill, ink = badge.PALETTES["numerical"]
        draw.rounded_rectangle((80, 50, 239, 89), radius=6, fill=fill)
        draw.rectangle((120, 60, 180, 77), fill=ink)
        image.save(self.path)
        self.assertRejected(self.measure(), "low_contrast_boundary")

    def test_interior_color_patch_is_not_hidden_by_core_color_threshold(self):
        image = self.fixture()
        ImageDraw.Draw(image).rectangle((88, 55, 110, 84), fill=(31, 111, 211))
        image.save(self.path)
        self.assertRejected(self.measure(), "nonuniform_fill")

    def test_colored_border_cannot_hide_an_oversized_outer_badge(self):
        for border_width in (2, 10):
            with self.subTest(border_width=border_width):
                image = self.fixture()
                draw = ImageDraw.Draw(image)
                draw.rectangle((80 - border_width, 50 - border_width, 239 + border_width, 89 + border_width),
                               outline=(70, 0, 70), width=border_width)
                image.save(self.path)
                self.assertRejected(self.measure(), "border")

    def test_cli_never_overwrites_input_or_its_hardlink(self):
        self.fixture()
        original = self.path.read_bytes()
        alias = self.directory / "alias.png"
        alias.hardlink_to(self.path)
        for target in (self.path, alias):
            with self.subTest(target=target), redirect_stderr(StringIO()), self.assertRaises(SystemExit):
                badge.main([str(self.path), "--roi", *map(str, self.roi), "--palette", "numerical", "--output", str(target)])
            self.assertEqual(self.path.read_bytes(), original)

    def test_prompt_only_or_supplied_bbox_never_proves_measurement(self):
        self.path.write_text("Badge: 160x40, font 24, measured bbox [80,50,240,90]", encoding="utf-8")
        self.assertRejected(self.measure(), "unreadable_raster")
        with self.assertRaises(TypeError):
            badge.measure_badge(self.path, roi=self.roi, palette="numerical", bbox=(80, 50, 240, 90))

    def test_bad_roi_transparency_and_unknown_palette_reject(self):
        self.fixture()
        for roi in ((80, 90, 240, 50), (-1, 0, 400, 150), (0, 0, 901, 383), (0.0, 0, 400, 150)):
            with self.subTest(roi=roi):
                self.assertRejected(self.measure(roi=roi), "invalid_search_roi")
        self.assertRejected(self.measure(palette="invented"), "unknown_palette")
        Image.new("RGBA", (900, 383), (0, 0, 0, 0)).save(self.path)
        self.assertRejected(self.measure(), "transparent_final_raster")

    def test_cli_json_and_exit_code_distinguish_raster_pass_and_rejection(self):
        report = self.directory / "measurement.json"
        for size, expected_code in (((160, 40), 0), ((200, 60), 1)):
            with self.subTest(size=size):
                self.fixture(size=size)
                output = StringIO()
                with redirect_stdout(output):
                    code = badge.main([str(self.path), "--roi", *map(str, self.roi), "--palette", "numerical", "--output", str(report)])
                self.assertEqual(code, expected_code)
                self.assertEqual(json.loads(output.getvalue()), json.loads(report.read_text()))
                self.assertFalse(json.loads(output.getvalue())["cover_approved"])


if __name__ == "__main__":
    unittest.main()
