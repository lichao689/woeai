# WOEAI Site Agent Guide

This repository is the public website for the WOEAI research group. Treat it as
a Sphinx documentation site, not as an application package.

## Outcome Priority

Use this order when deciding homepage placement, navigation weight, and copy
tradeoffs:

1. 招生 Recruitment
2. 产业合作 Industry Collaboration
3. 学术可信度 Academic Credibility

## Required Checks

Run this before claiming a site change is complete:

```bash
./scripts/check-docs.sh
```

The script installs only `docs/requirements.txt` into a temporary virtual
environment and builds HTML with Sphinx warnings treated as failures.

## Content Boundaries

- Do not invent partner names, lab facilities, admission quotas, stipend
  amounts, dated news, media coverage, awards, or publication claims.
- For public facts, start from
  `docs/superpowers/source-packets/2026-06-woeai-site-source-packet.md` and the
  existing source pages under `docs/source/`.
- Unknown facts should be written as "to be confirmed" in planning documents,
  not published as definite public claims.
- Keep recruitment copy direct and useful. It may explain research directions,
  expected backgrounds, contact path, and application materials when those are
  source-supported.
- Keep industry collaboration copy capability-based unless named partners or
  cases are explicitly source-backed.

## Site Structure

- `docs/source/index.rst` owns the homepage and top-level navigation.
- `docs/source/Recruitment.rst` should be the first conversion path.
- `docs/source/IndustryCollaboration.rst` should be the second conversion path.
- `docs/source/Research.rst` should connect research themes to direction pages
  and publications.
- `docs/source/People.rst`, `docs/source/Projects.rst`, and
  `docs/source/Publications.rst` are proof pages and should stay factual.

## Editing Notes

- Prefer small, independently verifiable commits.
- Keep Sphinx references valid; broken anchors become release blockers.
- Keep template residue out of the public site.
- Do not add Python package metadata unless the repository intentionally becomes
  an installable package in a future plan.
