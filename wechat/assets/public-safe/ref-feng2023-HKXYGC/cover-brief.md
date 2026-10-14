# ref-feng2023-HKXYGC 当前封面简报

## 当前候选（2026-10-14）

本节为当前文件和状态的唯一入口；后附原始证据简报保留形成过程，不以其中“未生成”措辞代替当前状态。

- cover_design_contract: `WOEAI-cover-v5`
- secondary_direction: `数值风洞`
- cover_text_confirmation: `batch-authorized-editorial-selection`；采用已审证据简报原文案。
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 高风速区域在哪里 / 核电厂微地形风场验证`
- verified_publication_line: `核科学与工程 · 2023`
- selected_candidate: B（网格与局部绕流）
- final_cover_path: `wechat/assets/public-safe/ref-feng2023-HKXYGC/cover-wechat-900x383-20261014-v5.png`
- final_cover_sha256: `a0392a4d949149d908bdf5b09a96dcebced88fcc9ee575fca3c0e1887b4edf99`
- final_dimensions: `900×383 px`
- actual_tools: 内置 imagegen 生成/局部修正工程插图；Pillow 等比导出与固定文字排版；最终像素测量及宽图预览。不是全图一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700、主标题 48 px / 700、副标题 24 px / 400、期刊年 18 px / 400，全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，160×40 px；圆角名义 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实测来自最终文件，不由 prompt 代替。
- source_anchor: PDF file page 2，Figs.1–3；page 3，Fig.7 与 Section 3.2。双穹顶及矩形厂房形态按 Fig.2 约束，无虚构冷却塔、排烟或事故。
- selection_and_science_review: A 为较远海岸场景，C 箭头方向容易误读；B 的双穹顶、相邻矩形厂房和通道关系更清楚。多面体网格只是方法示意，不是原文实际网格或新的 CFD 云图。
- source_scope: 源文约束的概念插图，不是实际计算云图、实测照片或原场址精确几何复刻。
- local_pixel_review: 完整 900×383、360 px 与 120 px 宽图检查通过；缩略图仅诊断层级、主对象与分类，不要求小字均可读。
- independent_review: passed；独立逐张检查实际 PNG，并结合此前全文科学审核确认科学表达边界。
- backend_upload_and_mobile_preview: pending；未据本地视觉检查声明官方后台通过。
- article_and_registry_state: 封面制作未改科学主文、原图、主要 review 或注册表；交整合者复核后消费此路径。

## 原始证据简报（历史形成过程）

### 核电厂微地形风场封面证据简报

- publication_ref: ref-feng2023-HKXYGC
- 一级方向：工程结构抗风
- 二级方向与标签：数值风洞
- 本轮文字授权：用户同意按原文拟定并复核主副标题，不再逐篇等待五选一；工程插图用图像生成，文字标签用固定排版。
- 采用主标题：高风速区域在哪里
- 采用副标题：核电厂微地形风场验证
- 期刊年份：核科学与工程 · 2023
- cover_execution_mode: image-gen
- confirmed_text_mode: authorized-deterministic-typesetting
- cover_text_confirmation: batch-authorized-editorial-selection

#### 科学场景

采用横向工程示意图：沿海山地与核电厂低矮建筑群，突出厂房之间的通道和厂房角部来流分离，旁置简洁计算网格的局部过渡。图 1、2 给出真实地形和建筑形态，图 3 给出厂区加密网格，图 7 给出建筑间通道与局部风速比分布。工程插画明确为解释性示意，不做新的计算云图。

#### 证据与限制

- PDF file page 2，Figs. 1–3：沿海起伏地形、厂房与网格。
- PDF file page 3，Fig. 7、Section 3.2：180 度来流下局部加速位置。
- 不添加虚构冷却塔、排放烟羽、失火、爆炸、污染或事故元素。
- 不绘制带数值的风险热力图，不把示意箭头当实测速度，不暗示设备失效或核安全事故已发生。
- 不宣称数值模型替代规范、风洞验证或抗风承载力检查。

#### 固定排版与验收

按当前封面标准输出 900×383；数值风洞配色、160×40 标签及 24 px 名义字体。图像生成仅做工程插图，采用获准的固定排版路线添加文字，实际最终像素、字形与标签边界仍须验收。当前未生成、未测量、未完成后台预览。
