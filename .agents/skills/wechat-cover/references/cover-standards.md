# WOEAI WeChat Cover Standards

## Series contract: WOEAI-cover-v2

Use one design system across papers. Change the scientific subject and confirmed
wording, not the layout, typography, rendering language or arbitrary palette.
Retain the three existing direction color families below. This is a project
specification, not a platform-wide promise. Verify actual WeChat backend crops
before release; change the series contract as a whole if requirements change.

## Canvas and fixed grid

Coordinates refer to a final **900 × 383 px** canvas, origin at upper left.
Larger sources must preserve these proportions. A matching ratio alone does not
meet the final export requirement. Inspect actual dimensions, not filenames.

| Element | Fixed bounds / treatment |
|---|---|
| Outer safe area | x = 36–864; y = 24–359; essential text stays inside |
| Integrated text zone | x = 36–396; width 360; low-detail shared background |
| Direction badge | x = 36, y = 28; 128 × 40; −4° tilt; 6 px corner radius |
| Main hook | x = 36, y = 84; width 360, height 108; at most two lines |
| Subtitle | x = 36, y = 200; width 360, height 30; one line |
| Publication line | x = 36, y = 238; width 360, height 44; at most two lines |
| Scientific scene | x = 420–864; y = 28–280; one dominant object |
| Crop-critical subject | diagnostic object inside x = 420–620, y = 56–276 |
| Technical route | x = 36–864; y = 290–359; three sparse nodes and two arrows |

Blend text and scene through a soft luminance gradient, shared geometry or
subdued flow lines. No hard divider, white card, curved panel border or glowing
UI frame. Use a restrained engineering editorial illustration, coherent
perspective and clean geometry. Do not alternate cartoons, photographs, neon
science fiction and dense dashboards across papers. Scene/method/application
candidates change subject emphasis within the same grid, not the design system.

## Typography and text budget

Use one modern Chinese sans-serif family throughout: Noto Sans CJK SC / Source
Han Sans visual style, with sans-serif Latin characters. These are generation
visual targets, not a claim that a font file is embedded. Target the sizes below;
visual tolerance up to 10% does not relax any box, line-count or text-budget
limit. Never shrink the whole title to fit or accept overflow.

- Badge: 24 px, bold 700; exact four-character category.
- Hook: 48 px, extra-bold 800, 54 px line height; preferably 6–12 full-width
  character equivalents, maximum 14; at most seven per line, two lines total.
  Count punctuation/Latin width in the actual fit; never break an abbreviation.
- Subtitle: 24 px, medium 500, 30 px line height; at most 15 full-width character
  equivalents. Add a method or condition rather than repeat the hook.
- Publication line: 18 px, semibold 600, 22 px line height. Use the exact public
  journal name plus ` · <Year>`; wrap at a word boundary into two lines. Do not
  invent abbreviations. The 18 px minimum is strict, including font tolerance.
  If it cannot fit, stop for a reviewed layout/text decision.
- Only these four elements may contain text. No DOI, authors, impact factors,
  fake chart values, UI labels, figure numbers, added slogans or translations.
- No logo or watermark by default, including invented WOEAI/publisher marks.
  An explicitly requested authorized logo needs a reviewed series-wide revision,
  not a one-paper placement improvisation.
- Confirmed wording takes priority over a suggested length: if it cannot fit,
  ask for revised text. Do not silently shorten it or remove the subtitle.
- Derive journal/year only from verified public metadata. Omit this line when
  either is unavailable, and record why; do not invent a source or date.

## Fixed palette

Keep the shared grid and typography identical across directions. Only the
following established category tokens differ. Use the base under text; confine
complex scientific color fields and lighting to the scene.

| Category | Text-zone base | Badge / text | Hook | Subtitle / publication |
|---|---|---|---|---|
| 数值风洞 | #EFF6FC | #0B6FD3 / #FFFFFF | #073B7A | #334155 / #073B7A |
| 结构抗风 | #EFF6FC | #0F766E / #D9FFF2 | #075A60 | #334155 / #075A60 |
| 漂浮风电 | #062B4F | #FFC83D / #062B4F | #FFFFFF | #D9EAF7 / #D9EAF7 |

