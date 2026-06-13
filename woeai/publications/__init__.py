"""Publication data model and rendering for WOEAI Academic Outputs.

Stage 1 of the architecture plan populates this package with the Publication
data model, taxonomy, author-marker logic, and citation rendering currently
inlined in ``scripts/update-publications-from-zotero.py``.
"""

from woeai.publications.taxonomy import (
    RESEARCH_FAMILY_ORDER,
    RESEARCH_SUBDIRECTION_ORDER,
)

__all__ = ["RESEARCH_FAMILY_ORDER", "RESEARCH_SUBDIRECTION_ORDER"]
