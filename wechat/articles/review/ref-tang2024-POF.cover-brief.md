# ref-tang2024-POF 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `数值风洞`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，当前气象风场重建候选已获采用；后续采用状态与制作者早期的待审字段分开记录。
- final_cover_path: `wechat/assets/public-safe/ref-tang2024-POF/cover-wechat-900x383-20261015-v5.png`
- final_image_sha256: `89d88d59c4e2b84f22aad699f2957068dee1e57d8cd5947ca5b4ce06d273711a`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-tang2024-POF.md`；`wechat/articles/review/ref-tang2024-POF.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 粗网格能补回什么 / 移位窗口重建气象风场`
- 主标题实际分行：粗网格能 / 补回什么。
- publication_metadata_line: `Physics of Fluids · 2024`；实际分行：Physics of Fluids · 2024。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品也不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；出版行一行，全部水平正体。
- selected_candidate_and_history: 采用已批准候选，未新增生成、改词或修图；较早事实简报的制作阶段状态不作为当前采用状态。

## 关键事实证据定位记录

研究主线：利用移位窗口网络重建气象风场，区分同源降采样恢复与不同分辨率WRF模拟之间的降尺度映射。

画面对象与关系：区域海岸与地形上方的水平气象场中，粗细单元和稀疏流线表达空间重建任务；不是加密真实求解网格后重新运行求解器。

- PDF file pages 4–5，图1–4：窗口／移位窗口注意力、层级和位置表示改动。
- PDF file pages 6–7，图5、表I：广东地区WRF嵌套域及100 m高度的水平风速分量；输入和目标分别来自不同分辨率模拟。
- PDF file pages 6–7、14–20，图16–25、表III–IV：同源二维算例与WRF气象降尺度分别检验，逐点误差、结构相似性和速度分布并非同一指标。
- PDF file pages 19–21，图26、表V及结论：湍动能是另外训练的映射，百米／秒级工程尺度仍属后续研究。

## 科学边界

- 粗细网格只表达风场重建概念，不能说成同一图像机械放大，也不能以颜色更平滑证明物理精度更高。
- 海岸地形是区域尺度概念场景，不是广东精确地形或某时刻的计算风场；不宣称来自现场观测。
- 千米级目标不等于已解析建筑绕流、瞬时阵风或局部风压；没有跨地区／跨年份泛化、现场部署或通用加速倍率的证明。
- 数组边长放大倍数与物理网格间距比不同，原文配准及部分指标存在待澄清之处；封面不放倍数、精度、耗时、虚构色标或性能曲线。

## 最终栅格与标签

- measured_canvas: `900 × 383 px`
- badge_target: `160 × 40 px`；名义圆角6 px，标签字24 px／700。
- badge_measurement_method: 已有最终栅格的独立调色板连通域测量；8连通、局部背景颜色支持度至少50%，边界采用右／下不含的像素坐标。成品及相关记录已重新核对SHA-256对应关系，不以提示词或配置尺寸冒充像素实测。
- badge_search_region: `[20, 20, 210, 85)`；只是搜索范围，不是测量结果。
- badge_outer_bbox_xyxy: `[36, 32, 196, 72)`
- badge_measured_width_height: `160 × 40 px`；在158–162 × 38–42 px允许范围内。
- badge_ink_bbox_and_height: `[69, 40, 162, 64)`，`93 × 24 px`；墨迹高度不作为名义字号证据。
- badge_nominal_typography_evidence: 既有实际渲染记录明确给出Noto Sans CJK SC Bold、24 px、700；主标题、副标题和出版行字号分别由同一渲染记录确认。
- badge_radius_and_padding_review: 已知渲染设置为6 px圆角，既有成品审查已核对圆角外观；不宣称色彩检测器测得精确半径。墨迹距标签左／上／右／下边界分别为33／8／34／8 px，完全位于标签内。圆角视觉目标仅容许至多±1 px栅格边缘不确定性。
- badge_geometry_status: `pass`
- exact_text_status: `passed-existing-final-pixel-review`
- typography_and_radius_status: `passed-render-settings-and-existing-visual-review`
- scientific_evidence_status: `passed-source-bounded-cover-review`
- horizontal_composition_status: `passed-existing-final-pixel-review`
- design_contract_checked: `passed-local`

## 横向成品审查与状态区分

- horizontal_composition: 左侧浅蓝文字区与右侧区域气象计算面连贯衔接；粗细单元承担一个主要解释关系，不拼成多模块仪表板。 色系为浅蓝文字区、蓝色标签与白色标签字。
- review_provenance: 本记录继承既有独立成品审查的900／360／120像素观察，本次编写只核对记录和字节，不声称另行打开图像进行了新的视觉检查。
- 900 × 383：文字完整、水平正体，区域气象场主体和粗细单元关系清楚，右侧空间得到使用。
- 360 px宽：主副标题可辨，区域风场重建场景仍可识别。
- 120 px宽：仅记录区域计算场景和系列身份可识别，不承诺细网格或所有文字可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们描述制作时点，不覆盖后续独立审查和当前采用确认，也未被回填成历史通过。
- current_independent_review: `passed`；采用后续独立的成品科学／视觉审查结论，而非仅凭标签测量通过。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 封面采用与本地视觉通过不等于图片上传、后台草稿创建、手机浅色／深色预览或文章发布批准；公开资产绑定由后续获授权集成步骤完成。
