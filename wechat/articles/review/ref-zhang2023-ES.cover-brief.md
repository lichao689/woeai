# ref-zhang2023-ES 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `结构抗风`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，四层横担光学位移与等效荷载重构的修正成品方案已获采用；本记录只绑定该最终哈希。
- final_cover_path: `wechat/assets/public-safe/ref-zhang2023-ES/cover-wechat-900x383-20261015-v5.png`；这是拟集成的公开目标路径，不表示本记录已完成公开绑定。
- final_image_sha256: `1723245f3f710ff82e0f0ddfb3fc3f2214d1f69be0218dc3b97de06bf6a13c08`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-zhang2023-ES.md`；`wechat/articles/review/ref-zhang2023-ES.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `结构抗风 | 四处位移反推塔身风力 / 模态识别重构等效荷载`
- 主标题实际分行：四处位移 / 反推塔身风力。
- publication_metadata_line: `Engineering Structures · 2023`；出版行实际为一行。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成及必要修复；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；全部水平正体。名义字号依据实际渲染记录，不从墨迹高度反推。
- selected_candidate_and_history: 首轮插图多出第五层横担，已拒绝；通过一次内置图像工具修复去掉额外横担，最终候选恰有四个标记高度。只采用修正后的最终哈希，旧图不作合格证据。

## 源文件获取记录

已获准使用的私有论文工作区中19个物理页的当前出版社PDF；论文身份由题名、作者与DOI核对，期刊和年份亦与现有注册表一致。当前副本与历史来源哈希不同，不声称恢复了历史原件字节。本次只读既有正文、证据与独立审核记录，不重新下载PDF。

当前完整科学稿的独立来源忠实性审查已通过，无必须修改项；含35个正文编号式、27个附录编号式、33幅原图、五表与42条参考文献。科学来源忠实性不等于证明反演算法可直接执行或唯一恢复局部真值。

## 关键事实证据定位记录

研究主线：由四层横担的有限位移观测识别主导模态力，再重构能再现结构响应的等效分布荷载；不是由四个点直接测出所有杆件的局部真实风力。

画面对象与关系：四层横担钢格构塔、四个青绿色测量高度、代表性相机与虚线视线，对应右侧简化荷载对象。最低标记在最低横担而非塔脚。

- PDF file pages 1–4，摘要、第2节及图1：有限位移、模态力识别、等效集中力重构与多集中质量悬臂杆关系。
- PDF file pages 4–6，第3.1节与图2–4：42.5 m四层横担角钢塔，以及10段等效模型；画面不复制有限元单元或节点总数。
- PDF file pages 7–8：测点1、2、4、6、第一阶主导及给定白噪声检验；画面四个测量高度对应响应观测，不是四个力传感器。
- PDF file page 10，图19及第4节：运动捕捉相机与四层横担的光学位移测量布置。
- PDF file pages 12–15，图27–33与表4–5：37.5 m/s、90°工况下总风力和位移的检验，包含横风总量及较低测点响应的差异。

## 科学边界

- 单台代表性相机只说明光学观测，不能推断实际系统只有一台相机；虚线是概念视线，不是发射的激光束或物理拉索。
- 四个测量高度不等于四段荷载模型。右侧代表节点与箭头是等效荷载说明，不是原文10分段的完整重建，也不是四处直接风力测量。
- 以第一阶主导响应为依据，不能唯一恢复每段或每根杆件的全部瞬时力；本文也未反演平均风力。
- 不宣称任意噪声免疫或所有位置误差小于10%。原文横风总脉动力系数为0.050对0.040，较低测点位移偏差亦被保留；局部风力无直接实测真值。
- 需要可靠模态参数、测点布置与更新模型；没有验证明显扭转、多模态共同主导、塔线耦合或真实台风破坏。

## 最终栅格与标签

- measured_canvas: `900 × 383 px`
- badge_target: `160 × 40 px`；名义圆角6 px，标签字24 px／700。
- badge_measurement_method: 每篇各自最终栅格的既有独立调色板连通域测量；8连通、局部背景颜色支持度至少50%，边界采用右／下不含的像素坐标。本次重新核对成品SHA-256、测量记录及渲染记录的对应关系，不用提示词、配置尺寸或另一篇的测量替代本图证据。
- badge_search_region: `[20, 20, 210, 85)`；只是搜索范围，不是测量结果。
- badge_outer_bbox_xyxy: `[36, 32, 196, 72)`
- badge_measured_width_height: `160 × 40 px`；在158–162 × 38–42 px允许范围内。
- badge_ink_bbox_and_height: `[69, 40, 164, 64)`，`95 × 24 px`；墨迹高度不等于名义字号。
- badge_nominal_typography_evidence: 对应最终哈希的实际渲染记录明确为Noto Sans CJK SC Bold、24 px、700；主标题48 px、副标题24 px、出版行18 px由同一记录确认。
- badge_radius_and_padding_review: 已知渲染设置为6 px圆角，既有成品审查核对其外观；不称色彩检测器测得精确半径。墨迹距标签左／上／右／下边界为33／8／32／8 px，完整位于标签内。圆角视觉目标只容许至多±1 px栅格边缘不确定性。
- badge_geometry_status: `pass`
- exact_text_status: `passed-existing-final-pixel-review`
- typography_and_radius_status: `passed-render-settings-and-existing-visual-review`
- scientific_evidence_status: `passed-source-bounded-cover-review`
- horizontal_composition_status: `passed-existing-final-pixel-review`
- design_contract_checked: `passed-local`

## 横向成品审查与状态区分

- horizontal_composition: 左侧为文字，右侧以相机观测四层横担的塔与等效荷载对象说明输入和重构关系；横向留白支持阅读，不以中心裁切框约束全部信息。 色系为浅蓝文字区、深青绿色标签与浅绿色标签字，保持结构抗风系列层级。
- review_provenance: 本记录继承后续独立成品审查的实际900／360／120像素观察。本次编写重新核对每篇各自成品与记录的字节、尺寸及证据，不声称另做一次开图视觉检查。
- 900 × 383：文字完整、水平正体，修正后四层横担与四个标记高度清楚，相机、虚线视线和等效荷载对象无文字遮挡。
- 360 px宽：主副标题可辨，光学位移观测与荷载重构主关系仍可识别。
- 120 px宽：塔形与系列身份可识别；四层标记、视线细节及全部文字不保证可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们是制作时点的历史状态，不覆盖后续独立科学／视觉审查和当前采用确认，也没有被回填成历史通过。早期正文记录中的封面未制作与独立审查待完成同样按历史时点解释。
- current_independent_review: `passed`；科学稿来源审查与封面科学／视觉审查分别有据，不以标签测量通过代替二者。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 采用与本地视觉通过不等于main提交／推送、网站部署、图片上传、后台草稿创建、真实手机浅色／深色预览或文章发布批准。公开资产绑定由后续获授权集成步骤完成；本记录未改变这些外部状态。
