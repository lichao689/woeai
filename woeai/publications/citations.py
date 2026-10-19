"""Canonical, validated bibliography for paper-reading pages."""
import re
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

from woeai.publications.registry import load_registry


def normalized_text(value):
    return " ".join(unicodedata.normalize("NFKC", value).split())


def _required(value, ref, field):
    normalized = normalized_text(value) if isinstance(value, str) else ""
    normalized = re.sub(r"[\u200b-\u200f\u2060\ufeff]", "", normalized)
    if (not normalized or normalized.casefold() in {"n/a", "na", "none", "null", "unknown", "pending"}
            or re.search(r"\b(?:TODO|TBD|placeholder)\b|\u5f85\u8865|\u5f85\u786e\u8ba4|\u5360\u4f4d", normalized, re.I)
            or not any(c.isalnum() for c in normalized)):
        raise ValueError(f"{ref}: citation {field} is missing or placeholder text")
    return value.strip()


def _name_characters(name):
    return sorted(c.casefold() for c in normalized_text(name) if c.isalnum())


def citation_for_record(record):
    """Project checked registry text, rejecting incomplete or inconsistent metadata."""
    custom = record["custom"]
    ref = custom["publication_ref"]
    bib = custom["legacy_bibliography"]
    title = _required(bib.get("title"), ref, "title")
    journal = _required(bib.get("publicationTitle"), ref, "publicationTitle")
    creators = bib.get("creators")
    if not isinstance(creators, list) or not creators:
        raise ValueError(f"{ref}: citation creators must be a nonempty author list")
    creators = [_required(author, ref, "creators") for author in creators]
    year = bib.get("year")
    if type(year) is not int or not 1000 <= year <= 9999:
        raise ValueError(f"{ref}: citation year must be a recorded four-digit year")
    if (normalized_text(_required(record.get("title"), ref, "title")) != normalized_text(title)
            or normalized_text(_required(record.get("container-title"), ref, "publicationTitle")) != normalized_text(journal)):
        raise ValueError(f"{ref}: citation title/journal inconsistent with structured registry")
    date = record.get("issued", {}).get("date-parts", [[]])
    if not date or not date[0] or date[0][0] != year:
        raise ValueError(f"{ref}: citation year inconsistent with structured registry")
    if record.get("DOI") and bib.get("doi") and record["DOI"] != bib["doi"]:
        raise ValueError(f"{ref}: citation doi inconsistent with structured registry")
    if "author" in record:
        if not isinstance(record["author"], list) or not record["author"] or any(not isinstance(a, dict) for a in record["author"]):
            raise ValueError(f"{ref}: citation authors inconsistent with structured registry")
        names = [" ".join(str(a.get(k, "")) for k in ("given", "family")).strip()
                 if not a.get("literal") else a["literal"] for a in record["author"]]
        if (len(names) != len(creators)
                or any(_name_characters(a) != _name_characters(b)
                       for a, b in zip(names, creators))):
            raise ValueError(f"{ref}: citation authors inconsistent with structured registry")
    rendered = _required(bib.get("rendered"), ref, "rendered")
    normalized = normalized_text(rendered)
    for field in (title, journal, str(year)):
        if normalized_text(field) not in normalized:
            raise ValueError(f"{ref}: citation rendered body is inconsistent with required fields")
    # Name order may be family/given or given/family, but authors may not vanish.
    author_part = normalized.split(normalized_text(title), 1)[0].rstrip(" ,.")
    rendered_authors = author_part.split(";")
    if (len(rendered_authors) != len(creators)
            or any(_name_characters(a) != _name_characters(b)
                   for a, b in zip(rendered_authors, creators))):
        raise ValueError(f"{ref}: citation rendered body lacks the complete recorded authors")
    text = re.split(r"\s+(?:影响因子|中科院分区|引用次数)\s*[:：]", rendered, maxsplit=1)[0].strip()
    doi = record.get("DOI") or bib.get("doi")
    if doi:
        doi = _required(doi, ref, "doi")
        if not re.fullmatch(r"10\.\d{4,9}/[^\s<>]+", doi):
            raise ValueError(f"{ref}: citation doi is invalid")
        linked = re.findall(r"https?://(?:dx\.)?doi\.org/([^\s]+)", text)
        if any(value.rstrip(".").casefold() != doi.casefold() for value in linked):
            raise ValueError(f"{ref}: citation rendered DOI conflicts with recorded doi")
        if doi.casefold() not in text.casefold():
            text += f" https://doi.org/{doi}."
    if "citation_note" in custom:
        text += " " + _required(custom["citation_note"], ref, "citation_note")
    return text