Use at most one hook accent: numerical blue #0B6FD3, structural teal #0F766E,
or offshore yellow #FFC83D. Cyan #00A6D6 belongs to the scene, not small text on
pale backgrounds. Check the final composite, not just token colors: aim at
least 4.5:1 for small text and 3:1 for the large hook. Dark-ocean publication
metadata must stay pale, never deep blue on dark blue.

## Scientific meaning and evidence

Read the audited article and review before choosing visual elements. The three
route nodes show verified input → method → output. Do not present a potential
engineering use as an experimentally demonstrated result or deployed project.
Record paper-section/figure anchors for the object, method and output. Missing
evidence stays pending; do not invent plausible geometries or research detail.

Do not generate quantitative result curves, numerical improvements or benchmark
wins without evidence. An unlabelled abstract curve must not imply a measured
trend. Paper figures are evidence/inspiration, not default cover collages.
Original figure extraction, reuse rights and public-safety rules in
`wechat/STYLE.md` still apply. Never alter scientific figures to manufacture
results, and do not expose private sources or project branding.

## Execution and confirmation

A skills/specification/brief-only maintenance request does not request image
generation. Preserve selected assets, text confirmations and backend history;
record migration pending instead of claiming old covers satisfy this contract.
For actual cover production:

1. Read this contract, the audited article and review; use
   `wechat/templates/cover-brief.md` for the paired brief.
2. Default to `image-gen`; use `prompt-only` only when the user explicitly asks
   for prompts without image generation. Do not ask a redundant mode question.
3. Present five concrete `category | hook / subtitle` choices plus custom text;
   obtain the exact choice before new generation or complete prompt output.
   Existing confirmation records are not permission to silently change words.
4. For `image-gen`, generate three candidates (scene, method, application) within
   this same grid, with confirmed text generated inside the image. Reject wrong,
   missing, extra or illegible text. Retry one round with unchanged words; after
   two failed rounds ask for shorter/clearer confirmed text. Do not fall back to
   no-text covers or post-generation text overlays.
5. For `prompt-only`, deliver exactly three complete prompts labelled
   `提示词 1｜研究场景`, `提示词 2｜方法机制`, `提示词 3｜工程应用`.
   Start with selected wording, put file/check summaries after the prompts, and
   do not generate images, run previews or update drafts in this mode.
6. Default to English prompt instructions with exact quoted Chinese words;
   use Chinese prompts when requested. Each delivered prompt must be standalone:
   spell out canvas/grid, font scale, category hex colors, confirmed text,
   verified journal/year when available, three evidence-based route nodes,
   crop core and prohibited elements. Do not leave placeholders or “same as above”.

## Acceptance and crops

A center-square crop of 900 × 383 covers x = 258.5–641.5 (42.56% of its width).
It cannot retain the whole left-aligned title. The square must preserve the
recognizable diagnostic object; the wide cover carries the complete words.
A dedicated square asset is a separate scoped deliverable.

Inspect each surface:

- Full 900 × 383: exact text, science, composition, scale and palette.
- 360 × 153 wide mobile approximation: readable hook/subtitle and decipherable
  secondary provenance. Shorten through confirmation if necessary, not shrinking.
- 120 × 120 center square: recognizable diagnostic subject; tiny metadata is
  not expected to be readable.
- Center 5:4 crop: subject survives without misleading partial results.
- 120 px wide thumbnail: recognizable visual identity and dominant subject;
  do not claim every text line can be read at this size.
- Side-by-side with two series covers: same grid, type scale and rendering
  language, with only the category token differences allowed above.

Run the skill's `scripts/cover_preview.py` with candidate labels and optional
scores. It measures dimensions/ratio/file size and previews the full source and
common crops; it does not certify text, science, contrast or backend behavior.
Score specificity, subject clarity, engineering credibility, readable hook,
crop survival and exact text from 1–5; do not default to full marks. Any incorrect
text, unsupported result or missing crop-critical object rejects a candidate
regardless of its average score.

Store public-safe final assets under `wechat/assets/public-safe/<ref>/` and
experiments/previews in ignored local storage. Record confirmed words, sources,
candidates, rejections, selected path, measured dimensions, contract version,
evidence anchors, local checks and backend checks separately. Set
`cover_image_checked: true` only after an actual WeChat backend mobile preview.
A specification update, matching dimensions or local preview is not acceptance.
