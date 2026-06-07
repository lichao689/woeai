# WOEAI Publications Zotero Sync Plan

Date: 2026-06-07

Goal: update the RTD website's journal-paper list from the local Zotero public publication record while keeping the public page format consistent, source-bounded, and repeatable for future agents.

## Confirmed Decisions

### Source Boundary

- The authoritative publication source is Zotero `My Publications / 我的出版物`.
- Include only Zotero top-level items where:
  - `inPublications == true`
  - `itemType == journalArticle`
- Do not include general Zotero library references, attachments, notes, conference papers, theses, patents, or arbitrary collection contents.
- The previously unmatched teaching paper `中国共产党精神谱系视域下土木工程课程思政建设的探索与实践` has been added to Zotero `My Publications` and should be handled by the same source rule.

### CSL Style

Use the user's installed Zotero CSL style as the citation renderer:

- Source file: `/Users/lichao/Drive/Myfiles/96 常用备份/SoftConfig/zotero/jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcFav-01.csl`
- Installed style file: `/Users/lichao/Zotero/styles/jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcfav-01.csl`
- CSL id: `http://www.zotero.org/styles/jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcfav-01`
- SHA256: `fde99536c18e025299488fe4f65cd6269172d2274e1b48e877e64b24cd52aef1`

The script should call the Zotero local API with `include=data,bib` and the CSL `style` query parameter.

### Publication Metrics

- Publication Metrics are whatever the confirmed Zotero + CSL rendering emits, including impact factor, journal quartile, Chinese Academy of Sciences division, and citation count.
- Do not invent metrics.
- Do not query the web to fill missing metrics.
- Do not maintain a metrics override file in this cycle.
- If a paper has no available metric, omit that metric from the public entry instead of adding a placeholder.

### Output Format

- Generate the complete `docs/source/Publications.rst`, not just a paste-in fragment.
- Preserve a hand-authored template area for reading notes and selected highlights.
- Generate the journal-paper section from Zotero.
- Keep the current paragraph-style RST format, not a table.
- Use CSL output for author order and name format.
- Post-process CSL output only for:
  - visible Publication Numbers,
  - `Li Chao` / `李朝` bolding,
  - RST escaping,
  - RST anchor insertion,
  - site-specific highlight/reference synchronization.

### Numbering

- Publication Numbers are visible display numbers, not stable identifiers.
- Regenerate Publication Numbers for the current complete ordering.
- The newest paper should have the largest visible number.
- Order papers by publication year descending, then full parsed date descending within the year, then normalized title ascending when dates tie or only a year is available.
- When numbers change, update visible numbers in highlights and other prose that mention them.

### Anchors And Links

- Regenerate all publication anchors in this cycle.
- Use stable human-readable publication anchors:
  - Format: `ref-{first-author}{year}-{journal-initialism}`.
  - `first-author` is the first author's family name for English names, or pinyin family name for Chinese names.
  - `year` is the publication year.
  - `journal-initialism` is derived from the full journal title's uppercase initials, for example `Ocean Engineering` -> `OE`, `Journal of Building Engineering` -> `JBE`, `Physics of Fluids` -> `POF`.
  - If two papers collide, append a deterministic short title token rather than an order-based suffix.
- After regenerating anchors, update every intra-site `:ref:` that points to publication anchors.
- Do not rely on old anchors remaining valid.
- Do not leave broken references; `./scripts/check-docs.sh` must pass.

### Highlights And Direction Pages

- Update `Selected Highlights` and relevant direction pages using Representative Publications only.
- Do not list every newly added paper in highlights.
- Representative Publications should support recruitment, technical collaboration, or academic credibility for a research theme.

### Script And Snapshot Locations

- Add script: `scripts/update-publications-from-zotero.py`
- Add source snapshot: `docs/superpowers/source-packets/2026-06-publications-zotero-snapshot.json`
- The snapshot is evidence for review, not an RTD build input.
- RTD must continue to build static committed RST only; it must not depend on live Zotero.
- Commit the script, snapshot, generated `Publications.rst`, and related reference updates together in one changeset.

## Current Data Observations

- Zotero local API base: `http://127.0.0.1:23119`
- Zotero local API status was healthy on 2026-06-07.
- After adding the teaching paper, Zotero `My Publications` contains 74 journal articles.
- The current website contains 61 journal-paper entries before this sync.
- The first diff pass found 13 Zotero journal articles missing from the website before the teaching paper was added to Zotero.

## Open Decisions

None.

## Verification

Run before claiming completion:

```bash
./scripts/check-docs.sh
git diff --check
rg -n ':ref:`[^`]+<ref-' docs/source
```

Also inspect the generated `Publications.html` for:

- author bolding,
- line wrapping,
- DOI rendering,
- omitted unavailable metrics,
- updated selected highlights,
- no stale visible publication numbers.
