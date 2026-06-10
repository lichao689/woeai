# WOEAI WeChat Cover Quality Upgrade Plan

> For agentic workers: use the `wechat-cover` skill for this work. This plan
> upgrades the cover workflow before regenerating final covers. Do not treat
> dimension checks alone as cover approval.

## Goal

Upgrade WOEAI WeChat paper-article covers from "dimension-safe assets" to
"click-worthy, article-specific editorial covers" while preserving public
safety, WeChat crop safety, and the Manual Publication Gate.

## Implementation Status

- Phase 1 standards update: implemented in `wechat-cover` skill,
  `cover-standards.md`, and `wechat/STYLE.md`.
- Phase 2 preview tooling: candidate labels, optional score metadata, and
  small-thumbnail preview implemented in `cover_preview.py`.
- Phase 2 text tooling: `cover_text_overlay.py` added. It performs deterministic
  overlay when Pillow is available and returns a clear JSON dependency error
  when Pillow is not available in the current Python runtime.
- Phase 3 pilot: executed for `ref-zhao2025-SCS`. Generated and compared
  `2` no-text image-gen candidates, `2` image-gen short-text candidates, and
  `2` programmatic-overlay candidates. Candidate D was confirmed by the user
  and switched into the public-safe formal v2 cover asset.
- Phase 4 batch cover regeneration: not yet executed.

The new workflow should support both:

- generated visual candidates without embedded text;
- generated or composed candidates with short Chinese text.

Direct image-generation text is allowed as an experiment, but any distorted,
misspelled, low-contrast, or unreadable text must be rejected. Deterministic
programmatic text overlay remains the fallback and preferred production route
when exact Chinese text matters.

## Current Problem

The existing `wechat-cover` skill mostly checks:

- `900 x 383 px` size and `2.35:1` ratio;
- centered composition for square/share-card crops;
- no embedded secrets, private details, logos, or unapproved text;
- review-note metadata.

It does not yet strongly evaluate:

- whether the cover has a clear visual subject;
- whether it is specific to the paper instead of generic technology wallpaper;
- whether it is still readable as a small WeChat thumbnail;
- whether it creates enough curiosity to click;
- whether the visual language is consistent across WOEAI research families.

## Domain Map

- `WeChat Article Source`: the public-safe Markdown content master.
- `One-Paper WeChat Article`: the article unit; one paper, one cover.
- `RTD Paper Companion Page`: derived website page; may reuse the final cover.
- `WeChat Draft Record`: non-sensitive draft metadata after API submission.
- `wechat-cover`: cover brief, candidates, preview, quality review, metadata.
- `cover_preview.py`: local technical and crop preview; should become a
  candidate comparison board, not only a size checker.
- `wechat_draft.py`: consumes approved cover path for dry-run and live draft
  creation/update, but must not judge visual quality by itself.

## Design Decisions

1. Produce at least two cover families per article:
   - no-text editorial visual;
   - short-text editorial visual.
2. Try image-gen direct text as one candidate lane when useful.
3. Keep deterministic text overlay available for exact final wording.
4. Keep cover text short:
   - category tag: `数值风洞`, `结构抗风`, or `漂浮风电`;
   - main hook: normally 8-14 Chinese characters;
   - optional subtitle only when the thumbnail remains readable.
5. Let the WeChat title carry the full article title. The cover text should
   create curiosity, not repeat the full paper title.
6. Do not mark `cover_image_checked: true` until the WeChat backend/mobile
   preview is actually checked.

## Proposed File Changes

### Skill And Standards

- Update `.agents/skills/wechat-cover/SKILL.md`.
  - Add candidate generation lanes: no-text, image-gen text, deterministic text
    overlay.
  - Require candidate scoring before selecting a final cover.
  - Require small-thumbnail review before approval.
- Update `.agents/skills/wechat-cover/references/cover-standards.md`.
  - Add a visual quality rubric.
  - Add typography rules.
  - Add rejection criteria.
  - Add research-family visual language.
- Optionally update `wechat/STYLE.md` so article-level cover rules match the
  skill.

### Scripts

- Extend `.agents/skills/wechat-cover/scripts/cover_preview.py`.
  - Support multiple candidates with labels.
  - Show full cover, square crop, share-card crop, and small-thumbnail views.
  - Display basic scores/check fields beside each candidate.
  - Keep output under `wechat/.local/cover-previews/`.
- Add a deterministic text overlay helper, for example:
  - `.agents/skills/wechat-cover/scripts/cover_text_overlay.py`
  - Inputs: base image, category tag, main hook, optional subtitle, output path.
  - It should use local fonts when available and fail clearly when no Chinese
    font is usable.
- Optionally add a simple candidate manifest format:
  - `wechat/.local/cover-candidates/<publication_ref>/manifest.json`
  - This remains ignored/private unless a final public-safe asset is selected.

