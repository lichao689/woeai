# Homepage progress card completeness repair

Status: local implementation reviewed; the user subsequently explicitly authorized submission to main and site deployment after successful tests and independent review.
Base: fdbf5380886ba2cba5f4094e4c452ee03e92c77c.
Environment: existing primary checkout on lcMacM4.local; inherited model route.

## Request and acceptance

The selected paper ref-zheng2025-QHDXXB (the central/offset semi-submersible model-test paper) must explain its research problem and contribution in both homepage languages. All displayed papers, including future additions, must have nonempty, non-placeholder copy and traceable sources. Missing copy must stop generation/build instead of showing a partial card, inventing from the title, or selecting a replacement. Preserve qualification filtering before publication-date sorting and at most three per family, six current papers, full citations, unique covers, and the approved laboratory layout. Do not modify WeChat or rewrite the registry.

Additional authorized wording: Chinese hero gains the explicit environmental qualifier in the wind/ocean actions statement; the directly corresponding English statement gains environmental. No other slogans change.

## Diagnosis

The selection fix in 4e4148c admitted the already-produced and reviewed QHDXXB paper instead of the unproduced CSICM paper. The five-entry home-progress.json was not extended. render_home_progress used an empty-dict annotation fallback, a bibliography-title fallback and an if-copy block that omitted both paragraphs. Prior tests asserted selection, citations, links and covers, but not each card's explanatory paragraphs. An older test deliberately allowed the then-unproduced CSICM card to omit these paragraphs; the permissive rendering remained when selection was corrected. The new real-data regression fails in both languages on the original implementation.

## Minimal implementation

- Add bounded QHDXXB bilingual copy based on the existing reviewed introduction and evidence review; no new PDF audit is claimed.
- Require both languages' heading/problem/contribution and a same-paper reviewed public introduction with real nonempty second-level section locators for problem and contribution. Apply this after unchanged eligibility/ranking to every displayed row.
- Eliminate empty annotation/title fallback and conditional omission. Errors identify publication_ref and field. Chinese artifact generation validates English copy too.
- Add per-claim section locators for the other five unchanged summaries; evidence metadata stays out of public card markup.
- Update the homepage guide, generated Chinese marker block and relevant regressions.

## Scientific evidence

QHDXXB sources: wechat/articles/draft-public-safe/ref-zheng2025-QHDXXB.md and its existing public review. The reviewed source identifies the same DTU 10-MW turbine, 1:70 complete-system wind-wave tests and two representative operating/survival sea states. Review evidence locates the model at PDF file page4, experiment conditions at pages4-5, motions at pages7-8, turbine response at pages8-10 and limitations at page12. The two complete platform/mooring designs differ beyond turbine position; the card explicitly retains that limitation. It claims no universal winning design, isolated causal offset effect or full-life experimental validation.

All six cards' problem/contribution source sections are recorded in docs/data/home-progress.json. Existing five summaries retain their exact wording. Their cited sections support geometry generation vs wind-field accuracy (BE), tank frequency/damping rather than whole-structure performance (He OE), the precomputed CFD database/measurements/WebGIS (BS), concrete conceptual system design with local-detail limits (He structural), and equivalent-load target/accuracy/effort trade-offs (Zheng OE).

## Regression seams and release boundary

Use the shared render_home_progress public interface with current real data and fresh reviewed future-paper fixtures, plus existing artifact CLI and strict Sphinx gate. Test missing entry/language/fields, empty/invisible/placeholder text, invalid same-paper provenance/section locators, legitimate prose, and a new top-three paper without copy (must fail, never replace with the fourth). Preserve existing eligibility, date, cover, citation and layout tests. Inspect local Chinese/English desktop/mobile output.

Independent Spec and Standards reviewers assess the exact aggregate diff against the base and this request. Save local test/review/browser evidence under the existing ignored outputs directory. Public submission and deployment are explicitly authorized after successful validation and independent review.
