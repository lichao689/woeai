#!/usr/bin/env python3
"""Create a local WeChat cover preview page with crop-safety checks.

The preview is public-safe and does not contact WeChat. It approximates common
WeChat display crops so an editor can catch obvious cover problems before a
backend mobile preview.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


WECHAT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WECHAT_ROOT.parent
DEFAULT_OUTPUT_DIR = WECHAT_ROOT / ".local/cover-previews"


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def image_dimensions(path: Path) -> tuple[int | None, int | None]:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    if data.startswith(b"\xff\xd8"):
        idx = 2
        while idx + 9 < len(data):
            if data[idx] != 0xFF:
                idx += 1
                continue
            marker = data[idx + 1]
            idx += 2
            if marker in {0xD8, 0xD9}:
                continue
            length = int.from_bytes(data[idx : idx + 2], "big")
            if 0xC0 <= marker <= 0xC3 and idx + 7 < len(data):
                height = int.from_bytes(data[idx + 3 : idx + 5], "big")
                width = int.from_bytes(data[idx + 5 : idx + 7], "big")
                return width, height
            idx += length
    return None, None


def file_url(path: Path) -> str:
    return path.resolve().as_uri()


def cover_summary(path: Path, target_width: int, target_height: int, max_bytes: int) -> dict[str, Any]:
    width, height = image_dimensions(path)
    ratio = (width / height) if width and height else None
    target_ratio = target_width / target_height
    ratio_delta = abs(ratio - target_ratio) if ratio else None
    size = path.stat().st_size if path.exists() else 0
    return {
        "path": repo_relative(path),
        "exists": path.exists(),
        "bytes": size,
        "width": width,
        "height": height,
        "ratio": round(ratio, 4) if ratio else None,
        "target_ratio": round(target_ratio, 4),
        "ratio_delta": round(ratio_delta, 4) if ratio_delta is not None else None,
        "target_ratio_match": bool(ratio_delta is not None and ratio_delta <= 0.02),
        "file_size_ok": size <= max_bytes,
    }


def render_card(summary: dict[str, Any]) -> str:
    path = Path(REPO_ROOT / summary["path"]).resolve()
    src = html.escape(file_url(path), quote=True)
    title = html.escape(summary["path"])
    metadata = "".join(
        f"<tr><th>{html.escape(str(key))}</th><td>{html.escape(str(value))}</td></tr>"
        for key, value in summary.items()
        if key not in {"path", "exists"}
    )
    return f"""
<section class="card">
  <h2>{title}</h2>
  <table>{metadata}</table>
  <div class="grid">
    <div>
      <h3>Full Cover 2.35:1</h3>
      <div class="frame wide">
        <img src="{src}" alt="{title}">
        <div class="safe"></div>
      </div>
    </div>
    <div>
      <h3>Center Square Crop</h3>
      <div class="frame square">
        <img src="{src}" alt="{title}">
      </div>
    </div>
    <div>
      <h3>5:4 Share Crop</h3>
      <div class="frame share">
        <img src="{src}" alt="{title}">
      </div>
    </div>
  </div>
  <p class="note">Dashed box marks an approximate center safe area. This local
  preview is a first-pass check; final approval still requires WeChat backend
  mobile preview.</p>
</section>
"""


def render_page(summaries: list[dict[str, Any]]) -> str:
    cards = "\n".join(render_card(summary) for summary in summaries)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>WOEAI WeChat Cover Preview</title>
  <style>
    body {{
      margin: 0;
      background: #f3f5f7;
      color: #18212f;
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 28px 18px 48px;
    }}
    h1 {{
      margin: 0 0 20px;
      font-size: 24px;
      line-height: 1.3;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 18px;
      line-height: 1.45;
    }}
    h3 {{
      margin: 0 0 8px;
      font-size: 14px;
      color: #42526b;
    }}
    .card {{
      margin: 0 0 24px;
      padding: 18px;
      background: #fff;
      border: 1px solid #d8dee8;
      border-radius: 8px;
    }}
    table {{
      width: 100%;
      margin: 0 0 18px;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      padding: 7px 8px;
      border-bottom: 1px solid #e5e9f0;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      width: 160px;
      color: #667085;
      font-weight: 600;
    }}
    .grid {{
      display: grid;
      grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1.25fr);
      gap: 16px;
      align-items: start;
    }}
    .frame {{
      position: relative;
      overflow: hidden;
      background: #dfe5ec;
      border: 1px solid #b6c2d0;
    }}
    .wide {{ aspect-ratio: 900 / 383; }}
    .square {{ aspect-ratio: 1 / 1; }}
    .share {{ aspect-ratio: 5 / 4; }}
    .frame img {{
      width: 100%;
      height: 100%;
      display: block;
      object-fit: cover;
      object-position: center center;
    }}
    .safe {{
      position: absolute;
      left: 16.666%;
      top: 0;
      width: 66.666%;
      height: 100%;
      border-left: 2px dashed rgba(255, 255, 255, 0.9);
      border-right: 2px dashed rgba(255, 255, 255, 0.9);
      box-shadow: inset 0 0 0 1px rgba(15, 45, 82, 0.65);
      pointer-events: none;
    }}
    .note {{
      margin: 12px 0 0;
      color: #596579;
      font-size: 13px;
      line-height: 1.6;
    }}
    @media (max-width: 780px) {{
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <main>
    <h1>WOEAI WeChat Cover Preview</h1>
    {cards}
  </main>
</body>
</html>
"""


def default_output(images: list[Path]) -> Path:
    if len(images) == 1:
        return DEFAULT_OUTPUT_DIR / f"{images[0].stem}.cover-preview.html"
    return DEFAULT_OUTPUT_DIR / "cover-preview.html"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--target-width", type=int, default=900)
    parser.add_argument("--target-height", type=int, default=383)
    parser.add_argument("--max-bytes", type=int, default=5 * 1024 * 1024)
    args = parser.parse_args()

    images = [image.resolve() for image in args.images]
    for image in images:
        if not image.exists():
            raise FileNotFoundError(image)
    output = (args.output or default_output(images)).resolve()
    summaries = [cover_summary(image, args.target_width, args.target_height, args.max_bytes) for image in images]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_page(summaries), encoding="utf-8")
    print(json.dumps({"ok": True, "output": repo_relative(output), "covers": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
