# ref-zhao2025-SCS 封面简报

## 当前有效封面（2026-10-14）

本节为当前选图唯一入口。下方历史记录中的旧分类、旧路径、旧评分和旧后台说明均不代表本次状态。

- cover_design_contract: `WOEAI-cover-v5`
- current_secondary_direction: `数值风洞`
- cover_text_confirmation: `user-confirmed-batch-editorial`；用户已授权本批依据原文拟定并复核后采用，不逐篇重复选五选一。
- current_cover_text: `数值风洞 | 从影像到可计算几何 / 三维高斯重建与轮廓整理`
- selected candidate: `20261014-v5`
- final cover path: `wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-20261014-v5.png`
- current_final_sha256: `8bf2b4b0f009e15df7c2b23ef5c822da9e861ceb62ad77196e1060722c071b29`
- final_dimensions: `900 × 383 px`
- current_local_state: 本地全图、宽图及缩略图诊断通过，独立视觉复核通过。
- rendering_route: 工程插画由内置 imagegen 生成；文字与徽标按本轮用户授权固定排版。最终文件是明确记录的组合排版，不宣称一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700，主标题 48 px / 700，副标题 24 px / 400，期刊年份 18 px / 400；全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，实测 160×40 px；圆角渲染参数 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，实际墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实际字形、内边距与圆角同时目视检查。
- evidence_anchor: Fig.1 工作流、Fig.14 三维高斯点云与 Fig.18 建筑几何。
- selection_and_science_review: 三方向采用 B，以点云/高斯椭球到建筑几何的渐变表现几何整理。A 无人机元素非必要；C 风场容易误认为实际验证结果，故不采用。建筑是匿名概念场景，不是原文场地复刻。
- source_scope: 概念插画，不是论文计算图、实测照片、原图尺寸复刻或已建成项目。
- local_preview: 已检查完整 900×383、360 px 与 120 px 宽图；缩略图只诊断分类、主对象及标题层级，不要求最小图所有小字可读。
- current_backend_state: 本次上传与回读以同篇正式投递记录为准；本地审核不等于已提交。
- backend_preview_status: `pending`；实际微信手机端预览尚未核验。
- rtd_cover_state: 本轮不改既有 RTD 封面引用。

## 历史记录与本轮过程（不作为当前选图入口）

### ref-zhao2025-SCS 封面简报

#### 文章标题

数值风洞 | 用 3D Gaussian Splatting 重建城市建筑几何

#### 视觉目标

封面应表达“从城市影像和 3DGS 点云到 CFD 可用建筑几何”的技术路线。不要直接使用论文正文图作为封面，不嵌入文字、logo、合作方名称或未经确认的具体地名。画面主体保持在中间区域，适配微信公众号首图 `900 x 383 px` 及可能的方形裁切。

#### 候选概念 1: 城市街区与风场叠加

- 核心画面: 一个抽象化城市街区，白色或浅灰建筑群从鸟瞰角度展开，透明蓝绿色风场流线和速度等值面穿过街巷。
- 设计重点: 让读者第一眼看到“城市建筑几何 + 风场模拟”。
- 生成提示词方向: aerial view of a dense urban block, clean white building massing, translucent blue-green wind-flow simulation overlay, subtle CFD contour field, realistic but not tied to a named place, academic engineering visualization, no text, no logo.
- 风险控制: 不使用真实可识别城市地标；避免过度科幻化的霓虹风格；不要生成中文或英文文字。

#### 候选概念 2: 高斯点云变成建筑几何

- 核心画面: 左侧是由彩色 Gaussian 点云和半透明椭球组成的建筑轮廓，向右逐步过渡为规则的白色 LoD 建筑几何模型。
- 设计重点: 突出 3D Gaussian Splatting 从视觉重建走向 CFD 几何前处理的“方法感”。
- 生成提示词方向: 3D Gaussian Splatting point cloud of urban buildings transforming into clean simulation-ready building geometry, colored translucent ellipsoids on the left, precise white LoD building model on the right, neutral background, engineering research cover, no text, no logo.
- 风险控制: 点云不要像娱乐特效；建筑几何需要规则、干净、可计算；避免出现无法解释的机械结构。

