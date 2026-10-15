# ref-zhao2023-BS 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `数值风洞`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，当前台风城市风场候选已获采用；后续采用状态与制作者早期的待审字段分开记录。
- final_cover_path: `wechat/assets/public-safe/ref-zhao2023-BS/cover-wechat-900x383-20261015-v5.png`
- final_image_sha256: `3fe6abed84d7fb86c46ba1f84629bfd429fc6f23c3a76c4252df6eeed5a8cf89`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-zhao2023-BS.md`；`wechat/articles/review/ref-zhao2023-BS.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `数值风洞 | 台风来时街道风怎么算 / 气象与城市流场单向嵌套`
- 主标题实际分行：台风来时 / 街道风怎么算。
- publication_metadata_line: `Building Simulation · 2023`；实际分行：Building Simulation · 2023。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品也不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；出版行一行，全部水平正体。
- selected_candidate_and_history: 采用已批准候选的最终文案；较早事实简报中的其他标题仅属未采用的编辑选项，不回写为当前图中文字。

## 关键事实证据定位记录

研究主线：将气象模型单向嵌套到城市CFD，并以局地观测趋势修正边界，研究台风事件中的街区风场。

画面对象与关系：有海岸和后方地形的密集街区承接上方气象输入；计算域和稀疏流线表达气象到城市的单向关系，不表示城市反向反馈天气模式。

- PDF file pages 4–5，图2：九龙湾地形、海岸与城市建筑背景，以及不同观测位置的分工。
- PDF file pages 7–10，图5–6：中尺度到城市CFD的单向嵌套、按时段设置的平均边界和稳态RANS方法。
- PDF file pages 10–12，图7：观测与气象模拟的趋势差异经空间相关性传递到侧边界，不是域内逐楼强制同化。
- PDF file pages 13–19，图12、14–17及表2：海马事件、独立测站的平均量验证、指定工况行人风与测站代表性。

## 科学边界

- 海岸山地城市为概念示意，不是九龙湾精确几何或真实计算帧；不把台风眼置于研究街区，也不把其他台风破坏照片移作海马证据。
- 方法是单向气象到城市传递，城市CFD采用稳态RANS分时段边界；不称双向耦合、LES、完整瞬时阵风解析或已部署实时预警。
- NP观测参与同化、SE观测用于独立验证，不能把两者合并成同一验证站；趋势修正不是CFD域内加入逐点松弛源。
- 证据限于海马、指定站点和21小时内的30分钟均值比较；不承诺全城统一误差、全年行人舒适度合规、结构风压或损伤预测。

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

- horizontal_composition: 左侧文字与右侧沿海密集街区连贯衔接，保留气象输入到街道的尺度联系；不加入多余的流程节点或数值排行榜。 色系为浅蓝文字区、蓝色标签与白色标签字。
- review_provenance: 本记录继承既有独立成品审查的900／360／120像素观察，本次编写只核对记录和字节，不声称另行打开图像进行了新的视觉检查。
- 900 × 383：文字完整、水平正体，沿海城市、计算场和来流关系清楚，工程场景占据右侧宽幅空间。
- 360 px宽：主副标题可辨，气象输入下的街区场景仍可识别。
- 120 px宽：仅记录城市场景与系列身份可识别，不承诺街道流线细节或所有文字可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们描述制作时点，不覆盖后续独立审查和当前采用确认，也未被回填成历史通过。
- current_independent_review: `passed`；采用后续独立的成品科学／视觉审查结论，而非仅凭标签测量通过。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 封面采用与本地视觉通过不等于图片上传、后台草稿创建、手机浅色／深色预览或文章发布批准；公开资产绑定由后续获授权集成步骤完成。
