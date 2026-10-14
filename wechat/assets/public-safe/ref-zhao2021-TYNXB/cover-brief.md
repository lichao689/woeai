# ref-zhao2021-TYNXB 当前封面简报

## 当前候选（2026-10-14）

本节为当前文件和状态的唯一入口；后附原始证据简报保留形成过程，不以其中“未生成”措辞代替当前状态。

- cover_design_contract: `WOEAI-cover-v5`
- secondary_direction: `数值风洞`
- cover_text_confirmation: `batch-authorized-editorial-selection`；采用已审证据简报原文案。
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 天气来风接入山地 / 单向嵌套检验局地风场`
- verified_publication_line: `太阳能学报 · 2021`
- selected_candidate: A（粗细尺度单向联系）
- final_cover_path: `wechat/assets/public-safe/ref-zhao2021-TYNXB/cover-wechat-900x383-20261014-v5.png`
- final_cover_sha256: `6b99e7549dc0bbfa3609179612f60bac78e5d86ab5daa7c060d62129b472e386`
- final_dimensions: `900×383 px`
- actual_tools: 内置 imagegen 生成/局部修正工程插图；Pillow 等比导出与固定文字排版；最终像素测量及宽图预览。不是全图一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700、主标题 48 px / 700、副标题 24 px / 400、期刊年 18 px / 400，全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，160×40 px；圆角名义 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实测来自最终文件，不由 prompt 代替。
- source_anchor: PDF file page 2 Fig.2；page 3 Fig.3 的 WRF 粗格点与 CFD 边界插值；page 5 Fig.6 地形。
- selection_and_science_review: B、C 的尺度差别可见但单向传递不如 A 明确；A 用唯一从粗网格到局地边界的箭头，不画反馈。云与海岸为环境氛围，不表示 CFD 已求解热力、湿物理或真实场址航拍。
- source_scope: 源文约束的概念插图，不是实际计算云图、实测照片或原场址精确几何复刻。
- local_pixel_review: 完整 900×383、360 px 与 120 px 宽图检查通过；缩略图仅诊断层级、主对象与分类，不要求小字均可读。
- independent_review: passed；独立逐张检查实际 PNG，并结合此前全文科学审核确认科学表达边界。
- backend_upload_and_mobile_preview: pending；未据本地视觉检查声明官方后台通过。
- article_and_registry_state: 封面制作未改科学主文、原图、主要 review 或注册表；交整合者复核后消费此路径。

## 原始证据简报（历史形成过程）

### 复杂地形 NWP/CFD 嵌套封面证据简报

- publication_ref: ref-zhao2021-TYNXB
- 一级方向：工程结构抗风
- 标签：数值风洞
- 主标题：天气来风接入山地
- 副标题：单向嵌套检验局地风场
- 期刊年份：太阳能学报 · 2021
- cover_text_confirmation: batch-authorized-editorial-selection
- confirmed_text_mode: authorized-deterministic-typesetting
- cover_execution_mode: image-gen

用户已授权本轮按来源拟定并复核文字，工程插图用图像生成，文字与标签固定排版。

#### 科学画面依据

以大范围疏网格逐渐接近起伏山地上的细网格计算域，只有单向从粗尺度向小尺度传递的视觉关系。局部域中表现山脊迎风和背风空间差异，不放真实结果曲线或伪造数值。来源为 PDF file page 2 Fig. 2、page 3 Fig. 3、page 5 Fig. 6。

#### 不得误画

不画双向反馈、卫星直接测得所有局部湍流、人工智能网络或漂浮海上平台；不加入热力/湿过程已被CFD求解的暗示；不把所有测点显示成统一改善。山地形态为原文示意依据，不冒称可识别的实际航拍场址。

#### 排版验收

输出900×383，数值风洞配色；160×40标签、24 px名义字体，标题/副标题/期刊年均按当前统一标准固定排版。图像生成仅制作插图；最终须测实际标签边界并检查全部字形、对比度和横向构图，后台手机预览另记。当前未生成、未测量。
