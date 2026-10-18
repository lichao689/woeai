"""English presentation of the existing, unchanged publication registry."""
import json
from html import escape
from pathlib import Path
from woeai.publications.homepage import render_home_progress, copy_home_progress_covers
from woeai.publications.taxonomy import RESEARCH_FAMILY_EN, RESEARCH_SUBDIRECTION_EN

SELECTED = (
    ("ref-zhao2026-BS", "Reusing CFD for urban wind assessment", "A precomputed database connects city-block simulation to rapid wind-field estimation."),
    ("ref-chen2024-JCP", "Better inflow for large eddy simulation", "Synthetic turbulence is examined through coherence, mass balance and pressure behaviour."),
    ("ref-tang2025-JBE", "Learning structural response from graphs", "A graph-based surrogate brings structural connectivity into response prediction."),
    ("ref-zhou2023-AE", "Comparing floaters over a service life", "Long-term dynamics and multiobjective optimisation reveal design trade-offs."),
    ("ref-he2026-OE-structural", "Designing a concrete floating platform", "Concept design connects dimensions, dynamic performance and overall strength."),
    ("ref-zheng2023-JRSE", "How direction changes floating wind response", "Combined wind–wave model tests examine a Y-shaped semi-submersible."),
)

def records(app):
    rows = json.loads((Path(app.confdir).parent / "data/publications.json").read_text())
    result = []
    for row in sorted(rows, key=lambda x: x["custom"]["order"]):
        custom = row["custom"]
        bib = custom["legacy_bibliography"]
        # Only public bibliographic fields enter page context; workflow evidence
        # and private source locators are deliberately excluded.
        result.append(dict(ref=custom["publication_ref"], title=bib["title"],
                           authors="; ".join(bib["creators"]), year=bib["year"],
                           journal=bib["publicationTitle"], doi=bib.get("doi", ""),
                           family=RESEARCH_FAMILY_EN[custom["research_family"]],
                           topic=RESEARCH_SUBDIRECTION_EN[custom["subdirection"]]))
    return result

def source_read(app, docname, source):
    if docname in ("index", "en/index"):
        app.env.note_dependency(str(Path(app.confdir).parent / "data/home-progress.json"))
        app.env.note_dependency(str(Path(app.confdir).parent / "data/home-progress-selection.json"))
        root = Path(app.confdir).resolve().parents[1]
        for cover in (root / "wechat/assets/public-safe").glob("*/cover.png"):
            app.env.note_dependency(str(cover))
    if docname == "index":
        app.env.note_dependency(str(Path(app.confdir).parent / "data/publications.json"))
        return
    if not docname.startswith("en/"):
        return
    app.env.note_dependency(str(Path(app.confdir).parent / "data/publications.json"))
    rows = records(app)
    if docname == "en/Publications":
        parts = []
        for row in rows:
            parts.append(f".. _en-{row['ref']}:\n\n**{row['title']}**\n\n{row['authors']}. {row['journal']} ({row['year']}).\n\n{row['family']} / {row['topic']}. " +
                         (f"`DOI <https://doi.org/{row['doi']}>`__" if row['doi'] else "") + "\n")
        source[0] = source[0].replace(".. ENGLISH PUBLICATIONS", "\n".join(parts))
    elif docname.startswith("en/highlights/"):
        row = next(x for x in rows if x["ref"] == docname.rsplit("/", 1)[1])
        source[0] += (f"\nSource paper\n------------\n\n{row['authors']}. **{row['title']}**. {row['journal']} ({row['year']}).\n\n"
                      f"`Read the paper (DOI) <https://doi.org/{row['doi']}>`__ · "
                      f":doc:`Chinese reading notes </paper-notes/{row['ref']}>` · "
                      f":ref:`Publication record <en-{row['ref']}>`\n")

def page_context(app, pagename, templatename, context, doctree):
    english = pagename.startswith("en/")
    pairs = {"index":"en/index", "Research":"en/Research", "Publications":"en/Publications", "Recruitment":"en/JoinUs", "search":"en/Search"}
    pairs.update({value:key for key,value in list(pairs.items())})
    paired = pagename in pairs
    context.update(is_english=english, site_home="en/index" if english else "index",
                   site_search="en/Search" if english else "search",
                   language="en" if english else "zh-CN",
                   language_target=pairs.get(pagename, "index" if english else "en/index"),
                   language_label=("中文" if paired else "中文首页") if english else ("EN" if paired else "EN home"))
    if english:
        by_ref = {x["ref"]:x for x in records(app)}
        context["english_highlights"] = [dict(by_ref[ref], heading=heading, deck=deck) for ref,heading,deck in SELECTED]
        if pagename == "en/index":
            context["recent_progress"] = render_home_progress(Path(app.confdir).resolve().parents[1], english=True)
        description = "WOEAI Lab studies structural wind engineering, floating offshore wind and AI-supported engineering methods. Laboratory lead: Chao Li."
        context["metatags"] = context.get("metatags", "") + f'<meta name="description" content="{escape(description, quote=True)}">'
    if pagename == "en/index":
        return "en-home.html"
    if pagename == "en/Search":
        return "en-search.html"

def write_home_covers(app, exception):
    if exception is None and app.builder.format == "html":
        copy_home_progress_covers(Path(app.confdir).resolve().parents[1], Path(app.outdir))


def setup(app):
    app.connect("source-read", source_read)
    app.connect("build-finished", write_home_covers)
    app.connect("html-page-context", page_context)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
