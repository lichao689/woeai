# ref-tang2026-RE 封面简报

- 文章标题: 数值风洞 | 如何高效重建城市风能中的高时间分辨率风场
- 分类标签: 数值风洞
- 封面短钩子: 风场超分辨
- 副标题: 城市风能应用
- 目标读者: 关注 WOEAI 论文、城市风能、数值风洞、湍动入流和 AI 代理模型的公众号读者
- 避免: 私密项目名称、未确认合作方、复杂小字、虚构 UI 标签、夸张宣传语

## 候选方向

1. research scene: 城市建筑群上方的风场快照序列，从稀疏低时间分辨率帧过渡到连续高时间分辨率湍流演化，右侧可出现半透明城市街区、风机剪影和蓝青色速度等值面。
2. method: WTT-SRST 的稀疏窗口注意力与时序超分辨映射，用分层窗口、stride 采样节点、低分辨率输入帧到高分辨率输出帧的流程感表达方法贡献，避免真实 UI 标签。
3. engineering impact: 面向城市风能调度和风资源评估的加速数值风洞场景，用高时间分辨率风场、功率谱/相干性抽象曲线和节能计算意象表达“更快、守物理、可应用”。

## 本轮提示词生成

- cover_execution_mode: `prompt-only`
- cover_text_confirmation: user-confirmed
- confirmed_cover_text: `数值风洞 | 稀疏快照补全风场 / 看见湍流时间细节`
- confirmed_text_mode: `image-gen-text`
- prompt-only output count: 3
- confirmation_note: confirmed in chat
- prompt-only outputs:
  1. research scene prompt:
     A technically credible editorial cover image for a WOEAI WeChat article about temporal super-resolution of wind fields in urban wind energy applications. Show an urban district with simplified building blocks and a few small wind-energy devices near rooftops or open urban edges, with blue-cyan CFD-like wind contours and streamlines evolving from two sparse low-temporal-resolution snapshots into a continuous sequence of high-temporal-resolution turbulent wind-field frames. Use a clean modern academic engineering magazine style and a wide 2.35:1 composition, target 900 x 383 px. Reserve the left 38-45% as a clean, low-detail white-to-pale-blue text-safe panel and reserve the right 55-62% for the article-specific engineering visual. Keep the main wind-field sequence centered enough for square and share-card crops.

     Use exactly three Chinese text elements on the left panel, in this order: 1) a rounded strong-blue pill category tag: "数值风洞"; 2) an oversized bold deep-navy main hook: "稀疏快照补全风场"; 3) a smaller dark gray or blue-gray subtitle below: "看见湍流时间细节". Keep the Chinese characters crisp, complete, high-contrast, and unchanged. Add subtle cyan-blue data-frame accents near the text panel edge, but do not place text over wind streamlines. Do not add any other text, English translations, fake chart labels, map labels, UI labels, logos, watermarks, or decorative small captions. Avoid generic city skyline, abstract AI wallpaper, unrelated lab scenes, private partner branding, distorted Chinese text, missing or rewritten cover text.

  2. method prompt:
     A technically credible editorial cover image for a WOEAI WeChat article about WTT-SRST, Sparse Window-based Attention, and temporal super-resolution mapping for turbulent urban wind fields. On the right side, visualize the method as an abstract but engineering-plausible flow: two low-resolution wind-field snapshot tiles enter a layered sparse-window attention structure with window grids, stride-sampled nodes, shifted-window connections, and then expand into multiple high-temporal-resolution wind-field frames with coherent blue-cyan turbulence patterns. The visual should feel like a numerical wind-tunnel workflow, not a software screenshot. Use a clean modern academic engineering magazine style and a wide 2.35:1 composition, target 900 x 383 px. Reserve the left 38-45% as a clean, low-detail white-to-pale-blue text-safe panel and reserve the right 55-62% for the method visual.

     Use exactly three Chinese text elements on the left panel, in this order: 1) a rounded strong-blue pill category tag: "数值风洞"; 2) an oversized bold deep-navy main hook: "稀疏快照补全风场"; 3) a smaller dark gray or blue-gray subtitle below: "看见湍流时间细节". Keep the Chinese characters crisp, complete, high-contrast, and unchanged. Use cyan-blue glowing data frames, clean grid geometry, sparse attention nodes, and wind-field contour cues. Do not add formulas, percentages, English labels, fake UI panels, fake chart labels, map labels, logos, watermarks, or extra captions. Avoid generic neural-network wallpaper, dense unreadable diagrams, unrelated chip imagery, distorted Chinese text, missing or rewritten cover text.

  3. engineering impact prompt:
     A technically credible editorial cover image for a WOEAI WeChat article about using physics-aware AI to accelerate high-temporal-resolution wind-field reconstruction for urban wind energy scheduling, wind-resource assessment, and numerical wind-tunnel data acceleration. Show a right-side engineering impact scene: a compact urban wind-energy environment with building blocks, wind-flow bands, high-temporal-resolution wind-field frames, and abstract power-spectrum or coherence curves drawn only as unlabeled graphic lines, suggesting that the reconstructed wind field preserves temporal details and supports engineering decisions. Include a subtle efficient-computing cue such as a small clean data-layer glow or simplified compute grid, without making it the main subject. Use a clean modern academic engineering magazine style and a wide 2.35:1 composition, target 900 x 383 px. Reserve the left 38-45% as a clean, low-detail white-to-pale-blue text-safe panel and reserve the right 55-62% for the engineering visual.

     Use exactly three Chinese text elements on the left panel, in this order: 1) a rounded strong-blue pill category tag: "数值风洞"; 2) an oversized bold deep-navy main hook: "稀疏快照补全风场"; 3) a smaller dark gray or blue-gray subtitle below: "看见湍流时间细节". Keep the Chinese characters crisp, complete, high-contrast, and unchanged. Use blue-cyan wind contours, clean urban geometry, wind-energy application cues, and restrained academic visual polish. Do not add any other text, English translations, fake chart labels, map labels, UI labels, logos, watermarks, or decorative small captions. Avoid hype, unconfirmed project claims, private partner names, generic smart-city poster styling, decorative technology wallpaper, distorted Chinese text, missing or rewritten cover text.

