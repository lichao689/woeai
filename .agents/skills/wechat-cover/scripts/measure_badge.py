#!/usr/bin/env python3
"""Measure an isolated solid badge in actual final-cover pixels, not a prompt.

A pass is only raster geometry/containment evidence. Font size/weight, corner
radius, wording, science and backend rendering ALWAYS require separate review.
The ROI is a generously padded search area, never a supplied measurement.
Unsupported gradients, touching decoration, low contrast, clipping or ambiguous
color components reject automatic evidence rather than guessing a boundary.
Requires Pillow; never resizes, generates or modifies the input image.
"""
from __future__ import annotations

import argparse
import hashlib
from io import BytesIO
import json
from pathlib import Path
from statistics import median
from typing import Any

from PIL import Image, ImageFilter

CANVAS = (900, 383)
BADGE = (160, 40)
DIMENSION_TOLERANCE = 2
PALETTES = {
    "numerical": ((11, 111, 211), (255, 255, 255)),
    "structural": ((15, 118, 110), (217, 255, 242)),
    "offshore": ((255, 200, 61), (6, 43, 79)),
}
THRESHOLDS = {
    "color_max_channel_error": 24,
    "blend_max_channel_residual": 12,
    "antialias_min_coverage": 0.5,
    "antialias_boundary_uncertainty_px": 2,
    "minimum_search_padding_px": 6,
    "minimum_component_pixels": 32,
    "background_max_channel_variation": 16,
    "minimum_fill_background_channel_contrast": 64,
    "interior_max_channel_variation": 8,
    "minimum_silhouette_box_coverage": 0.94,
}
PENDING = [
    "nominal 24 px font size (not the measured glyph ink height)",
    "bold 700 font weight and intended typeface",
    "6 px corner radius",
    "exact confirmed text, upright lettering, legibility and visual balance",
    "scientific accuracy and series composition",
    "actual WeChat backend mobile preview",
]


def _near(pixel: tuple[int, ...], color: tuple[int, ...], tolerance: int) -> bool:
    return max(abs(a - b) for a, b in zip(pixel, color)) <= tolerance


def _coverage(pixel, foreground, background):
    """RGB channel-space blend estimate, not physical alpha or font metadata."""
    direction = [f - b for f, b in zip(foreground, background)]
    denominator = sum(d * d for d in direction)
    if not denominator:
        return False
    alpha = sum((p - b) * d for p, b, d in zip(pixel, background, direction)) / denominator
    residual = max(abs(p - (b + alpha * d)) for p, b, d in zip(pixel, background, direction))
    return 0.5 <= alpha <= 1.1 and residual <= 12


