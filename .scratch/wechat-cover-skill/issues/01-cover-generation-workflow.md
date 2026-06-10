# Issue 01: Build The Repo-Local WeChat Cover Workflow

Status: ready-for-agent

## Summary

Build a first repo-local workflow for generating, reviewing, and recording WOEAI
WeChat paper-article cover images. This is the proving ground before creating a
global `wechat-cover` skill.

## Background

The current WeChat paper pipeline can create a draft through the official
WeChat draft API, but cover generation is still manual and under-specified. The
first test cover used `900 x 383 px` and worked as an API asset, but the user
wants a more deliberate, attractive, article-aware cover process.

## Tasks

1. Verify current WeChat cover-size and crop guidance before hard-coding any
   reusable standard.
2. Define a compact cover brief format derived from:
   - title category,
   - article title,
   - abstract,
   - key finding,
   - target reader,
   - avoid list.
3. Generate or document at least three candidate cover directions for
   `ref-zhao2026-BS`.
4. Add a simple preview/check process for:
   - full cover ratio,
   - center/square thumbnail crop,
   - no distorted generated text,
   - visual relevance to the article.
5. Store approved public-safe outputs under
   `wechat/assets/public-safe/<publication_ref>/`.
6. Update the review-note shape so cover prompt, source, final path, dimensions,
   approval, and WeChat backend preview state are consistently recorded.
7. Update `wechat/STYLE.md` and `.agents/skills/wechat-paper/SKILL.md` only if
   the trial reveals a stable new rule.

## Acceptance Criteria

- The repo has a documented cover workflow that another agent can follow for
  the next WOEAI paper article.
- `ref-zhao2026-BS` has at least three cover candidate concepts or candidate
  images recorded in a public-safe way.
- The chosen final cover has dimensions recorded and a thumbnail-safety check.
- The review note clearly distinguishes:
  - generated source image,
  - final cropped/resized image,
  - backend preview still pending or complete.
- No secrets, private preview material, raw API responses, or private image
  references are committed.

## Suggested Implementation Notes

- Prefer a small helper script only if it removes repeated manual work.
- Keep prompts public-safe and avoid unpublished project names.
- Do not embed Chinese title text in generated images by default.
- Keep the cover visually tied to the article rather than a generic research
  illustration.

## Comments

- 2026-06-09: User chose repo-local task first, not immediate global skill.
