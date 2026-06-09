#!/usr/bin/env python3
"""Render a WOEAI WeChat Markdown article to a copy-ready local HTML page.

This is intentionally a small WOEAI-specific renderer. It covers the article
shape used in `wechat/articles/draft-public-safe/`: headings, paragraphs,
lists, images with following captions, bold text, inline math, and display
math. The output is a local HTML file with inline styles, so copying from the
browser into the WeChat Official Account editor has a better chance of keeping
the layout.
"""

from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
from pathlib import Path


WECHAT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTICLE = WECHAT_ROOT / "articles/draft-public-safe/ref-zhao2026-BS.md"
DEFAULT_OUTPUT = WECHAT_ROOT / ".local/exports/ref-zhao2026-BS.academic-clean.html"


STYLES = {
    "article": (
        "max-width:677px;margin:0 auto;padding:24px 18px 44px;"
        "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
        "font-size:16px;line-height:1.86;color:#1f2933;background:#ffffff;"
    ),
    "h1": (
        "margin:0 0 18px;padding:0 0 16px;border-bottom:2px solid #23486f;"
        "font-size:25px;line-height:1.36;color:#0f2d52;font-weight:700;"
    ),
    "h2": (
        "margin:34px 0 15px;padding:0 0 0 12px;border-left:4px solid #2f6f9f;"
        "font-size:20px;line-height:1.38;color:#153a63;font-weight:700;"
    ),
    "h3": (
        "margin:25px 0 12px;font-size:17px;line-height:1.45;"
        "color:#24364b;font-weight:700;"
    ),
    "p": "margin:0 0 16px;",
    "ul": "margin:0 0 18px;padding-left:20px;",
    "ol": "margin:0 0 18px;padding-left:22px;",
    "li": "margin:0 0 8px;",
    "img": "display:block;width:100%;height:auto;margin:22px auto 8px;",
    "caption": (
        "margin:0 0 24px;padding-left:10px;border-left:3px solid #c3d6e4;"
        "font-size:13px;line-height:1.68;color:#59636f;"
    ),
    "formula": (
        "margin:18px 0;padding:16px;text-align:center;overflow-x:auto;"
        "border:1px solid #d4dee8;background:#f7fafc;color:#18344f;"
        "font-family:'Times New Roman',Georgia,serif;font-size:18px;line-height:1.5;"
    ),
    "button": (
        "position:sticky;top:0;z-index:10;display:flex;gap:10px;align-items:center;"
        "justify-content:center;padding:12px;background:#eef3f7;border-bottom:1px solid #d7dce2;"
        "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
    ),
}


def styled(tag: str, content: str, style_key: str | None = None, **attrs: str) -> str:
    style = STYLES[style_key or tag]
    attr_parts = [f'style="{html.escape(style, quote=True)}"']
    for key, value in attrs.items():
        attr_parts.append(f'{key}="{html.escape(value, quote=True)}"')
    return f"<{tag} {' '.join(attr_parts)}>{content}</{tag}>"


def inline_image_src(markdown_file: Path, raw_src: str, embed_images: bool) -> str:
    image_path = (markdown_file.parent / raw_src).resolve()
    if not embed_images:
        return image_path.as_uri()
    mime = mimetypes.guess_type(image_path.name)[0] or "image/png"
    data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def render_inline(text: str) -> str:
    placeholders: list[str] = []

    def store(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def math_repl(match: re.Match[str]) -> str:
        return store(render_inline_math(match.group(1)))

    text = re.sub(r"\$([^$\n]+)\$", math_repl, text)
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)

    for idx, value in enumerate(placeholders):
        escaped = escaped.replace(f"\u0000{idx}\u0000", value)
    return escaped


def render_inline_math(src: str) -> str:
    src = src.strip()
    src = src.replace(r"\,", " ")
    src = src.replace(r"\times", "×")
    src = src.replace(r"\circ", "°")
    src = src.replace(r"\%", "%")
    src = re.sub(r"\\mathrm\{([^}]+)\}", lambda m: f'<span style="font-style:normal;">{html.escape(m.group(1))}</span>', src)
    src = re.sub(r"([A-Za-z])_\{([^}]+)\}", lambda m: f'<em>{html.escape(m.group(1))}</em><sub>{render_inline_math(m.group(2))}</sub>', src)
    src = re.sub(r"([A-Za-z])_([A-Za-z0-9]+)", lambda m: f'<em>{html.escape(m.group(1))}</em><sub>{html.escape(m.group(2))}</sub>', src)
    src = re.sub(r"([A-Za-z])\^\{([^}]+)\}", lambda m: f'<em>{html.escape(m.group(1))}</em><sup>{render_inline_math(m.group(2))}</sup>', src)
    src = re.sub(r"([A-Za-z])\^([A-Za-z0-9]+)", lambda m: f'<em>{html.escape(m.group(1))}</em><sup>{html.escape(m.group(2))}</sup>', src)
    src = re.sub(r"\b([A-Za-z])\b", lambda m: f"<em>{m.group(1)}</em>", src)
    return f'<span style="font-family:\'Times New Roman\',Georgia,serif;">{src}</span>'