def reading_citations(root):
    """Enumerate every actual reading source; absent registry data is an error."""
    records = load_registry(Path(root))
    by_ref = {}
    for row in records:
        ref = row["custom"]["publication_ref"]
        if ref in by_ref:
            raise ValueError(f"{ref}: duplicate citation registry entry")
        by_ref[ref] = row
    pages = []
    for folder in ("paper-notes", "en/highlights"):
        for source in sorted((Path(root) / "docs/source" / folder).glob("*.rst")):
            ref = source.stem
            if ref not in by_ref:
                raise ValueError(f"{ref}: reading page has no registered citation")
            row = by_ref[ref]
            pages.append({"ref": ref, "docname": f"{folder}/{ref}",
                          "text": citation_for_record(row),
                          "doi": row.get("DOI") or row["custom"]["legacy_bibliography"].get("doi") or ""})
    return pages


def citation_for_ref(root, publication_ref):
    matches = [r for r in load_registry(root)
               if r["custom"]["publication_ref"] == publication_ref]
    if len(matches) != 1:
        raise ValueError(f"{publication_ref}: exactly one registered citation is required")
    return citation_for_record(matches[0])




class _CitationHTML(HTMLParser):
    """Inspect the real emitted citation paragraph, including hidden ancestors."""
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        hidden = (bool(self.stack and self.stack[-1][1]) or "hidden" in attrs
                  or attrs.get("aria-hidden") == "true"
                  or bool(re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden)", attrs.get("style", ""), re.I)))
        if tag in self.VOID:
            return
        self.stack.append((tag, hidden))
        if "paper-full-citation" in attrs.get("class", "").split():
            self.blocks.append({"depth": len(self.stack), "hidden": hidden, "text": [], "links": [], "active": True})
        if tag == "a":
            for block in self.blocks:
                if block["active"]:
                    block["links"].append(attrs.get("href"))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break
        for block in self.blocks:
            if len(self.stack) < block["depth"]:
                block["active"] = False

    def handle_data(self, data):
        for block in self.blocks:
            if block["active"]:
                block["text"].append(data)


def check_built_citations(root, outdir):
    """Fail missing outputs, empty/hidden bodies, stale text and missing DOI links."""
    problems = []
    for page in reading_citations(root):
        path = Path(outdir) / (page["docname"] + ".html")
        if not path.is_file():
            problems.append(f"{page['docname']}: citation HTML output missing")
            continue
        parser = _CitationHTML()
        parser.feed(path.read_text(encoding="utf-8"))
        if len(parser.blocks) != 1:
            problems.append(f"{page['docname']}: expected one rendered citation body, got {len(parser.blocks)}")
            continue
        body = parser.blocks[0]
        if body["hidden"]:
            problems.append(f"{page['docname']}: rendered citation body is hidden")
        if normalized_text("".join(body["text"])) != normalized_text(page["text"]):
            problems.append(f"{page['docname']}: rendered citation body is empty, placeholder or inconsistent")
        if page["doi"] and "https://doi.org/" + page["doi"] not in body["links"]:
            problems.append(f"{page['docname']}: recorded DOI link missing from rendered citation")
    return problems
