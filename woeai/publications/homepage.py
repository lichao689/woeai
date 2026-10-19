"""Registry-backed recent papers for the two language versions of the homepage."""

import json
import hashlib
import re
import unicodedata
from html import escape
from pathlib import Path

from PIL import Image

from woeai.publications.registry import load_registry, wechat_content_reviewed
from woeai.publications.taxonomy import RESEARCH_FAMILY_EN, RESEARCH_FAMILY_ORDER
from woeai.publications.textutils import parse_date
from woeai.wechat.review import find_review_cover


def publication_date(record):
    """Use CSL dates, enriching year-only dates from the public bibliography."""
    issued = record.get("issued", {})
    parts = issued.get("date-parts", [[]])[0]
    date = tuple((parts + [0, 0, 0])[:3]) if parts else parse_date(issued.get("literal"))
    legacy = parse_date(record["custom"]["legacy_bibliography"].get("date"))
    if date[0] and legacy[0] == date[0] and not date[1]:
        return legacy
    return date if date[0] else legacy


def recent_publications(records, root: Path):
    """Filter explicitly selected, produced introductions before grouping and ranking."""
    selection = json.loads((root / 'docs/data/home-progress-selection.json').read_text())
    selected = set(selection['publication_refs'])
    eligible = [row for row in records
                if row['custom']['publication_ref'] in selected
                and row['custom'].get('content_production') == 'included'
                and wechat_content_reviewed(row, root)]
    groups = []
    for family in RESEARCH_FAMILY_ORDER:
        rows = [row for row in eligible if row['custom']['research_family'] == family]
        rows.sort(key=lambda row: (
            tuple(-part for part in publication_date(row)),
            row['custom']['order'], row['custom']['publication_ref'],
        ))
        groups.append((family, rows[:3]))
    return groups


def _required_card_text(value, ref, field):
    """Reject empty or visibly unfinished copy before any card is emitted."""
    if not isinstance(value, str):
        raise ValueError(f"home-progress.json: {ref} {field} must be nonempty text")
    normalized = unicodedata.normalize("NFKC", value)
    normalized = re.sub(r"[\u200b-\u200f\u202a-\u202e\u2060\ufeff]", "", normalized).strip()
    placeholder = re.search(
        r"\b(?:todo|tbd|placeholder)\b|to be (?:added|confirmed|completed)"
        r"|待(?:补(?:充)?|完善|确认|填写|定)|占位|暂无", normalized, re.IGNORECASE)
    placeholder = placeholder or re.fullmatch(
        r"n/?a|null|none|pending(?: review| confirmation)?|coming soon", normalized, re.IGNORECASE)
    if not any(character.isalnum() for character in normalized) or placeholder:
        raise ValueError(f"home-progress.json: {ref} {field} is empty or placeholder text")


