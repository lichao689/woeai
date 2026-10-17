# WOEAI WeChat Cover Standards

## Series contract: WOEAI-cover-v5

One engineering-editorial visual language, flexible horizontal composition,
fixed badge geometry and evidence-grounded science. This contract replaces the
old fixed-coordinate v2 grid and reconstructs the subsequently confirmed design
principles; it does not certify or rewrite existing covers. Migration is pending
until each actual final image is checked. These are project rules, not promises
about current WeChat platform behavior.

## Fixed invariants versus flexible composition

The final decoded canvas is **900 × 383 px**, origin at the upper left. A larger
same-ratio source is not a final export. Measure after all resizing and cropping.

| Fixed invariant | Required result on the final canvas |
|---|---|
| Direction badge | **160 × 40 px**, rounded rectangle, nominal **6 px** radius |
| Badge lettering | Nominal **24 px**, bold **700**, horizontal, upright, unskewed |
| Badge wording | Exactly one confirmed secondary-direction name from the five below |
| Confirmed text | Unchanged, complete, legible; no invented labels or extra captions |
| Scientific meaning | Evidence-grounded geometry, relationships and claims |

The badge position may change with composition, but its width, height, radius
and nominal lettering size do not scale with the subject or title. The former
128 × 40 badge is retired. The only outer-box raster tolerance is **±2 px per
dimension**, inclusive: width **158–162**, height **38–42**. It covers edge
antialiasing/raster sampling, not a larger design. The target remains 160 × 40.
For example, 161 × 40 can pass geometry; **161 × 37** and **161 × 44** cannot.
Do not introduce percentage tolerance, shrink text to force fit or enlarge the
badge to accommodate composition. If an edge cannot be reliably identified,
record uncertainty and withhold the pass rather than widening tolerance.

Use margins and an uncluttered text background appropriate to the actual image.
Prefer comfortable outer breathing room (about 24 px or more), without turning
suggested x/y positions into a rejection grid. Main title, scene, supporting
relationship and empty space can move. Compare hierarchy, balance and legibility,
not compliance with old coordinates. Make full use of the wide aspect ratio.

All lettering is horizontal and upright. Use restrained engineering illustration,
coherent perspective and clean geometry; blend text and scene with background
luminance or subdued flow, rather than dashboard cards or a hard panel divider.
Do not squeeze the main scene, evidence and technical route into a centered
square. A route is optional: show only the verified relation needed to explain
the paper, not a compulsory three-node decoration.

## Direction and palette

Use exactly these five approved secondary directions, matching the paper's
registry classification and `CONTEXT.md`. For cover scope only, this five-direction rule supersedes the old three-label
wording in historical guidance and briefs; it does not change article
prefixes, registry verification fingerprints or existing approval states. Current
article rules remain in [writing standards](../../wechat-paper/references/writing-standards.md). Those
migrations require their own authorized edits and rechecks. No arbitrary topic
tag, extra badge or legacy `漂浮风电` editorial badge. The primary research families remain
工程结构抗风 / 海洋能源结构; they are not additional cover labels.

| Direction | Text-zone base | Badge / badge text | Hook | Subtitle / publication |
|---|---|---|---|---|
| 数值风洞 | #EFF6FC | #0B6FD3 / #FFFFFF | #073B7A | #334155 / #073B7A |
| 结构抗风 | #EFF6FC | #0F766E / #D9FFF2 | #075A60 | #334155 / #075A60 |
| 一体化分析 | #062B4F | #FFC83D / #062B4F | #FFFFFF | #D9EAF7 / #D9EAF7 |
| 混凝土浮体 | #062B4F | #FFC83D / #062B4F | #FFFFFF | #D9EAF7 / #D9EAF7 |
| 数值水池 | #062B4F | #FFC83D / #062B4F | #FFFFFF | #D9EAF7 / #D9EAF7 |

The five directions retain the three established palette families, not five new
styles. Use at most one category-color title accent. Complex fields and cyan
belong to the scene, not small text on pale backgrounds. Inspect the composite:
aim for at least 4.5:1 contrast for small text and 3:1 for the large hook.

## Typography and wording

Use one modern Chinese sans-serif visual family (Noto Sans CJK SC / Source Han
Sans style) with sans-serif Latin letters. A generation request is not proof of
an embedded font. **Nominal 24 px is a font/em-size instruction, not a demand that
the raster glyph ink be exactly 24 px high.** Font design, glyphs and antialiasing
change the ink bounds. Measure and record ink separately from the badge body.

- Badge: fixed lettering specification above, centered with clear inner padding;
  four- and five-character approved directions share the same outer dimensions.
- Hook: target 48 px extra-bold with about 54 px line height; preferably 6–12,
  maximum 14 full-width character equivalents, at most two lines. Preserve
  abbreviation integrity. Adjust line breaks/composition before shrinking text.
- Subtitle: target 24 px medium, one line, up to 15 full-width equivalents; add a
  method or condition instead of repeating the hook. Omit only if approved.
- Publication: exact verified public journal name and year, target/minimum 18 px,
  up to two lines at word boundaries. No invented abbreviations. If either is
  unavailable, omit and record why. If confirmed wording cannot fit legibly,
  request a text/layout decision rather than silently changing it.