def _bbox(points, width, offset=(0, 0)):
    xs, ys = zip(*((i % width, i // width) for i in points))
    return [min(xs) + offset[0], min(ys) + offset[1],
            max(xs) + 1 + offset[0], max(ys) + 1 + offset[1]]


def _components(mask, width, height):
    remaining = {i for i, present in enumerate(mask) if present}
    found = []
    while remaining:
        start = remaining.pop()
        component, stack = {start}, [start]
        while stack:
            i = stack.pop()
            x, y = i % width, i // width
            for yy in range(max(0, y - 1), min(height, y + 2)):
                for xx in range(max(0, x - 1), min(width, x + 2)):
                    j = yy * width + xx
                    if j in remaining:
                        remaining.remove(j)
                        component.add(j)
                        stack.append(j)
        found.append(component)
    return sorted(found, key=len, reverse=True)


def _outer_components(components, width):
    """Counters inside glyphs are fill islands, not second badge candidates."""
    outer = []
    for component in components:
        if len(component) < 32:
            continue
        for parent in outer:
            if component.issubset(_silhouette(parent, width)):
                parent.update(component)
                break
        else:
            outer.append(set(component))
    return outer


def _pixel_data(image):
    # Pillow 12.0 is the project's pinned dependency; 12.3 renamed this API.
    getter = getattr(image, "get_flattened_data", None)
    return list(getter() if getter else image.getdata())


def _silhouette(component, width):
    rows, columns = {}, {}
    for i in component:
        x, y = i % width, i // width
        rows.setdefault(y, []).append(x)
        columns.setdefault(x, []).append(y)
    row_bounds = {y: (min(xs), max(xs)) for y, xs in rows.items()}
    col_bounds = {x: (min(ys), max(ys)) for x, ys in columns.items()}
    return {
        y * width + x
        for y, (left, right) in row_bounds.items()
        for x in range(left, right + 1)
        if x in col_bounds and col_bounds[x][0] <= y <= col_bounds[x][1]
    }


def _finish(result):
    result["raster_gate_passed"] = not result["rejection_reasons"]
    result["status"] = "pass" if result["raster_gate_passed"] else "reject"
    return result


def measure_badge(path: str | Path, *, roi, palette: str) -> dict[str, Any]:
    """Return auditable JSON-compatible raster evidence; invalid inputs reject.

    ``roi`` is (x0, y0, x1, y1), exclusive, in the unmodified final 900x383
    image. Leave at least six pixels outside all badge edges. No position,
    category wording, claimed bbox or nominal-font measurement is accepted.
    """
    result = {
        "schema_version": 1,
        "status": "reject",
        "raster_gate_passed": False,
        "cover_approved": False,
        "visual_contract_checked": False,
        "backend_preview_checked": False,
        "image_sha256": None,
        "canvas": None,
        "search_roi_xyxy": list(roi) if isinstance(roi, (tuple, list)) else None,
        "search_roi_is_measurement": False,
        "palette": palette,
        "required_badge_dimensions": list(BADGE),
        "dimension_tolerance_px": DIMENSION_TOLERANCE,
        "badge_bbox_xyxy": None,
        "badge_width": None,
        "badge_height": None,
        "badge_dimensions_within_tolerance": False,
        "text_ink_bbox_xyxy": None,
        "text_ink_width": None,
        "text_ink_height": None,
        "text_ink_contained": False,
        "method": "isolated palette component; 8-connectivity; local-background RGB channel-space support >=50%; exclusive pixel bbox",
        "thresholds": dict(THRESHOLDS),
        "manual_checks_pending": list(PENDING),
        "limitations": [
            "Measures color support, not OCR, nominal font size, physical alpha or exact corner radius.",
            "Antialiased fringes below 50% estimated coverage are excluded; at most 2 px edge uncertainty is allowed.",
            "Search ROI must include the whole badge and isolation margin; it does not certify the rest of the image.",
            "Gradients, low contrast, texture and touching decoration need independent manual boundary evidence; do not override a rejection with a claimed bbox.",
        ],
        "rejection_reasons": [],
    }
    reject = result["rejection_reasons"].append
    if palette not in PALETTES:
        reject("unknown_palette")
        return result
    fill, ink = PALETTES[palette]
    result["fill_rgb"], result["text_rgb"] = list(fill), list(ink)
    try:
        data = Path(path).read_bytes()
        result["image_sha256"] = hashlib.sha256(data).hexdigest()
        with Image.open(BytesIO(data)) as source:
            result["canvas"] = list(source.size)
            if source.size != CANVAS:
                reject("incorrect_canvas: final pixels must be 900x383")
                return result
            if getattr(source, "n_frames", 1) != 1 or source.getexif().get(274, 1) != 1:
                reject("ambiguous_frame_or_orientation")
                return result
            rgba = source.convert("RGBA")
            if rgba.getchannel("A").getextrema() != (255, 255):
                reject("transparent_final_raster")
                return result
            image = rgba.convert("RGB")
    except (OSError, ValueError, Image.DecompressionBombError):
        reject("unreadable_raster: actual image bytes are required; prompts are not measurements")
        return result
    if (not isinstance(roi, (tuple, list)) or len(roi) != 4
            or any(type(n) is not int for n in roi)):
        reject("invalid_search_roi")
        return result
    x0, y0, x1, y1 = roi
    if not (0 <= x0 < x1 <= CANVAS[0] and 0 <= y0 < y1 <= CANVAS[1]):
        reject("invalid_search_roi")
        return result
    width, height = x1 - x0, y1 - y0
    pixels = _pixel_data(image.crop(roi))
    fill_mask = [_near(p, fill, 24) for p in pixels]
    components = _components(fill_mask, width, height)
    plausible = _outer_components(components, width)
    result["palette_component_count"] = len(plausible)
    if not plausible:
        reject("no_badge_pixels")
        return result
    if len(plausible) != 1:
        reject("ambiguous_badge_components")
        return result
    component = plausible[0]
    local = _bbox(component, width)

    def record(box):
        left, top, right, bottom = box
        result["badge_bbox_xyxy"] = [left + x0, top + y0, right + x0, bottom + y0]
        result["badge_width"], result["badge_height"] = right - left, bottom - top
        result["badge_dimensions_within_tolerance"] = all(
            abs(measured - target) <= DIMENSION_TOLERANCE
            for measured, target in zip((right - left, bottom - top), BADGE)
        )

    record(local)
    left, top, right, bottom = local
    margins = (left, top, width - right, height - bottom)
    if min(margins) == 0:
        reject("badge_clipped_at_search_roi_or_canvas_edge")
        return result
    if min(margins) < 6:
        reject("insufficient_search_padding: need at least 6 px around detected badge")
        return result
    ring = [
        pixels[y * width + x]
        for y in range(top - 6, bottom + 6)
        for x in range(left - 6, right + 6)
        if x < left - 2 or x >= right + 2 or y < top - 2 or y >= bottom + 2
    ]
    background = tuple(round(median(p[c] for p in ring)) for c in range(3))
    result["local_background_rgb"] = list(background)
    if not all(_near(p, background, 16) for p in ring):
        reject("nonuniform_surround: gradient_or_touching_decoration_requires_manual_evidence")
    if max(abs(f - b) for f, b in zip(fill, background)) < 64:
        reject("low_contrast_boundary_requires_manual_evidence")
    if result["rejection_reasons"]:
        return result
    background_components = _components([_near(p, background, 16) for p in pixels], width, height)
    ring_seed = (top - 3) * width + left
    connected_background = next((c for c in background_components if ring_seed in c), set())
    if not connected_background or _bbox(connected_background, width) != [0, 0, width, height]:
        reject("enclosed_surround_or_border_requires_manual_evidence")
        return result
    support_mask = [_near(p, fill, 24) or _coverage(p, fill, background) for p in pixels]
    support_components = _components(support_mask, width, height)
    plausible = _outer_components(support_components, width)
    if len(plausible) != 1 or not component.issubset(plausible[0]):
        reject("ambiguous_antialias_support")
        return result
    component = plausible[0]
    measured = _bbox(component, width)
    record(measured)
    if any(abs(a - b) > 2 for a, b in zip(local, measured)):
        reject("unstable_boundary: antialias support exceeds 2 px")
    left, top, right, bottom = measured
    if min(left, top, width - right, height - bottom) < 6:
        reject("insufficient_search_padding_or_clipped_support")
    if not result["badge_dimensions_within_tolerance"]:
        reject("badge_dimensions_outside_160x40_plus_or_minus_2_px")
    # A different-colored border must not turn an oversized badge into an
    # apparently compliant inner-fill box. Only background/faint AA is allowed.
    fringe = [
        pixels[y * width + x]
        for y in range(max(0, top - 2), min(height, bottom + 2))
        for x in range(max(0, left - 2), min(width, right + 2))
        if not (left <= x < right and top <= y < bottom)
    ]
    if any(not _near(p, background, 16) and not _coverage(p, background, fill) for p in fringe):
        reject("unsupported_border_or_touching_decoration")
    silhouette = _silhouette(component, width)
    box_area = (right - left) * (bottom - top)
    if len(silhouette) / box_area < 0.94:
        reject("irregular_badge_shape_or_touching_decoration")
    silhouette_image = Image.new("L", (width, height))
    silhouette_image.putdata([255 if i in silhouette else 0 for i in range(width * height)])
    interior = {i for i, value in enumerate(_pixel_data(silhouette_image.filter(ImageFilter.MinFilter(5)))) if value}
    ink_mask = [_near(p, ink, 24) or _coverage(p, ink, fill) for p in pixels]
    seed_area = interior | {
        y * width + x
        for y in range(top + 8, bottom - 8)
        for x in range(left + 8, right - 8)
    }
    ink_components = [c for c in _components(ink_mask, width, height) if c & seed_area]
    text = set().union(*ink_components) if ink_components else set()
    if not text:
        reject("no_text_ink_pixels")
    else:
        ink_box = _bbox(text, width, (x0, y0))
        result["text_ink_bbox_xyxy"] = ink_box
        result["text_ink_width"] = ink_box[2] - ink_box[0]
        result["text_ink_height"] = ink_box[3] - ink_box[1]
        result["text_ink_contained"] = text.issubset(interior)
        if not result["text_ink_contained"]:
            reject("text_ink_not_safely_contained")
    unknown = [i for i in silhouette if not support_mask[i] and not ink_mask[i] and not _coverage(pixels[i], fill, ink)]
    if unknown:
        reject("unsupported_interior_colors: gradient_texture_or_decoration_requires_manual_evidence")
    # Inspect fill safely away from both outline and glyph edges, not AA blends.
    solid_mask = Image.new("L", (width, height))
    solid_mask.putdata([255 if i in interior and not ink_mask[i] else 0 for i in range(len(pixels))])
    solid = [pixels[i] for i, value in enumerate(_pixel_data(solid_mask.filter(ImageFilter.MinFilter(5)))) if value]
    if not solid or any(max(p[c] for p in solid) - min(p[c] for p in solid) > 8 for c in range(3)):
        reject("nonuniform_fill_requires_manual_evidence")
    return _finish(result)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--roi", nargs=4, type=int, required=True, metavar=("X0", "Y0", "X1", "Y1"))
    parser.add_argument("--palette", choices=PALETTES, required=True)
    parser.add_argument("--output", type=Path, help="Optional JSON evidence file; stdout always contains the report.")
    args = parser.parse_args(argv)
    if args.output and (args.output.resolve() == args.image.resolve()
                        or (args.output.exists() and args.image.exists() and args.output.samefile(args.image))):
        parser.error("the evidence output must not overwrite the input image")
    result = measure_badge(args.image, roi=args.roi, palette=args.palette)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if result["raster_gate_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
