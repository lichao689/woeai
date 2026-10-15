# ref-li2010-WAS 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `数值风洞`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，修正后的物理／数值风洞对照方案已获采用；本记录只绑定该修正版的最终哈希。
- final_cover_path: `wechat/assets/public-safe/ref-li2010-WAS/cover-wechat-900x383-20261015-v5.png`
- final_image_sha256: `e3ec1e1893a7fd44d41ea7bd33027d771079f64ac148f38272d1a0f3bf072349`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-li2010-WAS.md`；`wechat/articles/review/ref-li2010-WAS.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 数值风洞怎样更可靠 / 与物理风洞对照检验`
- 主标题实际分行：数值风洞 / 怎样更可靠。
- publication_metadata_line: `Wind and Structures · 2010`；实际分行：Wind and Structures · 2010。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品也不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；出版行一行，全部水平正体。
- selected_candidate_and_history: 采用已批准的第二版。前版过度突出局部屋盖风压，现以物理／数值风洞对照重构主线；前版保留为历史记录，不选用，也不将其旧方向或文案沿用至本图。

## 关键事实证据定位记录

研究主线：通过物理风洞对照检验提升数值风洞的预测能力；复杂曲面屋盖是检验对象，不把局部屋盖吸力现象当成论文的唯一贡献。

画面对象与关系：上方为物理缩尺模型及测压示意，下方为同一研究对象的数值模型概念图。中央拱形屋盖、两侧曲面翼部、成对开口及圆形与矩形塔楼用于建立两个模型的对应关系。

- PDF file pages 1–3、8–9：研究目标与DSRFG相关湍流入口；改进的是入口条件和数值分析能力，不将DSRFG称为新提出的LES闭合模型。
- PDF file pages 3–4，图1–2：1:400刚性风洞模型与348对测压孔；图1及PDF file page 5图3支持屋盖和塔楼的几何特征。
- PDF file page 7：LES动态亚格子动能模型与RNG初始场、平均风压比较基线。
- PDF file pages 5–6、10、14–15、24：两个数值风向、上表面比较范围，以及分离区与再附区表现不同。

## 科学边界

- 测压管线为概念示意，不是试验装置逐根复刻；下方网格与流线不是实际求解器输出，也不是原文混合／四面体网格拓扑的精确再现。
- 成对模型表达对照关系，不代表支承构件完全相同。数值模型省略树状柱，本文数值比较限于屋盖上表面，不能扩展为净风压或完整结构响应验证。
- 仅检验90°和45°数值来流。LES在分离区较合理，RNG在再附区相对更好；脉动幅值及部分相关性偏大，不能宣称全面优胜或替代所有物理风洞试验。
- 不附加误差百分比、安全概率、结构承载或长期极值结论；背景块体不逐一认定为粗糙元或周围建筑。

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

- horizontal_composition: 左侧保留文字区，右侧上下对应物理与数值研究对象；横向空间服务于对照关系，不把全部科学内容挤入中央方框。 色系为浅蓝文字区、蓝色标签与白色标签字。
- review_provenance: 本记录继承既有独立成品审查的900／360／120像素观察，本次编写只核对记录和字节，不声称另行打开图像进行了新的视觉检查。
- 900 × 383：文字完整、水平正体，物理模型与数值模型的对应关系清楚，工程对象未在右侧被裁断。
- 360 px宽：主副标题可辨，物理与数值模型仍可区分。
- 120 px宽：两个研究模型与系列身份可识别；测压细节及所有文字不保证可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们描述制作时点，不覆盖后续独立审查和当前采用确认，也未被回填成历史通过。
- current_independent_review: `passed`；采用后续独立的成品科学／视觉审查结论，而非仅凭标签测量通过。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 封面采用与本地视觉通过不等于图片上传、后台草稿创建、手机浅色／深色预览或文章发布批准；公开资产绑定由后续获授权集成步骤完成。
