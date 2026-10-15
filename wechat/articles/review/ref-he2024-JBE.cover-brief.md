# ref-he2024-JBE 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `结构抗风`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，当前高楼与屋顶液箱候选已获采用；后续采用状态与制作者早期的待审字段分开记录。
- final_cover_path: `wechat/assets/public-safe/ref-he2024-JBE/cover-wechat-900x383-20261015-v5.png`
- final_image_sha256: `3a9aefa1ca618a2f77acc9b1bf7114cb287bcfec771f28551bdf4264539b3ccc`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-he2024-JBE.md`；`wechat/articles/review/ref-he2024-JBE.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `结构抗风 | 消防水箱怎样减振 / 液体晃荡与结构双向耦合`
- 主标题实际分行：消防水箱 / 怎样减振。
- publication_metadata_line: `Journal of Building Engineering · 2024`；实际分行：Journal of Building / Engineering · 2024。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品也不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；出版行两行，全部水平正体。
- selected_candidate_and_history: 采用已批准候选，未新增生成、改词或修图；较早事实简报的制作阶段状态不作为当前采用状态。

## 关键事实证据定位记录

研究主线：把非线性液体晃荡与结构运动双向连接，比较屋顶调谐液体阻尼器的质量和调谐设置对风振响应的影响。

画面对象与关系：地面固定的矩形高层建筑及屋顶矩形水箱构成主对象；水箱局部剖示液面与上部空气，说明液体运动和建筑振动相互作用。

- PDF file pages 1–2、19：屋顶消防水箱作为TLD的研究动机，不是消防合规或实际改造验收。
- PDF file pages 11–13，图15、式9–10：结构位移驱动液箱、晃荡反力反馈结构的双向数值耦合。
- PDF file pages 14–16，图21–24、表3：CAARC建筑及屋顶矩形TLD数值算例；箱体与液深可支持约半箱水、上部空气的定性表达。
- PDF file pages 13–14、16–19，图18、25–28：单自由度刚架与高层建筑是不同验证／应用层级，质量和调谐研究的比较口径不得混合。

## 科学边界

- 建筑与水箱是概念场景，不是精确CAARC立面、已建工程照片或实际消防改造；建筑不是浮体，水箱不是建筑周围的水池。
- 等效质量—弹簧模型不是真实装置构造，图中不增加机械活塞、弹簧、大摆锤或浮筒；液面示意不替代真实响应曲线。
- 78.5%的位移降低属于单自由度刚架共振简谐激励，不得移作高楼风振或普遍减振效果。
- 未证明有效控制绕Z轴扭转或抗震效果，也不能推导越多水越好、通用最优调谐、消防合规或实楼承载验收。

## 最终栅格与标签

- measured_canvas: `900 × 383 px`
- badge_target: `160 × 40 px`；名义圆角6 px，标签字24 px／700。
- badge_measurement_method: 已有最终栅格的独立调色板连通域测量；8连通、局部背景颜色支持度至少50%，边界采用右／下不含的像素坐标。成品及相关记录已重新核对SHA-256对应关系，不以提示词或配置尺寸冒充像素实测。
- badge_search_region: `[20, 20, 210, 85)`；只是搜索范围，不是测量结果。
- badge_outer_bbox_xyxy: `[36, 32, 196, 72)`
- badge_measured_width_height: `160 × 40 px`；在158–162 × 38–42 px允许范围内。
- badge_ink_bbox_and_height: `[69, 40, 164, 64)`，`95 × 24 px`；墨迹高度不作为名义字号证据。
- badge_nominal_typography_evidence: 既有实际渲染记录明确给出Noto Sans CJK SC Bold、24 px、700；主标题、副标题和出版行字号分别由同一渲染记录确认。
- badge_radius_and_padding_review: 已知渲染设置为6 px圆角，既有成品审查已核对圆角外观；不宣称色彩检测器测得精确半径。墨迹距标签左／上／右／下边界分别为33／8／32／8 px，完全位于标签内。圆角视觉目标仅容许至多±1 px栅格边缘不确定性。
- badge_geometry_status: `pass`
- exact_text_status: `passed-existing-final-pixel-review`
- typography_and_radius_status: `passed-render-settings-and-existing-visual-review`
- scientific_evidence_status: `passed-source-bounded-cover-review`
- horizontal_composition_status: `passed-existing-final-pixel-review`
- design_contract_checked: `passed-local`

## 横向成品审查与状态区分

- horizontal_composition: 左侧文字留白与右侧固定高楼、屋顶液箱形成横向主次；水箱服务于建筑减振叙事，不将孤立储水罐作为唯一对象。 色系为浅蓝文字区、青绿色标签与浅绿标签字。
- review_provenance: 本记录继承既有独立成品审查的900／360／120像素观察，本次编写只核对记录和字节，不声称另行打开图像进行了新的视觉检查。
- 900 × 383：文字完整、水平正体，高层建筑与屋顶液箱关系清楚，长刊名按词分为两行。
- 360 px宽：主副标题可辨，建筑和屋顶液箱作为一个研究对象仍可识别。
- 120 px宽：系列与建筑主体可识别；屋顶水体细节很小，不能宣称液面细节或所有文字可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们描述制作时点，不覆盖后续独立审查和当前采用确认，也未被回填成历史通过。
- current_independent_review: `passed`；采用后续独立的成品科学／视觉审查结论，而非仅凭标签测量通过。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 封面采用与本地视觉通过不等于图片上传、后台草稿创建、手机浅色／深色预览或文章发布批准；公开资产绑定由后续获授权集成步骤完成。
