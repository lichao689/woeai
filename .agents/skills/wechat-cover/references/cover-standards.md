# WOEAI WeChat Cover Standards

## Current Default

- Default first-cover size: `900 x 383 px`.
- Default ratio: about `2.35:1`.
- Treat this as current design guidance, not a permanent platform contract.
  Recheck the WeChat backend or current documentation before hard-coding future
  dimensions.

## Crop Safety

Keep the main visual subject in the center. The local preview checks:

- full `2.35:1` cover,
- center square crop,
- `5:4` share-card-like crop,
- small thumbnail,
- approximate center safe area.

These are first-pass checks only. The final approval surface is the WeChat
backend mobile preview.

## Candidate Concepts

Generate at least three directions for each paper:

1. Research scene: the physical or engineering system.
2. Method: the model, simulation, database, algorithm, or workflow.
3. Engineering impact: how the work supports decisions, platforms, or practice.

For each direction, either generate image-gen-text candidates in `image-gen`
mode or write full image-generation prompts in `prompt-only` mode. Each final
cover must contain the exact user-confirmed cover text generated directly in the
image.

## Execution Modes

The default execution mode is `image-gen`: generate cover-image candidates
directly through image generation.

The alternate execution mode is `prompt-only`: output exactly three complete
image-generation prompts, one each for the research scene, method, and
engineering impact directions. In this mode, do not call image generation,
create image files, run crop preview, or update a WeChat draft.

Use `prompt-only` only when the user's request explicitly says to generate only
prompts or not generate images. Use `image-gen` for all other cover-generation
requests, including when the request does not name an execution mode. Do not ask
a separate execution-mode question.

The execution-mode rule does not replace text confirmation. Both modes still
require the five cover-text options plus one custom-text option before image
generation or prompt-only output.

## Prompt-Only Chat Output

After the user confirms a cover-text option number in `prompt-only` mode,
produce exactly three complete prompts and make them the visible center of the
reply.

- Begin with a single concise confirmation line naming the selected text.
- Label the prompts in Chinese:
  `提示词 1｜研究场景`, `提示词 2｜方法机制`, and
  `提示词 3｜工程应用`.
- Write each prompt as a normal wrapped paragraph or block quote, not a fenced
  code block, unless the user explicitly asks for code-block copy boxes.
- Do not output abbreviated prompt previews, placeholder fragments, "same as
  above", or "see file".
- Put any file-update or check summary after the three prompts, not before.

## Text Policy

Use cover text only when it improves click appeal and remains readable as a
thumbnail.

User confirmation is required before generating any cover candidate or
prompt-only output. The agent should offer exactly five concrete cover-text
combinations plus one custom-text option. The five generated combinations
should each be ready to use on the cover. The selected option becomes the
source of truth for image-generation prompts.

Preferred structure:

- category tag: `数值风洞`, `结构抗风`, or `漂浮风电`;
- main hook: preferably 6-12 Chinese characters;
- subtitle: short, concrete, and one or two sizes smaller than the hook.

Do not repeat the full article title. Let the WeChat title field carry the
complete wording. Omit the subtitle only when the user explicitly confirms a
no-subtitle variant for readability.

## Cover Text Layout

Use the same main text hierarchy for all WOEAI WeChat paper covers:

1. Category tag.
2. Main hook.
3. Subtitle.
4. Derived publication metadata line, when journal and year are available.

The prompt must describe the text layout as a fixed editorial design system,
not as loose text decoration:

- wide `2.35:1` cover composition;
- left `38-45%` integrated text-safe zone with low visual detail;
- right `55-62%` article-specific engineering visual;
- the text-safe zone must blend into the same full-cover background using a
  soft luminance gradient, atmospheric haze, subtle wind lines, or shared
  geometry;
- no obvious vertical divider, hard color wall, white card, curved border, or
  high-contrast seam between the text zone and the visual zone;
- text readability should come from local brightness, contrast, blur, and
  reduced detail behind the text, not from a separate rectangular panel;
- category tag in a rounded pill at the upper-left of the text panel;
- main hook below the tag, oversized, bold, high contrast, and visually
  dominant;
- subtitle below the hook, one or two sizes smaller, readable but secondary;
- publication metadata line below the subtitle, left-aligned with the subtitle,
  when journal and year are available;
- text must not overlap complex wind streamlines, waves, buildings, equipment,
  data frames, or dense backgrounds.

## Bottom Technical Route Strip

