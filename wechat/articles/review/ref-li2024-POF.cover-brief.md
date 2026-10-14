# ref-li2024-POF 封面简报

## 当前有效封面（2026-10-14）

本节为当前选图唯一入口。下方历史记录中的旧分类、旧路径、旧评分和旧后台说明均不代表本次状态。

- cover_design_contract: `WOEAI-cover-v5`
- current_secondary_direction: `数值风洞`
- cover_text_confirmation: `user-confirmed-batch-editorial`；用户已授权本批依据原文拟定并复核后采用，不逐篇重复选五选一。
- current_cover_text: `数值风洞 | 让湍流天然无散 / 由矢量势旋度构造速度场`
- selected candidate: `20261014-v5`
- final cover path: `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-20261014-v5.png`
- current_final_sha256: `071748abc30f39e9e0491d180df583ee88d066d95e9369b8c0eda398c07bffff`
- final_dimensions: `900 × 383 px`
- current_local_state: 本地全图、宽图及缩略图诊断通过，独立视觉复核通过。
- rendering_route: 工程插画由内置 imagegen 生成；文字与徽标按本轮用户授权固定排版。最终文件是明确记录的组合排版，不宣称一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700，主标题 48 px / 700，副标题 24 px / 400，期刊年份 18 px / 400；全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，实测 160×40 px；圆角渲染参数 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，实际墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实际字形、内边距与圆角同时目视检查。
- evidence_anchor: PDF file page 5，Section II.B 的矢量势旋度构造，以及 Fig.3 流程。
- selection_and_science_review: 三方向采用 B，以矢量势表征到湍流速度场的双体积概念图表现方法。A 入口波面易误读为边界注入；C 重叠体积含义不清。只表达连续构造的无散性，不等同离散质量守恒或任意城市入流验证。
- source_scope: 概念插画，不是论文计算图、实测照片、原图尺寸复刻或已建成项目。
- local_preview: 已检查完整 900×383、360 px 与 120 px 宽图；缩略图只诊断分类、主对象及标题层级，不要求最小图所有小字可读。
- current_backend_state: 本次上传与回读以同篇正式投递记录为准；本地审核不等于已提交。
- backend_preview_status: `pending`；实际微信手机端预览尚未核验。
- rtd_cover_state: 本轮不改既有 RTD 封面引用。

## 历史记录与本轮过程（不作为当前选图入口）

### ref-li2024-POF 封面简报

#### 基本信息

- 文章标题: 数值风洞 | 用矢量势随机流生成无散湍流
- publication_ref: `ref-li2024-POF`
- 推荐尺寸: `900 x 383 px`
- 画面策略: 不使用论文公式截图；新版封面使用短中文 hook，不重复完整标题。
- 当前状态: final v2 cover generated at `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png`; local batch crop preview passed; WeChat backend preview pending

#### 候选概念 1: 研究场景

- 核心画面: 深色或浅色数值风洞空间中，一个干净的三维湍流矢量场被半透明流线和细密涡量纹理包围。
- 视觉重点: 中央保持一团可辨识的湍流结构，周围有规则网格和少量流线，表达“可控的随机湍流”。
- 适合原因: 直接回应读者对“数值风洞”和“湍流入流”的直观理解，适合作为第一眼识别。
- 避免事项: 不放论文图表、公式截图或中文/英文生成文字。

#### 候选概念 2: 方法机制

- 核心画面: 左侧抽象矢量势场以柔和曲线或箭矢表示，经过中间的旋度变换视觉符号后，右侧形成无散的三维湍流结构。
- 视觉重点: 从“矢量势”到“速度场”的转换关系，使用颜色过渡表达方法链路。
- 适合原因: 突出本文最关键的方法贡献，即由矢量势场生成满足无散条件的湍流。
- 避免事项: 不画具体公式，不把旋度符号做成不可读的小字，不出现未经审核的文字标注。

#### 候选概念 3: 工程影响

- 核心画面: 一个简化的 LES 入口面释放出可控湍动入流，流场进入建筑或计算域轮廓，背景保留数值网格。
- 视觉重点: 入口边界、可控入流、数值模拟域三者形成清晰层次。
- 适合原因: 面向工程读者说明这项方法为什么和数值风洞、建筑结构抗风计算相关。
- 避免事项: 不暗示具体工程项目或合作方，不出现真实建筑/伙伴名称。

#### 推荐方向

已采用 v2 封面。它延续候选概念 2：以抽象矢量势场、入口边界和三维湍流涡结构表达“先生成矢量势，再得到无散湍流”的方法链路；短文字为“数值风洞 / 让湍流天然无散”。这版比原无文字封面更适合公众号列表中的快速识别。

#### 系列规范迁移（2026-10-05）

- cover_design_contract: `WOEAI-cover-v2`
- 规范: [统一网格、字号、配色与裁切](../../../.agents/skills/wechat-cover/references/cover-standards.md)
- 本文方向: `数值风洞`，依据对应正文标题；仅用该方向固定色彩令牌，不另起画风
- 证据入口: [本文事实审阅](ref-li2024-POF.review.md)；生成前完成工程叙事证据卡
- 文字来源: 保留历史确认记录，旧请求文字不自动视为新一轮批准；缩短或改写须重新确认
- 科学元素: 选择一个已核实主对象；路线为已验证输入 → 方法 → 输出；潜在用途与结果分开
- 构图: 900 × 383 px；左文区 x=36–396；关键科学对象 x=420–620、y=56–276；底部三节点路线
- 历史复用限制: 既有提示词、概念和选图仅供溯源，不直接当新一轮完整提示词；重新按 v2 及审阅证据编写
- migration_status: specification-updated; existing-image-not-regenerated
- design_contract_checked: pending; 尺寸一致不证明旧图符合新布局、字级或科学对象裁切
- backend_preview_status: unchanged; 此次简报维护没有新增后台手机预览
