---
name: woeai-wechat-paper
description: Use when generating, reviewing, or updating WOEAI WeChat Official Account articles from published journal papers. Applies to one-paper-one-article drafts, historical paper reposts, formula and figure handling, backlog updates, and public-safe publication workflows in this repository.
---

# WOEAI WeChat Paper Article Skill

Use this skill when a task asks to create, revise, review, or track a WeChat Official Account article based on a published WOEAI journal paper.

The output is a public-safe Markdown draft and workflow metadata. Do not publish to WeChat automatically.

## Required Context

Read these files before drafting:

1. `AGENTS.md` for public-site boundaries and required checks.
2. `CONTEXT.md` for WOEAI vocabulary and semantic constraints.
3. `wechat/README.md` for the WeChat content workflow and backlog state model.
4. `wechat/STYLE.md` for article structure, tone, formula rules, and figure rules.
5. `wechat/templates/paper-explainer.md` for the draft shape.
6. `wechat/templates/review-checklist.md` for review gates.
7. `wechat/backlog/selected-papers.yml` to select and update the paper state.
8. `docs/source/Publications.rst` and the relevant research direction page for public website anchors.

If the task mentions Zotero, DOI, a PDF, or a paper title, inspect those sources when available. Do not invent missing bibliographic facts.

When a local PDF or author manuscript is available, inspect the original paper body, figures, captions, and conclusion instead of relying only on a public abstract.

## Article Unit

Use one selected paper per article.

Do not turn a paper article into a multi-paper survey. Related papers can appear only in `延伸阅读`.

## Public Safety

This repository is public. Anything committed here must be safe to expose.

Never include:

- WeChat AppSecret, access token, refresh token, cookies, preview credentials, or API keys.
- Zotero API keys or private library credentials.
- private partner names or unpublished project details.
- private review notes.
- publisher-owned figures unless reuse rights or author-owned source status are confirmed.
- local WeChat preview HTML.
- source images that are not approved for public release.

Unknown public facts should be written as `to be confirmed` in private planning notes, not in public drafts.

## Research Taxonomy

Use only these public research families and subdirections unless the user explicitly updates the taxonomy:

- `建筑结构抗风`
  - `数值风洞与湍流入流`
  - `高层建筑抗风与优化`
- `海上漂浮风电`
  - `浮式风机系统一体化分析与优化`
  - `浮式混凝土平台结构设计`
  - `数值风浪流水池`

## Draft Workflow

1. Select the target item from `wechat/backlog/selected-papers.yml`.
2. Verify `publication_ref`, title, year, DOI, and WOEAI website anchor.
3. Create or update the draft under `wechat/articles/draft-public-safe/`.
4. Name the draft with the paper's `publication_ref`, for example `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`.
5. Start from `wechat/templates/paper-explainer.md`.
6. Keep `wechat_status` aligned with the backlog state model:
   - `selected`
   - `drafting`
   - `reviewing`
   - `ready_to_publish`
   - `published`
   - `archived`
7. Update `wechat/backlog/selected-papers.yml` only when the user's task asks for workflow tracking or after a draft/review step changes status.

## Article Structure

Use this default order unless the paper strongly requires a small adjustment:

1. `论文信息`
2. `研究问题`
3. `方法贡献`
4. `关键发现`
5. `公式说明`
6. `工程意义`
7. `适用边界`
8. `图示与素材来源`
9. `延伸阅读`
10. `联系入口`

Write for technically literate readers who may include prospective students, collaborators, engineering software users, and academic peers.

Tone:

- Use the author's perspective and voice. The article should read like WOEAI or the authors are explaining their own paper to readers.
- Prefer `我们在这项研究中...`, `这项工作...`, and `这篇论文...` over third-party phrases such as `从公开摘要可确认...`.
- Scholarly first.
- Engineering relevance second.
- No hype.
- No unsupported partner names or project claims.
- Keep limitations visible.
- Avoid standing outside the paper as a detached reviewer unless explicitly writing a review note.

## Formula Handling

Do not render formulas as images.

Use the most direct formula format supported by the WeChat publishing workflow selected for the article. Keep formulas short enough for mobile display when possible.

For each important formula:

- provide the formula in the draft,
- explain the variables in nearby text,
- add one plain-language sentence explaining what the formula means,
- mark `formula_preview_checked: false` until the formula is checked in the final WeChat backend mobile preview.

If the formula cannot be reliably represented in the current publishing workflow, record the issue in `公式说明` and simplify the article around the concept rather than using a blurry image.

## Figure Handling

Prefer the paper's original high-resolution figures when reuse is permitted and the figure remains clear on mobile.

Use the clearest legally safe source:

- author-owned original figure export,
- author manuscript figure,
- supplementary material,
- publisher figure with confirmed reuse rights.

Redraw only when the original figure is unavailable, legally unsafe, low-resolution, or unsuitable for WeChat display.

Every figure needs:

- figure identifier from the paper, when applicable,
- source or generation method,
- copyright/reuse note,
- mobile clarity preview result,
- `figure_preview_checked: false` until final WeChat backend preview.

For a normal paper article, include several figure positions when the original paper has suitable figures. Choose figures that help readers understand:

- the method or workflow,
- the study object or geometry,
- the validation evidence,
- the final engineering or platform application.

Do not leave the article imageless unless the paper truly has no suitable figure or the user requests text-only output.

Do not commit unapproved source images. Keep private or unapproved image work under ignored local paths such as `wechat/.local/`. If image rights are not yet confirmed, include public-safe figure slots and captions in the draft, and mark the source image as pending author or reuse confirmation.

## Original Article Link

Add a `阅读原文` section near the end of the article.

For the first workflow version, use the DOI URL as the reading link. Do not imply that the repository hosts the full paper PDF unless a public author manuscript or approved download link is actually available.

## Draft Quality Gates

Before calling a draft ready:

- DOI and WOEAI publication anchor are checked.
- Research family and subdirection match `wechat/topics/`.
- No invented collaboration, partner, project, facility, award, or metric claims appear.
- Important formulas are not images and have explanations.
- The article includes suitable figure positions from the original paper when available, with source, rights, and clarity notes.
- The article includes a DOI-based `阅读原文` link.
- `wechat/templates/review-checklist.md` is satisfied or remaining items are explicitly marked for human review.
- `scripts/check-public-safe-content.py` passes.
- `./scripts/check-docs.sh` passes before claiming repository changes are complete.

Use `PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh` on this Mac if the default `python3` is older than 3.12.

## Output

When generating a draft, return:

- draft path,
- source evidence used,
- unresolved facts or human-review items,
- formula preview requirements,
- figure reuse and preview requirements,
- commands/checks run.

Do not claim the article is publish-ready until the WeChat backend mobile preview has checked formulas and figures.