### Review Notes And Briefs

- Update cover brief expectations:
  - cover promise;
  - target reader;
  - hook text options;
  - no-text prompt;
  - image-gen direct-text prompt;
  - deterministic overlay text;
  - avoid list;
  - candidate scoring notes.
- Update review note cover fields:
  - candidate count;
  - selected candidate ID;
  - selected text mode: `none`, `image-gen-text`, or `programmatic-overlay`;
  - rejected candidate reasons;
  - local candidate-board path;
  - WeChat backend preview status.

## Quality Rubric

Score each candidate from 1 to 5:

- Article specificity: does it clearly match this paper?
- Main-subject clarity: can a reader identify the subject in one second?
- Click appeal: does it create curiosity without hype?
- Engineering credibility: does it look technically serious, not decorative?
- Small-thumbnail readability: does it still work when small?
- Crop safety: does the subject survive square and share-card crops?
- Text quality, when present: is every character correct and readable?

Reject immediately if:

- Chinese text is wrong, distorted, incomplete, or unreadable;
- the image looks like generic AI technology wallpaper;
- the main subject is too faint or too small;
- the cover depends on tiny labels, formulas, or dense paper-figure details;
- it shows unapproved logo, partner, real project identity, or private detail;
- it contains a fake UI, fake map label, or misleading publication claim.

## Research-Family Visual Language

### 数值风洞

Use urban blocks, CFD grids, flow streamlines, turbulence/inflow, validation
points, database layers, or WebGIS layers. Avoid generic skylines unless the
method cue is unmistakable.

### 结构抗风

Use high-rise structural frames, wind pressure fields, floor response traces,
GNN nodes, vibration/control cues, or load paths. Avoid bare buildings without
structural or response information.

### 漂浮风电

Use floating platforms, wind-wave-current loading, mooring systems,
hydrodynamic response, structural optimization, or offshore environment.
Avoid generic wind turbines without floating-platform or ocean-engineering cues.

## Implementation Phases

### Phase 1: Standards And Skill Rewrite

- Update `wechat-cover` skill and cover standards.
- Add quality rubric, text policy, candidate lanes, and rejection criteria.
- Define review note fields.

Exit condition:

- The skill tells future agents how to create, compare, reject, and record
  cover candidates.

### Phase 2: Preview And Text Tooling

- Extend `cover_preview.py` into a candidate comparison board.
- Add deterministic text overlay helper.
- Add tests for dimensions, text metadata, output paths, and failure cases.

Exit condition:

- A worker can compare multiple candidate covers locally without opening
  WeChat or reading credentials.

### Phase 3: Pilot On One Article

Pilot on `ref-zhao2025-SCS`, because its current cover is conceptually correct
but visually too faint.

Generate at least:

- 2 no-text image-gen candidates;
- 2 image-gen direct-text candidates;
- 2 deterministic-overlay candidates from the best no-text images.

Exit condition:

- Candidate board shows all variants.
- At least one candidate passes the rubric and small-thumbnail check.
- Review note records why the final candidate was selected.

### Phase 4: Batch Regeneration

Apply the upgraded workflow to current pending covers:

- `ref-zhao2025-SCS`
- `ref-li2024-POF`
- `ref-tang2025-JBE`
- `ref-he2026-OE-structural`
- optionally revisit `ref-zhao2026-BS`

Exit condition:

- Each paper has a selected final cover, candidate-board path, review-note
  record, and dry-run/preflight compatibility.

### Phase 5: WeChat Backend Preview

- Create or update drafts only after explicit user confirmation.
- Check covers in the real WeChat backend/mobile preview.
- Only then set `cover_image_checked: true`.

Exit condition:

- Final cover approval is based on actual WeChat preview, not only local
  generated images.

## Verification

Run after implementation:

```bash
python .agents/skills/wechat-cover/scripts/cover_preview.py \
  wechat/assets/public-safe/<publication_ref>/cover-wechat-900x383-v1.png

python scripts/check-public-safe-content.py
python wechat/tools/wechat_draft.py dry-run --publication-ref <publication_ref>
python wechat/tools/markdown_to_rtd.py --publication-ref <publication_ref> --check
git diff --check
```

Run `./scripts/check-docs.sh` when RTD pages, Sphinx config, or generated RST
files are changed.

## Open Human Choices

Before final batch regeneration, the user should confirm:

- whether cover text should usually include only the short hook, or both
  category tag and hook;
- preferred tone: more academic-clean, more magazine-like, or more bold;
- whether WOEAI should use a subtle recurring brand mark or remain text-free
  except for the WeChat article title;
- whether image-gen direct text candidates should be considered final if the
  text is perfectly readable, or only used as inspiration.
