WOEAI Website
=============

This repository publishes the WOEAI group website for Wind & Ocean Engineering
empowered by AI at Harbin Institute of Technology, Shenzhen.

The site is a Sphinx documentation project, not a Python package. Its public
purpose is ordered as:

1. recruitment for students, postdocs, and research talent;
2. industry collaboration around wind engineering, offshore wind energy, and
   AI-enabled engineering methods;
3. academic credibility through people, projects, publications, teaching, and
   research directions.

Local Checks
------------

Use the repository-owned check script before committing changes:

.. code-block:: bash

   ./scripts/check-docs.sh

The script creates a temporary virtual environment, installs
``docs/requirements.txt``, and runs Sphinx with warnings treated as failures.

Content Rules
-------------

- Prefer source-backed updates over invented marketing copy.
- Use ``docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md``
  as the first reference for facts that were available during the 2026 site
  upgrade.
- Keep the homepage ordered around recruitment, industry collaboration, then
  academic credibility.
- Keep public pages free of template residue such as sample Python package
  documentation, placeholder usage pages, and unowned news cadence.

Key Paths
---------

- ``docs/source/index.rst``: homepage and navigation.
- ``docs/source/Recruitment.rst``: recruitment journey.
- ``docs/source/IndustryCollaboration.rst``: industry collaboration journey.
- ``docs/source/Research.rst``: research overview and direction hub.
- ``docs/source/Publications.rst``: publication proof.
- ``docs/source/Projects.rst``: project proof.
- ``docs/source/Contact.rst``: contact and QR entry point.
- ``docs/requirements.txt``: documentation build dependencies.
- ``scripts/check-docs.sh``: strict local verification.