Every WOEAI paper cover should include a bottom technical route strip that
compresses the paper's implementation path into a visual sequence. This is a
cover-level schematic, not a reproduction of a dense paper figure.

Use the strip to show the paper-specific route from input or problem, through
method, to output or engineering use:

- place it across roughly the lower `18-25%` of the cover;
- keep it visually connected to the main scene through the same palette,
  lighting, perspective, or flow lines;
- use small panels, arrows, simplified model/data blocks, engineering
  components, response curves, field snapshots, or validation/result cues;
- choose route elements from the article's actual method and evidence, such as
  inflow statistics to feedback control to LES domain to wind-pressure field,
  low-resolution snapshots to sparse attention to high-resolution wind frames,
  turbulence cube to coherence-preserving inflow to urban CFD, or structure to
  TLD geometry to response curve;
- keep the strip sparse and readable in a small thumbnail;
- do not use extra text labels by default, because image models often invent or
  distort small labels. Express the route through icons and schematic forms
  unless the user explicitly confirms a labelled route strip.

Only the confirmed three main text elements plus the derived publication
metadata line may appear on the cover. Do not add English translations, fake
chart labels, UI labels, map labels, figure numbers, decorative captions, logos,
watermarks, or small unreadable annotations.

## Publication Metadata Line

Add a publication metadata line by default when the public article source or
review metadata contains both journal name and publication year.

- format: `<Journal Name> · <Year>`, for example
  `Renewable Energy · 2026`;
- source: the article's public `期刊` and `年份` metadata;
- role: secondary scholarly provenance, not a marketing badge and not a second
  category tag;
- placement: directly below the subtitle in the integrated text-safe zone,
  left-aligned with the subtitle;
- typography: semi-bold deep-blue modern sans-serif text, about `65-75%` of the
  subtitle size;
- visibility: readable at phone thumbnail size while clearly secondary to the
  subtitle;
- avoid: leading dot, icon, enclosing badge, capsule, button-like outline, DOI,
  author names, volume, issue, page range, impact factor, quartile, or other
  publication metrics.

## Direction-Specific Text Styles

Keep the three directions visually related through the shared left text panel,
rounded category pill, oversized hook, and smaller subtitle. Differentiate them
through palette, contrast, and support graphics:

`数值风洞`:

- text zone: white to pale blue, bright and clean, blended into the same
  engineering scene rather than separated by a hard panel edge;
- category pill: strong blue background with white text;
- main hook: deep navy blue;
- subtitle: dark gray or blue-gray;
- support accents: cyan-blue glowing data frames, satellite/image thumbnails,
  grid or geometry panels, wind streamlines, or CFD contour cues;
- use when the story is about numerical wind tunnels, CFD, urban geometry,
  turbulence, inflow, WebGIS, or visual-data-to-CFD workflows.

`漂浮风电`:

- text zone: integrated with a darker ocean-engineering background, still
  clean enough for text;
- category pill: yellow or amber background with deep blue text;
- main hook: mostly white, with at most one important keyword in yellow;
- subtitle: light blue or pale cyan;
- support accents: wave-line layers, response curves, coordinate axes, platform
  comparison cues, offshore wind turbines, mooring or semi-submersible forms;
- prefer curve or wave accents over photo thumbnail frames.

`结构抗风`:

- text zone: white to pale blue city or building atmosphere, blended into the
  same structural scene rather than separated by a hard panel edge;
- category pill: strong blue background with white text;
- main hook: deep navy blue;
- subtitle: dark gray or blue-gray;
- support accents: wind-flow bands, building silhouettes, high-rise structures,
  TLD water, sloshing, vibration-response cues, or GNN/monitoring nodes;
- avoid generic city-poster styling; keep the visual tied to structural wind
  response or vibration control.

Reject image-gen-text candidates when:

- any Chinese character is wrong, distorted, missing, or hard to read;
- the model rewrites, omits, translates, or adds to the confirmed cover text;
- contrast is too low on the full cover or thumbnail;
- text competes with the main visual subject;
- fake UI labels, fake map labels, or misleading claims appear.

If all candidates in a round fail, retry once with the same confirmed text. If
two rounds fail, stop and ask the user to confirm shorter or clearer cover text.
Do not switch to a no-text cover or add text after generation.

## Title Category Cues

`数值风洞`:

- urban blocks,
- CFD grids,
- wind streamlines,
- turbulence or inflow,
- contour fields,
- validation points,
- database or WebGIS layers.
- visual-data-to-CFD geometry workflows.

`结构抗风`:

