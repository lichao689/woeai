# Reading-page complete citations

This guide owns bibliography projection and rendered-output checks for Chinese
paper-notes and English highlights. Scientific translations and original-paper
reference lists remain governed by paper-deep-dive-rst.md.

## One bibliographic authority

docs/data/publications.json supplies the checked title, complete ordered author
list, journal, year, citation body and known DOI. Structured CSL fields and the
legacy compatibility bibliography must agree where both are present. A known
structured DOI may be used when an older compatibility field is absent. Never
invent a DOI, final volume, issue or page range. Unknown DOI is allowed; a supplied
placeholder or malformed DOI is an error, not an acceptable missing value.
Publication metrics are not part of the full citation. Source-backed custom.citation_note
retains first-release/version limits when needed; first-release page counts must
not be presented as verified final volume/issue pagination.

Existing per-paper RST remains the scientific body source. The paper_citations
Sphinx extension projects one checked full citation at build time into every
actual Chinese note and English highlight, replacing legacy citation-only
paragraphs or adding the missing closing citation section. It preserves existing
section anchors and the latest reading layout. Do not hand-maintain another
bibliography by parsing Publications.rst presentation containers.

## Required gates

- Enumerate source files in paper-notes/ and en/highlights/; every source must map
  to exactly one registered citation. New pages automatically join the checks.
- Validate required fields, placeholder text, full authors and compatibility with
  structured metadata before building, including incremental builds. Registry
  changes are tracked as source dependencies.
- After successful HTML generation, check every expected output file and its
  unique paper-full-citation paragraph. The actual emitted text must match the
  checked complete citation; known DOI links must exist. Missing/duplicate/empty/
  placeholder/inline-hidden output is a hard build error.
- CI must run Chromium against all built reading pages at desktop and narrow
  widths. Read the expanded paragraph's innerText and computed visibility, not
  just source bytes or textContent. Hiding, clipping, missing text and a wrong DOI
  link must fail. Browser regression tests include these real DOM failures.
- The legacy Markdown converter shares the same registry citation validator.
  Unregistered or incomplete bibliography fails; warning-and-omit is retired.
  This does not authorize regenerating independent full-paper pages from WeChat.

Run the normal ./scripts/check-docs.sh gate. For the mandatory browser gate:

    npm ci --prefix tests/browser --ignore-scripts
    tests/browser/node_modules/.bin/playwright install --with-deps chromium
    node --test tests/browser/citation-check.test.cjs
    PYTHON_BIN=/tmp/woeai-docs-venv/bin/python node tests/browser/check-paper-citations.cjs /tmp/woeai-sphinx-html

On the authorized Mac, an existing Chrome may be selected with the process-local
WOEAI_BROWSER_EXECUTABLE path; local workflow uses .venv/bin/python and
docs/_build/html. The browser test server binds loopback only. Built-page tests
block third-party resources because citation visibility does not depend on ads
or remote formula scripts; live-site acceptance uses the normal Mac browser.

Citation-only metadata corrections require source evidence and a documented
non-content comparison. Preserve old scientific reviews and statuses; do not
mechanically rehash old approval, claim a new PDF audit, or promote phone-preview
or publication flags.
