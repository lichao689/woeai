WOEAI Website
=============

This repository publishes the WOEAI website for Wind and Ocean Engineering with
AI.

The site is a Sphinx documentation project, not a Python package. Its public
purpose is ordered as:

1. recruitment for students, postdocs, and research talent;
2. engineering applications around wind engineering, offshore wind energy, and
   AI-enabled engineering methods;
3. academic credibility through academic outputs, teaching, public research
   support, and research directions.

Repository Map
--------------

- ``docs/``: public website sources (``docs/source/``), structured website data
  (``docs/data/``), and Sphinx build dependencies. Start at
  `the homepage source <docs/source/index.rst>`_.
- ``wechat/``: article sources, evidence reviews, approved assets, and the
  existing WeChat workflow. Start at `the WeChat guide <wechat/README.md>`_.
- ``project/``: project maintenance guides, plans, specifications, research,
  and factual source packets. Start at `the project index <project/README.md>`_.
- ``tools/``: command entry points for publication maintenance. Existing
  ``wechat/tools/`` commands remain in place; tool consolidation is deferred.
- ``woeai/``: shared Python logic imported by repository commands, not an
  independently installable distribution.
- ``scripts/``: environment setup, build/check commands, site release metadata,
  and the existing Zotero publication-update entry point.
- ``tests/``: regression tests for the shared logic and command workflows.
- ``AGENTS.md``: contributor/agent guidance; ``CONTEXT.md``: project vocabulary.

Local Checks
------------

Use the repository-owned check script before committing changes:

.. code-block:: bash

   ./scripts/check-docs.sh

The script creates a temporary virtual environment, installs
``docs/requirements.txt``, and runs Sphinx with warnings treated as failures.

Site Build ID
-------------

This repository is a public documentation site, not a package with API
compatibility releases. Before publishing a site update, refresh the Sphinx
metadata with a Beijing-time Site Build ID:

.. code-block:: bash

   ./scripts/bump-site-release.py
   ./scripts/check-docs.sh

``docs/source/conf.py`` stores ``release`` as ``YYYY.MM.DD-HHMM`` and
``version`` as ``YYYY.MM.DD``. Do not change ``.readthedocs.yaml`` ``version:
"2"`` for this purpose; that value is the ReadTheDocs configuration schema.

Content Rules
-------------

- Prefer source-backed updates over invented marketing copy.
- Use ``project/sources/2026-06-woeai-site-source-packet.md``
  as the first reference for facts that were available during the 2026 site
  upgrade.
- Keep the homepage ordered around recruitment, engineering applications, then
  academic credibility.
- Keep public pages free of template residue such as sample Python package
  documentation, placeholder usage pages, and unowned news cadence.

Key Paths
---------

- ``docs/source/index.rst``: homepage, recruitment content, contact information,
  and navigation.
- ``docs/source/EngineeringApplications.rst``: engineering applications journey.
- ``docs/source/Research.rst``: research overview and direction hub.
- ``docs/source/Publications.rst``: academic-output proof.
- ``docs/source/Teaching.rst``: teaching and education proof.
- ``docs/requirements.txt``: documentation build dependencies.
- ``scripts/bump-site-release.py``: refreshes the Sphinx Site Build ID.
- ``scripts/check-docs.sh``: strict local verification.