- high-rise structures,
- wind pressure and load paths,
- vibration control,
- monitoring data,
- optimization,
- structural response.
- GNN nodes or response prediction cues.

`漂浮风电`:

- floating offshore wind platforms,
- wind-wave-current loading,
- mooring and coupled response,
- platform structure,
- offshore environment,
- system-level optimization.
- structural feasibility or cost/response tradeoff cues.

## Quality Rubric

Score each candidate from 1 to 5:

- article specificity,
- main-subject clarity,
- click appeal,
- engineering credibility,
- small-thumbnail readability,
- crop safety,
- text quality, when text is present.

Use these scores to compare candidates; do not average them blindly. A cover
with unreadable text, generic AI wallpaper, or a weak main subject should be
rejected even if its dimensions and file size pass.

## Prompt Template

Use an English prompt body for image generation by default, while keeping the
confirmed Chinese cover text exact and quoted. Most general image models follow
composition, lighting, layout, and style cues more reliably in English; the
cover text itself must remain Chinese. If the user says the target image model
is Chinese-first, or explicitly asks for Chinese prompts, write the prompt body
in Chinese while preserving the same structure and exact quoted cover text.

Split the confirmed cover text into:

- `<category tag>`: one of `数值风洞`, `漂浮风电`, or `结构抗风`;
- `<main hook>`: the main short hook;
- `<subtitle>`: the short subtitle. Omit only when the user explicitly confirmed
  no subtitle for readability.
- `<journal name>`: the journal name from the article's public `期刊` metadata;
- `<publication year>`: the year from the article's public `年份` metadata;
- `<publication metadata line>`: `<journal name> · <publication year>`, omitted
  only when either journal name or year is unavailable.

```text
A technically credible editorial cover image for a WOEAI WeChat article about
<paper topic>. Show <main visual subject>. Include <method or data cue>.
Use a clean modern academic engineering magazine style and a wide 2.35:1
composition. Keep the left 38-45% as a clean, low-detail integrated text-safe
zone and reserve the right 55-62% for the article-specific engineering visual.
Blend the text-safe zone into the same full-cover background with a soft
luminance gradient, atmospheric haze, subtle wind lines, or shared geometry.
Do not create an obvious vertical divider, hard color wall, white card, curved
border, or high-contrast seam between the text area and the visual area. Text
readability should come from local brightness, contrast, blur, and reduced
detail behind the text.

Add a bottom technical route strip across roughly the lower 18-25% of the
cover. Use small schematic panels, arrows, simplified model/data blocks,
engineering components, curves, or field snapshots to show <paper-specific
implementation path from input/problem to method to output/application>. Keep
the strip visually connected to the main scene and readable in a small
thumbnail. Do not add extra text labels in the strip unless the user explicitly
confirmed a labelled route strip.

Use exactly three Chinese text elements on the left panel, in this order:
1. a rounded pill category tag: "<category tag>";
2. an oversized bold main hook: "<main hook>";
3. a smaller subtitle below: "<subtitle>".

Below the subtitle, add one publication metadata line:
"<publication metadata line>". Use semi-bold deep-blue modern sans-serif text,
no leading dot, no icon, no enclosing badge, no capsule, no button-like outline.
Keep it readable at phone thumbnail size and clearly secondary to the subtitle.

Apply the direction-specific WOEAI text style for <category tag>: <direction
text style>. Keep the Chinese characters crisp, complete, high-contrast, and
unchanged. Do not add any other text, English translation, fake chart labels,
map labels, UI labels, logos, watermarks, or decorative small captions. No
people unless needed.
```

Add article-specific avoids:

- no generic city skyline,
- no decorative abstract technology wallpaper,
- no distorted Chinese text,
- no missing, rewritten, translated, or extra cover text,
- no unrelated lab scene,
- no private partner or project branding.
- no fake software UI, fake map label, or fake publication claim.

## Review Note Fields

Record cover information in `wechat/articles/review/<publication_ref>.review.md`
or a paired cover brief:

- cover status,
- selected execution mode: `image-gen` or `prompt-only`,
- candidate count or prompt count,
- selected candidate ID, when applicable,
- user-confirmed cover text choice,
- selected text mode: `image-gen-text`,
- prompt-only output count and complete prompt texts, when applicable,
- rejected candidate reasons,
- source candidate path, when applicable,
- final cover path, when applicable,
- dimensions, when applicable,
- generation tool,
- prompt or design brief,
- quality scores,
- local crop preview path, when applicable,
- backend preview state.
