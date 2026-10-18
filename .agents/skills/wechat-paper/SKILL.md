---
name: wechat-paper
description: Create or revise a source-backed WOEAI WeChat paper introduction, review evidence and offline preview. Use the bundled writing standards and templates; RTD deep dives and covers remain independent tasks. Live draft delivery requires separate explicit authorization.
---

# WeChat paper workflow

## Read the relevant authority

| Need | Read |
| --- | --- |
| Project boundaries, terminology | [AGENTS.md](../../../AGENTS.md), [CONTEXT.md](../../../CONTEXT.md) |
| Writing rules (one authority) | [references/writing-standards.md](references/writing-standards.md) |
| Natural writing and pinned licensed reference | [references/natural-scientific-writing.md](references/natural-scientific-writing.md) |
| Sources and fact evidence | [paper-sources-and-evidence.md](../../../project/guides/paper-sources-and-evidence.md) |
| Body / review / checklist scaffolds | [paper-explainer.md](templates/paper-explainer.md), [paper-review.md](templates/paper-review.md), [review-checklist.md](templates/review-checklist.md) |
| Rendering, credentials, draft delivery | [wechat/README.md](../../../wechat/README.md) |
| Runtime when needed | [cloud-wechat-workflow.md](../../../project/guides/cloud-wechat-workflow.md) |
| Covers (only if requested) | [wechat-cover](../wechat-cover/SKILL.md) |
| Independent RTD work | [paper-deep-dive-rst.md](../../../project/guides/paper-deep-dive-rst.md) |

## Execute only the authorized stage

1. Check workspace changes and the registry's selection, paper identity and existing evidence.
2. Read authorized sources and make a fact/evidence card. For editorial revisions, identify which
   existing source audit is being reused; never relabel it as a new PDF audit. Missing necessary
   sources stop the dependent work. Do not read credentials or contact WeChat during content work.
   Before drafting, fill the existing engineering narrative evidence card in
   [paper-review.md](templates/paper-review.md), including the main reader and reading goal.
   Review the original figures against that argument and fill the existing image-use record
   with their evidence roles and selection/omission reasons, following writing standards section 7.
3. Draft or revise using the bundled body template and writing standards. Keep the front problem
   section distinct from the engineering-value ending. Merge the old closing prose as needed;
   retain important conditions beside their evidence, original figures, abstract and final AI line.
   Use the card's argument to plan and check the prose, not to impose fixed sections.
   Place selected figures where the argument needs them; the body template's sample image group
   does not limit their number. Introduce what to inspect before each figure and explain the finding
   and its place in the argument afterward, separately from the caption.
4. Apply the natural-writing workflow and checklist. Record the engineering-value argument,
   source-backed potential uses, editorial inferences and retained scientific conditions in a
   separate language review when preserving historical audit records.
5. Check the selected article(s), render offline and inspect the result. With an already available
   runtime, run from the repository root:

   ```bash
   python3 scripts/check-public-safe-content.py
   python3 scripts/check-wechat-content.py wechat/articles/draft-public-safe/<publication_ref>.md
   python3 wechat/tools/wechat_draft.py preflight --publication-ref <publication_ref> --theme academic-clean
   git diff --check
   ```

   For related reading, verify same-account publication records before selecting links; inspect
   the assembled navigation as well as the source, with the AI statement still last. Missing
   publication evidence means omit the optional section, never invent a URL or publication state.
   Structure checks do not assess the semantic value/condition balance. Preflight needs existing
   upload approvals; report missing approvals without inventing fields. It does not read credentials,
   contact WeChat or update drafts. Setup, full-site builds and live diagnostics are separate scopes.
6. Report files, evidence, rendered checks, pending reviews and fingerprint impact. Writing-standard
   changes invalidate old WeChat evidence; keep the old receipts and re-review rather than rehashing
   them as approved. RTD text and evidence stay independent. Never call offline preview phone acceptance.
7. Only on explicit live create/update authorization, follow the delivery guide's credential,
   approved-asset and target-draft procedure. Do not publish or mass-send; a human publishes after preview.