## 选中方案

- cover_execution_mode: `image-gen`
- cover_text_confirmation: user-confirmed
- confirmed_cover_text: `数值风洞 | 稀疏快照补全风场 / 看见湍流时间细节`
- confirmed_text_mode: `image-gen-text`
- candidate count: 3
- selected candidate: `cover-wechat-900x383-imagegen-v2-c-engineering-impact`
- selected text mode: `image-gen-text`
- requested exact cover text: `数值风洞 / 稀疏快照补全风场 / 看见湍流时间细节`
- generation tool: Codex image generation tool
- prompt scene: 城市风能高时间分辨率风场重建、稀疏快照、WTT-SRST、物理一致性与工程应用
- candidate A path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-a-research-scene.png)`
- candidate B path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-b-method.png)`
- candidate C path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-c-engineering-impact.png)`
- final cover path: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v2.png`
- previous selected cover: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v1.png)`
- previous fallback cover: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- dimensions: `900 x 383 px`
- local crop preview: `wechat/.local/cover-previews/cover-wechat-900x383-imagegen-v2.cover-preview.html`
- quality scores: article_specificity=5, main_subject_clarity=5, click_appeal=5, engineering_credibility=4, thumbnail_readability=5, crop_safety=4, text_quality=5
- rejected candidate reasons: none; candidates A and B are retained as alternates but C best balances urban wind-energy context, wind-field frame sequence, and small-thumbnail clarity.
- approval state: local visual text check and crop preview passed; WeChat backend mobile preview pending
- draft state: v2 generated locally and not uploaded to the existing WeChat draft in this round; existing draft still has the prior cover until an explicit draft update is approved.

## 出版信息徽章测试

- cover_execution_mode: `image-gen`
- publication metadata text: `Renewable Energy · 2026`
- intermediate v3 metadata candidates:
  - `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v3-a-badge-top-right.png)`
  - `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v3-b-badge-inline.png)`
  - `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v3-c-badge-near-category.png)`
- metadata placement tested: subtitle-below publication line / subtitle-below capsule / subtitle-below editorial seal
- candidate D path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v4-d-pub-line.png)`
- candidate E path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v4-e-pub-capsule.png)`
- candidate F path: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v4-f-pub-seal.png)`
- local crop preview: `wechat/.local/cover-previews/cover-preview.html`
- test outcome: D best preserves title hierarchy; E has the strongest metadata readability and livelier badge treatment; F is visually comfortable but reads slightly like a button.
- draft state: v4 candidates are local tests only and were not uploaded to the existing WeChat draft.

## 出版信息行默认化测试

- cover_execution_mode: `image-gen`
- publication metadata line: `Renewable Energy · 2026`
- metadata style: subtitle-below semi-bold deep-blue text line; no leading dot, no icon, no badge, no capsule, no button-like outline
- current prompt fragment: `Below the subtitle, add one publication metadata line: "Renewable Energy · 2026". Use semi-bold deep-blue modern sans-serif text, no leading dot, no icon, no enclosing badge, no capsule, no button-like outline. Keep it readable at phone thumbnail size and clearly secondary to the subtitle.`
- candidate A path: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-a-pub-line-no-dot.png`
- candidate B path: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png`
- candidate C path: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-c-pub-line-no-dot.png`
- local crop preview: `wechat/.local/cover-previews/cover-preview.html`
- test outcome: B is the selected v5 direction because the publication metadata line is clearly readable without competing with the subtitle; A is quieter but smaller; C is balanced but slightly less legible.
- selected draft-update cover: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png`
- draft state: existing WeChat draft updated with `cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png` at 2026-06-11T16:41:36+08:00; WeChat backend mobile preview not yet checked.
