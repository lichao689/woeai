#!/usr/bin/env python3
"""Add deterministic Chinese text overlay to a WOEAI WeChat cover image.

The script is intentionally local-only and does not contact any service. It
requires Pillow for raster editing. When Pillow is unavailable, it exits with a
JSON error so agents can fall back to image-gen direct-text candidates or a
runtime that includes Pillow.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


LAST_JSON_OUTPUT = ""
REPO_ROOT = Path.cwd().resolve()


def emit(payload: dict[str, Any]) -> None:
    global LAST_JSON_OUTPUT
    LAST_JSON_OUTPUT = json.dumps(payload, ensure_ascii=False, indent=2)
    print(LAST_JSON_OUTPUT)


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def load_pillow() -> tuple[Any, Any, Any] | None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ModuleNotFoundError:
        return None
    return Image, ImageDraw, ImageFont


def candidate_fonts() -> list[Path]:
    names = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/Library/Fonts/NotoSansCJK-Regular.ttc",
    ]
    return [Path(name) for name in names if Path(name).exists()]


def load_font(ImageFont: Any, size: int) -> Any:
    for font_path in candidate_fonts():
        try:
            return ImageFont.truetype(str(font_path), size=size)
        except Exception:
            continue
    raise RuntimeError("No usable Chinese font found for cover text overlay")


def fit_font(Image: Any, ImageDraw: Any, ImageFont: Any, text: str, max_width: int, start_size: int, min_size: int) -> Any:
    for size in range(start_size, min_size - 1, -2):
        font = load_font(ImageFont, size)
        bbox = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            return font
    return load_font(ImageFont, min_size)


def draw_overlay(args: argparse.Namespace) -> dict[str, Any]:
    pillow = load_pillow()
    if pillow is None:
        return {
            "ok": False,
            "stage": "dependency_check",
            "message": "Pillow is required for deterministic cover text overlay. Install Pillow or use an image-gen direct-text candidate.",
        }

    Image, ImageDraw, ImageFont = pillow
    image = Image.open(args.input).convert("RGB")
    image = image.resize((args.target_width, args.target_height))
    draw = ImageDraw.Draw(image, "RGBA")

    margin = int(args.target_width * 0.07)
    panel_width = int(args.target_width * 0.46)
    panel_height = int(args.target_height * 0.66)
    panel_x = margin
    panel_y = int((args.target_height - panel_height) / 2)
    draw.rounded_rectangle(
        [panel_x, panel_y, panel_x + panel_width, panel_y + panel_height],
        radius=18,
        fill=(8, 31, 48, 178),
    )

    tag_font = fit_font(Image, ImageDraw, ImageFont, args.category, panel_width - 44, 32, 20)
    hook_font = fit_font(Image, ImageDraw, ImageFont, args.hook, panel_width - 44, 48, 28)
    subtitle_font = fit_font(Image, ImageDraw, ImageFont, args.subtitle, panel_width - 44, 28, 18) if args.subtitle else None

    x = panel_x + 24
    y = panel_y + 30
    draw.text((x, y), args.category, font=tag_font, fill=(152, 221, 224, 255))
    y += 54
    draw.text((x, y), args.hook, font=hook_font, fill=(255, 255, 255, 255))
    if args.subtitle and subtitle_font is not None:
        y += 68
        draw.text((x, y), args.subtitle, font=subtitle_font, fill=(220, 235, 244, 235))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    return {
        "ok": True,
        "stage": "cover_text_overlay",
        "input": repo_relative(args.input),
        "output": repo_relative(args.output),
        "category": args.category,
        "hook": args.hook,
        "subtitle": args.subtitle,
        "width": args.target_width,
        "height": args.target_height,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--category", required=True)
    parser.add_argument("--hook", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--target-width", type=int, default=900)
    parser.add_argument("--target-height", type=int, default=383)
    args = parser.parse_args(argv)

    try:
        payload = draw_overlay(args)
    except Exception as exc:
        payload = {
            "ok": False,
            "stage": "cover_text_overlay",
            "error_type": type(exc).__name__,
            "message": str(exc),
        }
    emit(payload)
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