def _card_annotation(root, row, annotations):
    """Both languages must cite actual sections of this reviewed introduction."""
    ref = row["custom"]["publication_ref"]
    entry = annotations.get(ref)
    if not isinstance(entry, dict):
        raise ValueError(f"home-progress.json: {ref} annotation is required")
    for language in ("zh", "en"):
        copy = entry.get(language)
        if not isinstance(copy, dict):
            raise ValueError(f"home-progress.json: {ref} {language} copy is required")
        for field in ("heading", "problem", "contribution"):
            _required_card_text(copy.get(field), ref, f"{language}.{field}")
    evidence = entry.get("evidence")
    if not isinstance(evidence, dict):
        raise ValueError(f"home-progress.json: {ref} evidence is required")
    relative = f"wechat/articles/draft-public-safe/{ref}.md"
    source = root / relative
    if (evidence.get("path") != relative
            or row["custom"]["wechat"]["path"] != relative
            or source.resolve() != root.resolve() / relative
            or not source.is_file()):
        raise ValueError(f"home-progress.json: {ref} evidence.path must name its reviewed public introduction")
    sections = dict(re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", source.read_text(), re.MULTILINE | re.DOTALL))
    for field in ("problem", "contribution"):
        locators = evidence.get(field)
        if (not isinstance(locators, list) or not locators
                or any(not isinstance(locator, str) or not sections.get(locator, "").strip()
                       for locator in locators)):
            raise ValueError(f"home-progress.json: {ref} evidence.{field} must cite nonempty source sections")
    return entry


def render_home_progress(root: Path, *, english=False):
    """Render the shared card markup, projecting only public display fields."""
    prefix = "../" if english else ""
    annotations = json.loads((root / "docs/data/home-progress.json").read_text())
    if not isinstance(annotations, dict):
        raise ValueError("home-progress.json must contain an object keyed by publication_ref")
    parts = []
    for family, rows in recent_publications(load_registry(root), root):
        label = RESEARCH_FAMILY_EN[family] if english else family
        parts.append(f'<div class="progress-family" data-research-family="{escape(family)}">'
                     f'<h3 class="progress-family-title">{escape(label)}</h3><div class="work-grid">')
        for row in rows:
            custom = row["custom"]
            ref = custom["publication_ref"]
            bib = custom["legacy_bibliography"]
            annotation = _card_annotation(root, row, annotations)
            copy = annotation["en" if english else "zh"]
            heading = copy["heading"]
            date = "-".join(f"{part:02d}" for part in publication_date(row) if part)
            record_url = f'Publications.html#{"en-" if english else ""}{ref.lower()}'
            parts.append(f'<article class="work-card" data-publication-ref="{escape(ref)}" data-publication-date="{date}">')
            image = f"home/progress-{ref}.webp"
            cover = find_review_cover(root / custom["wechat"]["review_path"], root=root)
            if cover is not None:
                image += "?v=" + hashlib.sha256(cover.read_bytes()).hexdigest()[:12]
                caption = "AI-generated reading-note cover · not research data" if english else "AI 生成的论文解读封面 · 非研究数据"
                parts.append(f'<figure><img src="{prefix}_static/{image}" alt="{escape(heading)}" width="900" height="383" loading="lazy" decoding="async">'
                             f'<figcaption>{escape(caption)}</figcaption></figure>')
            parts.append(f'<div class="work-body">'
                         f'<p class="work-tag">{escape(date)} · {escape(label)}</p><h4>{escape(heading)}</h4>')
            problem_label, contribution_label = ("Problem", "Contribution") if english else ("问题", "贡献")
            parts.append(f'<p><strong>{problem_label}</strong> {escape(copy["problem"])}</p>'
                         f'<p><strong>{contribution_label}</strong> {escape(copy["contribution"])}</p>')
            parts.append(f'<div class="paper-source"><p class="work-venue">{escape(str(bib["year"]))} · {escape(bib["publicationTitle"])}</p>'
                         f'<p class="paper-citation">{escape(bib["rendered"])}</p></div>'
                         f'<div class="work-links"><a href="{record_url}">{"Publication record" if english else "论文记录"} →</a>')
            note = f"paper-notes/{ref}"
            if (root / "docs/source" / (note + ".rst")).is_file():
                highlight = f"en/highlights/{ref}"
                if english and (root / "docs/source" / (highlight + ".rst")).is_file():
                    target, link_label = f"highlights/{ref}.html", "Read highlight"
                else:
                    target, link_label = f"{prefix}{note}.html", "Chinese reading notes" if english else "论文精解"
                parts.append(f'<a href="{target}">{link_label} →</a>')
            doi = bib.get("doi")
            if doi:
                parts.append(f'<a href="https://doi.org/{escape(doi, quote=True)}">{"Paper" if english else "原论文"} ↗</a>')
            parts.append('</div></div></article>')
        parts.append('</div></div>')
    return "\n".join(parts)


# The six homepage cards dominate the first-screen payload. The review covers
# ship as 900x383 PNG (~360–480 KB each, 2.5 MB for the section); re-encoding to
# WebP cuts that to ~30–60 KB. The edge serving this site is 160 ms away from
# mainland China, so removing two megabytes off the critical path is worth the
# conversion step.
COVER_WEBP_QUALITY = 85


def _write_webp(source: Path, target: Path) -> None:
    """Encode a review cover as WebP, keeping its dimensions and alpha."""
    with Image.open(source) as handle:
        if handle.mode not in ("RGB", "RGBA"):
            handle = handle.convert("RGB")
        handle.save(target, "WEBP", quality=COVER_WEBP_QUALITY, method=6)


def copy_home_progress_covers(root: Path, outdir: Path):
    """Generate homepage derivatives directly in Sphinx output, never in source."""
    destination = outdir / "_static/home"
    destination.mkdir(parents=True, exist_ok=True)
    current = set()
    for _, rows in recent_publications(load_registry(root), root):
        for row in rows:
            custom = row["custom"]
            cover = find_review_cover(root / custom["wechat"]["review_path"], root=root)
            if cover is None:
                continue
            name = f"progress-{custom['publication_ref']}.webp"
            _write_webp(cover, destination / name)
            current.add(name)
    # Remove stale derivatives of both the old and the current extension.
    for path in list(destination.glob("progress-*.webp")) + list(destination.glob("progress-*.png")):
        if path.name not in current:
            path.unlink()
