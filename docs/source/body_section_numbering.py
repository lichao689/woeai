"""Number HTML body H2/H3 after Sphinx has collected unnumbered navigation.

IDs are already assigned, so counters never change fragment URLs. References
inside explicit body contents topics reuse the same numbers. Global toctrees,
breadcrumbs and cross-references retain their original labels. Paper translations
keep their source numbering; presentation and bibliography indexes are excluded.
"""
import re

from docutils import nodes
from sphinx.errors import SphinxError
from sphinx.transforms.post_transforms import SphinxPostTransform

EXCLUDED_DOCS = {
    "index", "en/index", "Publications", "en/Publications",
    "PublicationsByYear", "GroupNews", "PublicationProgress", "en/Search",
}
# Arabic/CJK list markers and dotted prefixes may omit the separating space.
# A digit followed directly by a scientific abbreviation (3D, 1.5D) is not a marker.
MANUAL_NUMBER = re.compile(
    r"^(?:"
    r"\d+(?:\.\d+)*\s+\S|"
    r"\d+(?:\.\d+)*[、．)）]\s*\S|"
    r"\d+(?:\.\d+)*\.(?=\D)\s*\S|"
    r"\d+(?:\.\d+)+(?=[\u3400-\u9fff])|"
    r"\d+(?:\.\d+)*$|"
    r"[一二三四五六七八九十百]+[、．.)）]\s*\S|"
    r"[(（]\d+(?:\.\d+)*[)）]\s*\S)"
)
NUMBER_CLASS = "body-section-number"
REFERENCE_CLASS = "unnumbered-reference"


def numbering_enabled(docname):
    return docname not in EXCLUDED_DOCS and not docname.startswith("paper-notes/")


def section_depth(section):
    depth = 1
    parent = section.parent
    while parent is not None:
        if isinstance(parent, nodes.section):
            depth += 1
        parent = parent.parent
    return depth


def is_reference_section(section):
    parent = section
    while parent is not None:
        if REFERENCE_CLASS in parent.get("classes", []):
            return True
        parent = parent.parent
    return False


def prepend_number(node, number):
    node.insert(0, nodes.inline("", number + " ", classes=[NUMBER_CLASS]))


class BodySectionNumbering(SphinxPostTransform):
    default_priority = 800
    formats = ("html",)

    def run(self, **kwargs):
        if not numbering_enabled(self.env.docname):
            return
        # Reapplying output transforms must not duplicate their own prefixes.
        for prefix in list(self.document.findall(nodes.inline)):
            if NUMBER_CLASS in prefix.get("classes", []):
                prefix.parent.remove(prefix)
        numbers = {}
        major = minor = 0
        for section in self.document.findall(nodes.section):
            if is_reference_section(section):
                continue
            title = next((child for child in section if isinstance(child, nodes.title)), None)
            if title is None:
                continue
            if MANUAL_NUMBER.match(title.astext()):
                raise SphinxError(
                    f"{self.env.docname}: manual section number in {title.astext()!r}; "
                    "ordinary headings must be unnumbered in source (body numbering is automatic)."
                )
            depth = section_depth(section)
            if depth == 2:
                major += 1
                minor = 0
                number = str(major)
            elif depth == 3:
                minor += 1
                number = f"{major}.{minor}"
            else:
                continue
            prepend_number(title, number)
            for fragment in section["ids"]:
                numbers[fragment] = number
        # Docutils contents directives are body-local; env.tocs is never changed.
        for topic in self.document.findall(nodes.topic):
            if "contents" not in topic.get("classes", []):
                continue
            for reference in topic.findall(nodes.reference):
                fragment = reference.get("refid") or reference.get("refuri", "").removeprefix("#")
                if fragment in numbers:
                    prepend_number(reference, numbers[fragment])


def setup(app):
    app.add_post_transform(BodySectionNumbering)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
