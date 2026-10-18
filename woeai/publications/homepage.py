"""Registry-backed recent papers for the two language versions of the homepage."""

import json
from html import escape
from pathlib import Path

from woeai.publications.registry import load_registry
from woeai.publications.taxonomy import RESEARCH_FAMILY_EN, RESEARCH_FAMILY_ORDER
from woeai.publications.textutils import parse_date


def publication_date(record):
    """Use CSL dates, enriching year-only dates from the public bibliography."""
    issued = record.get("issued", {})
    parts = issued.get("date-parts", [[]])[0]
    date = tuple((parts + [0, 0, 0])[:3]) if parts else parse_date(issued.get("literal"))
    legacy = parse_date(record["custom"]["legacy_bibliography"].get("date"))
    if date[0] and legacy[0] == date[0] and not date[1]:
        return legacy
    return date if date[0] else legacy


def recent_publications(records):
    """Return three latest public papers per family, including uncatalogued notes."""
    ordered = sorted(records, key=lambda row: (
        tuple(-part for part in publication_date(row)),
        row["custom"]["order"], row["custom"]["publication_ref"],
    ))
    return [(family, [row for row in ordered if row["custom"]["research_family"] == family][:3])
            for family in RESEARCH_FAMILY_ORDER]


def render_home_progress(root: Path, *, english=False):
    """Render the shared card markup, projecting only public display fields."""
    prefix = "../" if english else ""
    annotations = json.loads((root / "docs/data/home-progress.json").read_text())
    parts = []
    for family, rows in recent_publications(load_registry(root)):
        label = RESEARCH_FAMILY_EN[family] if english else family
        parts.append(f'<div class="progress-family" data-research-family="{escape(family)}">'
                     f'<h3 class="progress-family-title">{escape(label)}</h3><div class="work-grid">')
        for row in rows:
            custom = row["custom"]
            ref = custom["publication_ref"]
            bib = custom["legacy_bibliography"]
            copy = annotations.get(ref, {}).get("en" if english else "zh", {})
            heading = copy.get("heading", bib["title"])
            date = "-".join(f"{part:02d}" for part in publication_date(row) if part)
            record_url = f'Publications.html#{"en-" if english else ""}{ref.lower()}'
            parts.append(f'<article class="work-card" data-publication-ref="{escape(ref)}" data-publication-date="{date}">')
            image = f"home/progress-{ref}.png"
            if (root / "docs/_static" / image).is_file():
                caption = "AI-generated reading-note cover · not research data" if english else "AI 生成的论文解读封面 · 非研究数据"
                parts.append(f'<figure><img src="{prefix}_static/{image}" alt="{escape(heading)}" width="900" height="383" loading="lazy" decoding="async">'
                             f'<figcaption>{escape(caption)}</figcaption></figure>')
            parts.append(f'<div class="work-body">'
                         f'<p class="work-tag">{escape(date)} · {escape(label)}</p><h4>{escape(heading)}</h4>')
            if copy:
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