- Only badge, hook, subtitle and publication line contain text. No DOI, authors,
  fake chart values, labels, figure numbers, slogans, invented logos or watermarks.

## Science and evidence gate

Read the audited article and source evidence before selecting a visible object.
Record source section/figure anchors for each structure, comparison and claim.
Distinguish diagrammatic illustration, simulation, physical experiment and real
application. A potential use is not a validated deployment.

Represent actual geometry and mechanics. In floating-platform illustrations,
verify columns, pontoons, braces/rods and connections before drawing them; visual
symmetry or plausibility does not establish their existence. Concrete/steel
material contrast must not invent a structural layout difference. A center-of-
gravity marker or arrow needs a verified definition/location and comparison;
"lower center of gravity" cannot be inferred from material or mass alone.

Wave, displacement or response-amplitude comparisons need the same defined
quantity, conditions and source evidence. Decorative waves or curves must not
imply measured damping, smaller amplitude, superiority or numerical improvement.
Where evidence is missing, remove that claim/graphic or simplify to the verified
object. Do not fill space with fictitious rods, CG markers or result curves.
Paper figures are evidence/inspiration, not a default collage; reuse rules remain
in `project/guides/paper-sources-and-evidence.md`.

## Badge measurement gate

Inspect the **actual final image** and record a measurement tied to its SHA-256.
A requested rectangle, generated description or prompt saying "160 × 40" is not
a measurement. Crop/resize/repair creates a new artifact and invalidates old QA.

1. Decode and check the final canvas. Identify the complete badge body using its
   visible fill, excluding shadows/halo. Record outer bounds as
   `[x0, y0, x1, y1)` (right/bottom exclusive), width and height.
2. Measure the actual glyph ink independently. Record its bounds and ink height,
   plus padding/containment. Ink must remain clearly inside the badge and legible;
   its measured height is not the nominal font size. Report nominal-size evidence
   separately: known rendering settings when available, otherwise visual target
   review with uncertainty. Never report a font-size measurement from ink height.
3. Use `../scripts/measure_badge.py` for flat, separable palette-colored badges
   (run from the repository root using its full skill path). It detects pixels
   inside a generously padded search region; that region is not the measured box.
   Use `--roi X0 Y0 X1 Y1 --palette offshore` (or `numerical` / `structural`)
   and `--output REPORT.json`; consult `--help` for details. Keep the machine JSON
   in ignored QA storage keyed to the final image hash, not beside public assets.
   Inspect the reported bounds against the image before accepting geometry.
4. The helper rejects wrong canvas, absent/ambiguous/clipped detection and an
   outer box outside 158–162 × 38–42. It is not OCR and does not verify wording,
   nominal font/weight, radius, visual quality, science or backend support.
   Review the 6 px corner-radius target (allow at most ±1 px raster edge
   uncertainty), text, padding and all other invariants separately. If color
   segmentation is unreliable, record a pixel-inspected/manual measurement with
   annotated boundaries, method and uncertainty; no automatic pass or made-up
   precision. An unresolved edge or out-of-tolerance box remains rejected.
5. Geometry pass alone does not pass the cover. Record separate geometry, wording,
   typography/radius, science, horizontal composition and backend review states.
   Missing measurement, oversized badge or any other failed invariant overrides
   candidate score averages and prevents delivery as a corrected final.

The helper is read-only on the source raster. It is not a deterministic badge
renderer and does not authorize overlays. Existing generation/edit permissions
and the bounded-repair rule in the skill still apply.

## Horizontal-first review and crop diagnostics

Review in this order:

1. Full 900 × 383: exact words, science, proportions, badge measurements,
   hierarchy, contrast and horizontal balance.
2. 360 px wide mobile approximation: readable hook/subtitle, useful main subject
   and provenance hierarchy. 120 px wide: recognizable subject/identity, not a
   promise that every line is readable.
3. Optional center-square and 5:4 diagnostics: record what is lost and whether
   that would matter on an actual supported surface. The 900 × 383 center square
   spans x = 258.5–641.5. This is crop geometry, not a required composition core.
   Losing peripheral information in this hypothetical square alone does not
   reject a good wide cover or require all scientific content to move centrally.
4. Series comparison: consistent type hierarchy, badge size, palette family and
   rendering language, not identical coordinates for every paper.
5. Actual WeChat backend/mobile preview: verify current crop controls and the
   result on the intended surface. Record date, surface and observed behavior.
   Do not assert that a custom square crop or separate square asset is supported
   without checking. If square delivery is required but unsupported/unverified,
   state that blocker and resolve it explicitly; do not silently harm the wide
   cover. A separate square asset is a separately scoped deliverable.

`cover_preview.py` creates a diagnostic board only. Dimensions and preview
success certify neither visual compliance nor platform behavior. Keep
`cover_image_checked: false` until the actual backend mobile preview is checked.
No credential access or remote update is implied by local QA.

## Evidence record and completion

Use the paired brief template to keep confirmed words, approved direction,
actual tools, file/hash, measured boxes, rejected attempts, strategy changes,
visual review and backend review distinct. Keep detailed reports/experiments in
ignored private storage and public notes free of private paths and identifiers.
Guidance updates preserve historical approvals and mark existing assets
migration-pending, never retroactively passed. Report failed, blocked, pending
and not-run gates honestly.
