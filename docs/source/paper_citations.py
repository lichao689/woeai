"""Always project complete, checked citations into both kinds of reading page."""
from pathlib import Path
import re

from docutils import nodes
from sphinx.errors import SphinxError

from woeai.publications.citations import reading_citations, check_built_citations

CITATION_TITLES = {"完整引用", "完整论文引用", "原文出处", "Source paper", "Full citation"}


def _root(app):
    return Path(app.confdir).resolve().parents[1]


def validate_citation_inputs(app):
    pages = reading_citations(_root(app))
    app._paper_citations = {page["docname"]: page for page in pages}


def track_registry(app, docname, source):
    if docname.startswith(("paper-notes/", "en/highlights/")):
        app.env.note_dependency(str(_root(app) / "docs/data/publications.json"))


def _citation_paragraph(text):
    paragraph = nodes.paragraph(classes=["paper-full-citation"])
    cursor = 0
    for match in re.finditer(r"https://doi\.org/[^\s]+", text):
        url = match.group().rstrip(".")
        paragraph += nodes.Text(text[cursor:match.start()])
        paragraph += nodes.reference("", url, refuri=url)
        cursor = match.start() + len(url)
    paragraph += nodes.Text(text[cursor:])
    return paragraph


def project_citation(app, doctree, docname):
    page = app._paper_citations.get(docname)
    if page is None:
        return
    sections = [section for section in doctree.findall(nodes.section)
                if section.children and isinstance(section[0], nodes.title)
                and section[0].astext() in CITATION_TITLES]
    if len(sections) > 1:
        raise SphinxError(f"{docname}: multiple complete-citation sections")
    english = docname.startswith("en/")
    if sections:
        section = sections[0]
        if any(not isinstance(child, (nodes.title, nodes.paragraph, nodes.target))
               for child in section.children):
            raise SphinxError(f"{docname}: unexpected content inside citation section")
        del section.children[1:]
    else:
        section = nodes.section(ids=["paper-full-citation"])
        section += nodes.title("", "Source paper" if english else "完整引用")
        doctree += section
    section["classes"].append("paper-citation-section")
    section += _citation_paragraph(page["text"])
    link = nodes.paragraph()
    destination = "en/Publications" if english else "Publications"
    anchor = ("en-" if english else "") + page["ref"].lower()
    uri = app.builder.get_relative_uri(docname, destination) + "#" + anchor
    link += nodes.reference("", "Publication record" if english else "WOEAI 学术成果页对应条目",
                            refuri=uri, internal=True)
    if english:
        uri = app.builder.get_relative_uri(docname, "paper-notes/" + page["ref"])
        link += nodes.Text(" · ")
        link += nodes.reference("", "Chinese reading notes", refuri=uri, internal=True)
    section += link




def validate_citation_output(app, exception):
    if exception is None and app.builder.format == "html":
        problems = check_built_citations(_root(app), Path(app.outdir))
        if problems:
            raise SphinxError("Citation output validation failed:\n" + "\n".join(problems))
        app._paper_citation_output_checked = len(app._paper_citations)

def setup(app):
    app.connect("builder-inited", validate_citation_inputs)
    app.connect("source-read", track_registry)
    app.connect("doctree-resolved", project_citation)
    app.connect("build-finished", validate_citation_output)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
