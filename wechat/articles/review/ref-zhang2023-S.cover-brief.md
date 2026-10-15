# ref-zhang2023-S 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `结构抗风`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，整塔测力与分段等效荷载的成品方案已获采用；本记录只绑定该最终哈希。
- final_cover_path: `wechat/assets/public-safe/ref-zhang2023-S/cover-wechat-900x383-20261015-v5.png`；这是拟集成的公开目标路径，不表示本记录已完成公开绑定。
- final_image_sha256: `685c179a25234b66a34b1c1381d6204195a2e523b7b451524c0a8b18f0717a8d`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-zhang2023-S.md`；`wechat/articles/review/ref-zhang2023-S.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `结构抗风 | 从整塔测力到分段风载 / 广义风力谱约束荷载估计`
- 主标题实际分行：从整塔测力 / 到分段风载。
- publication_metadata_line: `Structures · 2023`；出版行实际为一行。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成及必要修复；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；全部水平正体。名义字号依据实际渲染记录，不从墨迹高度反推。
- selected_candidate_and_history: 采用首次完成的最终候选。只记录这一最终哈希，不将工程插图称为原试验装置照片或原图复刻。

## 源文件获取记录

已获准使用的私有论文工作区中17个物理页的出版社正式版；题名、作者、期刊、年份与DOI已经由原文首页及现有注册表核对。本次只读既有正文、证据和独立审核记录，不重新下载PDF，不复制私有源路径或附件标识。

全文科学来源忠实性独立审查已通过；后续只修正公众号正文六处角度的上标符号，并有逐字节差异核验，其他19项科学稿件及原图字节不变。这一显示修正不改变封面事实或科学结论。

## 关键事实证据定位记录

研究主线：把整塔广义风力谱作为约束，估计沿高度分布的双方向随机风荷载，并考虑斜风下跨轴相干；不是用塔底记录唯一恢复每根杆件的真实瞬时风力。

画面对象与关系：四层横担、向上收细的钢格构塔与塔底测力概念装置，对应右侧分段等效荷载示意。两方向箭头表达水平荷载分量，节点表达代表高度；不把示意节点数当成原文10段离散模型。

- PDF file pages 1–2，摘要、引言及第2节：整塔谱约束分布式脉动荷载的研究目标；准定常方法的气动导纳和横风荷载局限。
- PDF file page 2，图1；page 3，图2与表1：等效集中力、实际塔型的四层横担与收细外形，以及10段模型参数。
- PDF file page 9，第3.1节；page 3，图3–4：1:25、1.7 m塔模型与试验装置；HFFB测力和气弹位移试验分别进行，不是同一时段同步测量。
- PDF file page 9，第3.2节与式(25)–(26)：两个塔体轴向风力的相干描述，拟合工况为30°、45°、60°。
- PDF file pages 10–11，第4.2节与第5节；page 8，图14：随机荷载及塔顶位移统计验证，RMS均值与峰值分布分别比较。

## 科学边界

- 塔底天平形状和连接线是概念表达，不是仪器逐件复刻；不能从画面推断测力与位移同步采集。
- 等效节点数、代表高度和箭头长度只说明离散荷载及两个水平分量，不对应逐段实际力值，也不是原文10段模型的精确绘图。
- 没有虚构功率谱、响应曲线或误差数值。小于10%仅指给定7个风向下塔顶位移RMS的样本均值误差，不是峰值或局部风力恢复精度保证。
- 方法仍依赖目标塔的经验谱、气动与相干参数、识别刚度及总阻尼；没有验证分段局部扭矩、塔线耦合、构件倒塌或任意非平稳灾害风。

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

- horizontal_composition: 左侧文字留白，右侧把实体格构塔、塔底测力与较简洁的等效荷载对象连成横向叙事；不把全部内容压入中央方形。 色系为浅蓝文字区、深青绿色标签与浅绿色标签字，保持结构抗风系列层级。
- review_provenance: 本记录继承后续独立成品审查的实际900／360／120像素观察。本次编写重新核对每篇各自成品与记录的字节、尺寸及证据，不声称另做一次开图视觉检查。
- 900 × 383：文字完整、水平正体，四层横担塔与分段荷载示意分工清楚，工程主体完整且无文字遮挡。
- 360 px宽：主副标题可辨，整塔对象与等效荷载关系仍可识别。
- 120 px宽：塔的主体与系列身份可识别；节点、箭头细节及全部文字不保证可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们是制作时点的历史状态，不覆盖后续独立科学／视觉审查和当前采用确认，也没有被回填成历史通过。早期正文记录中的封面未制作与独立审查待完成同样按历史时点解释。
- current_independent_review: `passed`；科学稿来源审查与封面科学／视觉审查分别有据，不以标签测量通过代替二者。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 采用与本地视觉通过不等于main提交／推送、网站部署、图片上传、后台草稿创建、真实手机浅色／深色预览或文章发布批准。公开资产绑定由后续获授权集成步骤完成；本记录未改变这些外部状态。