def render_display_math(src: str) -> str:
    compact = " ".join(line.strip() for line in src.strip().splitlines())
    known = r"E = \frac{K_{\mathrm{CFD}} - K_{\mathrm{m}}}{K_{\mathrm{m}}} \times 100\%"
    if compact == known:
        return styled(
            "div",
            (
                '<span style="font-style:italic;">E</span>'
                '<span style="padding:0 8px;">=</span>'
                '<span style="display:inline-block;vertical-align:middle;text-align:center;">'
                '<span style="display:block;padding:0 8px;border-bottom:1px solid #18344f;">'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">CFD</sub>'
                '<span style="padding:0 6px;">−</span>'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">m</sub>'
                '</span>'
                '<span style="display:block;padding:3px 8px 0;">'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">m</sub>'
                '</span>'
                '</span>'
                '<span style="padding:0 8px;">×</span>100%'
            ),
            "formula",
        )
    return styled("div", render_inline_math(compact), "formula")


def flush_paragraph(paragraph: list[str], output: list[str]) -> None:
    if paragraph:
        output.append(styled("p", render_inline(" ".join(paragraph)), "p"))
        paragraph.clear()


def flush_list(list_items: list[str], output: list[str], ordered: bool) -> None:
    if list_items:
        tag = "ol" if ordered else "ul"
        body = "".join(styled("li", render_inline(item), "li") for item in list_items)
        output.append(styled(tag, body, tag))
        list_items.clear()


def render_markdown(markdown_file: Path, embed_images: bool) -> str:
    lines = markdown_file.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    ordered = False
    in_math = False
    math_lines: list[str] = []
    previous_was_image = False

    for line in lines:
        stripped = line.strip()

        if in_math:
            if stripped == "$$":
                output.append(render_display_math("\n".join(math_lines)))
                math_lines.clear()
                in_math = False
            else:
                math_lines.append(line)
            continue

        if stripped == "$$":
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            in_math = True
            previous_was_image = False
            continue

        if not stripped:
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            previous_was_image = False
            continue

        image_match = re.match(r"!\[(.*?)\]\((.*?)\)", stripped)
        if image_match:
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            alt, src = image_match.groups()
            output.append(
                f'<img src="{html.escape(inline_image_src(markdown_file, src, embed_images), quote=True)}" '
                f'alt="{html.escape(alt, quote=True)}" style="{html.escape(STYLES["img"], quote=True)}">'
            )
            previous_was_image = True
            continue

        if stripped.startswith("# "):
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            output.append(styled("h1", render_inline(stripped[2:]), "h1"))
            previous_was_image = False
            continue

        if stripped.startswith("## "):
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            output.append(styled("h2", render_inline(stripped[3:]), "h2"))
            previous_was_image = False
            continue

        if stripped.startswith("### "):
            flush_paragraph(paragraph, output)
            flush_list(list_items, output, ordered)
            output.append(styled("h3", render_inline(stripped[4:]), "h3"))
            previous_was_image = False
            continue

        unordered_match = re.match(r"[-*]\s+(.*)", stripped)
        ordered_match = re.match(r"\d+\.\s+(.*)", stripped)
        if unordered_match or ordered_match:
            flush_paragraph(paragraph, output)
            this_ordered = bool(ordered_match)
            if list_items and ordered != this_ordered:
                flush_list(list_items, output, ordered)
            ordered = this_ordered
            list_items.append((ordered_match or unordered_match).group(1))
            previous_was_image = False
            continue

        flush_list(list_items, output, ordered)
        if previous_was_image and re.match(r"^图\s*\d+", stripped):
            output.append(styled("p", render_inline(stripped), "caption"))
            previous_was_image = False
        else:
            paragraph.append(stripped)
            previous_was_image = False

    flush_paragraph(paragraph, output)
    flush_list(list_items, output, ordered)
    return "\n".join(output)


def render_page(article_html: str, title: str) -> str:
    button_style = STYLES["button"]
    button_inner_style = (
        "border:0;background:#23486f;color:#fff;padding:8px 14px;"
        "font-size:14px;border-radius:4px;cursor:pointer;"
    )
    note_style = "font-size:13px;color:#4b5563;"
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
</head>
<body style="margin:0;background:#eef1f4;">
  <div style="{html.escape(button_style, quote=True)}">
    <button id="copy" style="{html.escape(button_inner_style, quote=True)}">复制公众号正文</button>
    <span id="status" style="{html.escape(note_style, quote=True)}">复制后粘贴到公众号编辑器。若图片没带过去，再手动上传图片。</span>
  </div>
  <main id="article" style="{html.escape(STYLES["article"], quote=True)}">
{article_html}
  </main>
  <script>
    const button = document.getElementById('copy');
    const status = document.getElementById('status');
    button.addEventListener('click', async () => {{
      const article = document.getElementById('article');
      const html = article.outerHTML;
      const text = article.innerText;
      try {{
        if (navigator.clipboard && window.ClipboardItem) {{
          await navigator.clipboard.write([
            new ClipboardItem({{
              'text/html': new Blob([html], {{type: 'text/html'}}),
              'text/plain': new Blob([text], {{type: 'text/plain'}})
            }})
          ]);
        }} else {{
          const range = document.createRange();
          range.selectNode(article);
          const selection = window.getSelection();
          selection.removeAllRanges();
          selection.addRange(range);
          document.execCommand('copy');
          selection.removeAllRanges();
        }}
        status.textContent = '已复制。现在可以去公众号编辑器粘贴。';
      }} catch (error) {{
        const range = document.createRange();
        range.selectNode(article);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        status.textContent = '浏览器限制了自动复制：正文已选中，请按 Command+C。';
      }}
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("article", nargs="?", type=Path, default=DEFAULT_ARTICLE)
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-embed-images", action="store_true")
    args = parser.parse_args()

    article = args.article.resolve()
    output = args.output.resolve()
    article_html = render_markdown(article, embed_images=not args.no_embed_images)
    first_line = article.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_page(article_html, first_line), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
