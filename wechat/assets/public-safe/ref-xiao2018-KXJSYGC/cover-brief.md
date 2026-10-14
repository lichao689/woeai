# ref-xiao2018-KXJSYGC 当前封面简报

## 当前候选（2026-10-14）

本节为当前文件和状态的唯一入口；后附原始证据简报保留形成过程，不以其中“未生成”措辞代替当前状态。

- cover_design_contract: `WOEAI-cover-v5`
- secondary_direction: `数值风洞`
- cover_text_confirmation: `batch-authorized-editorial-selection`；采用已审证据简报原文案。
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 风向变了网格不变 / 复杂地形风速比批量计算`
- verified_publication_line: `科学技术与工程 · 2018`
- selected_candidate: A 的两次局部科学修订版
- final_cover_path: `wechat/assets/public-safe/ref-xiao2018-KXJSYGC/cover-wechat-900x383-20261014-v5.png`
- final_cover_sha256: `3d9f5c5de1888b15fb978b5bf69d9261e0dfd66f6345ccab171c878e6f66076e`
- final_dimensions: `900×383 px`
- actual_tools: 内置 imagegen 生成/局部修正工程插图；Pillow 等比导出与固定文字排版；最终像素测量及宽图预览。不是全图一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700、主标题 48 px / 700、副标题 24 px / 400、期刊年 18 px / 400，全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，160×40 px；圆角名义 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实测来自最终文件，不由 prompt 代替。
- source_anchor: PDF file pages 1–2，Section 1 与 Fig.1 的目标区、真实扩展区、变平过渡区和速度分量；page 3 Fig.3 为地形依据。没有瞬态 LES 涡结构或量化性能承诺。
- selection_and_science_review: B 的两组等强箭头容易误读为同时相向来流；C 山体与湖泊偏离所需示意。A 初版峰形过陡，第一次修正后边缘仍像海岸悬崖，最终第二次改为低缓山地、连续地形扩展和宽阔平滑变平带。深蓝箭头与浅色幽灵箭头表示替代风向，不是同时冲撞；同一网格始终不旋转。
- source_scope: 源文约束的概念插图，不是实际计算云图、实测照片或原场址精确几何复刻。
- local_pixel_review: 完整 900×383、360 px 与 120 px 宽图检查通过；缩略图仅诊断层级、主对象与分类，不要求小字均可读。
- independent_review: passed；独立逐张检查实际 PNG，并结合此前全文科学审核确认科学表达边界。
- backend_upload_and_mobile_preview: pending；未据本地视觉检查声明官方后台通过。
- article_and_registry_state: 封面制作未改科学主文、原图、主要 review 或注册表；交整合者复核后消费此路径。

## 原始证据简报（历史形成过程）

### 全风向地形风速比封面简报

- publication_ref: ref-xiao2018-KXJSYGC
- 一级方向：工程结构抗风
- 标签：数值风洞
- 主标题：风向变了网格不变
- 副标题：复杂地形风速比批量计算
- 期刊年份：科学技术与工程 · 2018
- cover_text_confirmation: batch-authorized-editorial-selection
- confirmed_text_mode: authorized-deterministic-typesetting
- cover_execution_mode: image-gen

本轮已授权根据论文拟定复核文字，工程插图继续使用图像生成，文字和标签固定排版。

#### 可见科学对象

显示起伏山地位于中央目标域，外侧真实地形延伸、再逐渐变平的过渡；示意两种来流方向但保持同一块网格。图1是精确关系依据，图2/3给出真实地形起伏形态。工程插画不冒充新的CFD计算结果。

#### 科学限制

不得画成地形或整个网格旋转，不添加数值性能提升或“所有风向验证”印象；不画倒塔事故照片或未经来源支持的实际塔线布置。可以用抽象边界流线表达换向，但不制造量化加速色标。该论文是稳态RANS，不表现为已模拟瞬态LES涡结构。

#### 固定版式

900×383，数值风洞配色；160×40标签和24px名义字体遵守本轮统一排版。最终测像素边界、检查文字和科学场景；未生成、未测量、未后台预览。