#### 候选概念 3: 从视觉数据到仿真模型

- 核心画面: 中心是一条清晰的视觉流程：无人机影像纹理、点云、建筑几何、风场结果四个元素在同一画面中从左到右连接，但不使用文字标签。
- 设计重点: 表达本文的工程影响，即把视觉数据更快转化为城市风模拟可用模型。
- 生成提示词方向: cinematic but clean engineering workflow, drone imagery tiles becoming point cloud, point cloud becoming simplified urban building geometry, geometry surrounded by blue-green CFD wind contours, centered composition for WeChat cover crop, no embedded text, no logos, no named city.
- 风险控制: 不出现品牌化无人机或平台界面；流程符号保持简洁，不做复杂小字说明。

#### 当前状态

- 最终封面: `wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png`
- 新候选对比板: `wechat/.local/cover-previews/ref-zhao2025-SCS.quality-board.html`
- 新候选联系表: `wechat/.local/cover-candidates/ref-zhao2025-SCS/contact-sheet.png`
- 预览结果: all new candidates match `900 x 383 px`, pass local ratio and file-size checks
- 微信后台预览: pending

#### 2026-06-10 候选复审

本轮按升级后的 `wechat-cover` 规则生成并比较了无文字、image-gen 直出短文字、程序叠字三类候选。

| ID | 模式 | 本地候选文件 | 评价 |
|---|---|---|---|
| A | no-text | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-a-no-text-3dgs-to-geometry.png` | 3DGS 点云到建筑几何的论文特异性强，适合不放封面文字的稳妥方案。 |
| B | no-text | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-b-no-text-urban-cfd.png` | 城市 CFD 风场直观，工程感稳定，但比 A 更接近常规城市风场封面。 |
| C | image-gen-text | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-c-imagegen-text-urban-cfd.png` | 中文文字正确、可读性好，点击感强；主题偏城市风场，方法特异性略弱。 |
| D | image-gen-text | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-d-imagegen-text-3dgs-method.png` | 已采纳为 v2 正式封面。兼顾 3DGS 点云、建筑几何、CFD 风场和短中文 hook；小图识别度最好。 |
| E | programmatic-overlay | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-e-program-text-3dgs-method.png` | 文字最可控，但深色文字面板遮挡主体较多，视觉冲击弱于 D。 |
| F | programmatic-overlay | `wechat/.local/cover-candidates/ref-zhao2025-SCS/candidate-f-program-text-urban-cfd.png` | 文字可控，画面稳妥；主题特异性和点击感弱于 D。 |

#### 推荐

D 已由用户确认为新版正式封面，并保存为 `wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png`。它最能区别于一般“城市风场”封面，并且直接对应本文的 3D Gaussian Splatting 方法贡献；短文字“从影像到可计算几何”比完整标题更适合封面点击场景。

若不希望正式封面使用 image-gen 直接生成的文字，则选择 A 作为无文字方案，或以 A 为底图重新做更克制的程序叠字版本。

#### 系列规范迁移（2026-10-05）

- cover_design_contract: `WOEAI-cover-v2`
- 规范: [统一网格、字号、配色与裁切](../../../.agents/skills/wechat-cover/references/cover-standards.md)
- 本文方向: `数值风洞`，依据对应正文标题；仅用该方向固定色彩令牌，不另起画风
- 证据入口: [本文事实审阅](ref-zhao2025-SCS.review.md)；生成前完成工程叙事证据卡
- 文字来源: 保留历史确认记录，旧请求文字不自动视为新一轮批准；缩短或改写须重新确认
- 科学元素: 选择一个已核实主对象；路线为已验证输入 → 方法 → 输出；潜在用途与结果分开
- 构图: 900 × 383 px；左文区 x=36–396；关键科学对象 x=420–620、y=56–276；底部三节点路线
- 历史复用限制: 既有提示词、概念和选图仅供溯源，不直接当新一轮完整提示词；重新按 v2 及审阅证据编写
- migration_status: specification-updated; existing-image-not-regenerated
- design_contract_checked: pending; 尺寸一致不证明旧图符合新布局、字级或科学对象裁切
- backend_preview_status: unchanged; 此次简报维护没有新增后台手机预览
