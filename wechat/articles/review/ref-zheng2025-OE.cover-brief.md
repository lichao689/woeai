# ref-zheng2025-OE 封面简报

## 当前有效封面（2026-10-14）

本节为当前选图唯一入口。下方历史记录中的旧分类、旧路径、旧评分和旧后台说明均不代表本次状态。

- cover_design_contract: `WOEAI-cover-v5`
- current_secondary_direction: `一体化分析`
- cover_text_confirmation: `user-confirmed-batch-editorial`；用户已授权本批依据原文拟定并复核后采用，不逐篇重复选五选一。
- current_cover_text: `一体化分析 | 等效波浪荷载如何选 / 钢制半潜平台结构评估`
- selected candidate: `20261014-v5`
- final cover path: `wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-20261014-v5.png`
- current_final_sha256: `35f7ce65bfef4b30a8bbab9c9c3ce9de4542c527e02cbeab421c683f8533e58a`
- final_dimensions: `900 × 383 px`
- current_local_state: 本地全图、宽图及缩略图诊断通过，独立视觉复核通过。
- rendering_route: 工程插画由内置 imagegen 生成；文字与徽标按本轮用户授权固定排版。最终文件是明确记录的组合排版，不宣称一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700，主标题 48 px / 700，副标题 24 px / 400，期刊年份 18 px / 400；全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，实测 160×40 px；圆角渲染参数 6 px。
- badge_actual_ink_bounds: `[57, 39, 175, 63]`，实际墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实际字形、内边距与圆角同时目视检查。
- evidence_anchor: PDF file page 3，Fig.1；三个角部立柱、底部三角形浮筒闭环，塔筒位于一个角柱；不添加第四中央柱或上部 X 撑。
- selection_and_science_review: A 修订版；调整浮筒高度并去除错误低位叶轮，保留完整上部风机。B、C 未用于最终构型。
- source_scope: 概念插画，不是论文计算图、实测照片、原图尺寸复刻或已建成项目。
- local_preview: 已检查完整 900×383、360 px 与 120 px 宽图；缩略图只诊断分类、主对象及标题层级，不要求最小图所有小字可读。
- current_backend_state: 本次上传与回读以同篇正式投递记录为准；本地审核不等于已提交。
- backend_preview_status: `pending`；实际微信手机端预览尚未核验。
- rtd_cover_state: 本轮不改既有 RTD 封面引用。

## 历史记录与本轮过程（不作为当前选图入口）

### ref-zheng2025-OE 封面简报

- 文章标题: 漂浮风电 | 为半潜式风机找到可信的等效静力波浪荷载
- 分类标签: 漂浮风电
- 封面短钩子: 等效波浪荷载
- 副标题: 半潜式风机
- 目标读者: 关注 WOEAI 论文、工程风环境、结构抗风和海上漂浮风电方向的公众号读者
- 避免: 私密项目名称、未确认合作方、复杂小字、虚构 UI 标签、夸张宣传语

#### 候选方向

1. research scene: 半潜式浮式风机、海浪、等效静力波浪荷载、结构应力
2. method: 用论文方法关键词和工程计算视觉表达技术路线
3. engineering impact: 用结构响应、风场或平台场景强化工程可信度

#### 选中方案

- selected candidate: `cover-wechat-900x383-imagegen-v1`
- selected text mode: `image-gen-text`
- requested exact cover text: `漂浮风电 / 等效波浪荷载 / 半潜式风机`
- generation tool: Codex image generation tool
- prompt scene: 半潜式浮式风机、海浪、等效静力波浪荷载、结构应力
- final cover path: `wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-imagegen-v1.png`
- previous fallback cover: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- dimensions: `900 x 383 px`
- local contact sheet: `wechat/.local/cover-previews/batch-10-imagegen-contact-sheet.png`
- local crop preview: `wechat/.local/cover-previews/batch-10-imagegen-cover-preview.html`
- approval state: local visual text check and crop preview passed; WeChat backend mobile preview pending
- draft state: existing WeChat draft has been live-updated to this new cover; pending WeChat backend mobile preview

#### 系列规范迁移（2026-10-05）

- cover_design_contract: `WOEAI-cover-v2`
- 规范: [统一网格、字号、配色与裁切](../../../.agents/skills/wechat-cover/references/cover-standards.md)
- 本文方向: `漂浮风电`，依据对应正文标题；仅用该方向固定色彩令牌，不另起画风
- 证据入口: [本文事实审阅](ref-zheng2025-OE.review.md)；生成前完成工程叙事证据卡
- 文字来源: 保留历史确认记录，旧请求文字不自动视为新一轮批准；缩短或改写须重新确认
- 科学元素: 选择一个已核实主对象；路线为已验证输入 → 方法 → 输出；潜在用途与结果分开
- 构图: 900 × 383 px；左文区 x=36–396；关键科学对象 x=420–620、y=56–276；底部三节点路线
- 历史复用限制: 既有提示词、概念和选图仅供溯源，不直接当新一轮完整提示词；重新按 v2 及审阅证据编写
- migration_status: specification-updated; existing-image-not-regenerated
- design_contract_checked: pending; 尺寸一致不证明旧图符合新布局、字级或科学对象裁切
- backend_preview_status: unchanged; 此次简报维护没有新增后台手机预览
