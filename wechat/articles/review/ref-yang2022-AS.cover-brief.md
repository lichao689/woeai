# ref-yang2022-AS 封面简报

## 当前设计与采用

- cover_design_contract: `WOEAI-cover-v5`
- research_family: `工程结构抗风`
- secondary_direction: `结构抗风`
- scope: 记录已采用成品，供本地集成；本次不生成或修改图片。
- migration_state: `adopted-local-review-complete; integration-pending`
- user_adoption: `adopted`
- confirmation_note: 2026-10-15，按目标高度和响应量确定等效风荷载的修正成品方案已获采用；本记录只绑定该最终哈希。
- final_cover_path: `wechat/assets/public-safe/ref-yang2022-AS/cover-wechat-900x383-20261015-v5.png`；这是拟集成的公开目标路径，不表示本记录已完成公开绑定。
- final_image_sha256: `e2a1cbd8541b8decc69866d8ed192eb69a35e5bc842666a1eda00137c0130785`
- 文章与证据记录：`wechat/articles/draft-public-safe/ref-yang2022-AS.md`；`wechat/articles/review/ref-yang2022-AS.review.md`。

## 文字与制作记录

- cover_execution_mode: `image-gen`
- cover_text_confirmation: `batch-authorized-editorial-selection`
- confirmed_text_mode: `authorized-deterministic-typesetting`
- confirmed_cover_text: `结构抗风 | 等效风荷载该看哪一层 / 位移弯矩剪力分别等效`
- 主标题实际分行：等效风荷载 / 该看哪一层。
- publication_metadata_line: `Applied Sciences · 2022`；出版行实际为一行。
- actual_generation_and_edit_tools: 既有工程插图由内置 `image_gen.imagegen` 生成及必要修复；Pillow执行获授权的比例导出与确定性文字、标签排版。工程主体不是用代码绘制，成品不称全部文字均由图像工具生成。
- typography: Noto Sans CJK SC；标签24 px／700、主标题48 px／700、副标题24 px／400、出版行18 px／400；全部水平正体。名义字号依据实际渲染记录，不从墨迹高度反推。
- selected_candidate_and_history: 首轮插图把不同响应箭头分别绑定到不同高度，可能误导为每层只对应一种响应，已拒绝；一次内置图像工具修复移除这些箭头图标，保留三个概念目标截面。只采用修正后的最终哈希。

## 源文件获取记录

已获准使用的当前12页PDF用于科学正文与原图恢复，保留旧13页版本作明确标注的对照。论文身份、Applied Sciences与2022年已经同原文首页和现有注册表核对；两份来源不宣称字节相同。本次只读既有正文、证据与独立审核记录，不重新下载PDF。

独立完整科学来源忠实性审查已通过。图1的照片、尺寸及全部五阶振型和图2四面板均已恢复；图3继续采用原完整PNG，不声称与新源JPEG像素相同。式(10)恢复两版本都印有的绝对值竖线；式(19)有据采用旧版明确平方，并披露新版数字2落在基线附近的排印差异，不虚构统一后的新公式。

## 关键事实证据定位记录

研究主线：等效静力风荷载同时依赖目标高度与目标响应；位移、弯矩、剪力要分别评估，不能把顶点或基底的单一因子沿全高直接套用。

画面对象与关系：一座规则矩形高层建筑的工程概念图与三个不同高度的目标截面平面。建筑取自200×50×40 m数值算例，不是有名称的实建项目；三个平面只用于提示分析位置。

- 当前12页PDF file pages 7–8，第3节、式(23)–(30)：用位置与响应相关的影响函数计算背景、共振及阵风荷载因子。
- PDF file pages 8–9，第4节、表1–2：200×50×40 m规则高层建筑，0.22 Hz与1%阻尼，以及四组振型指数和质量折减参数。
- PDF file page 10，图3及pages 10–11结论：位移、弯矩、剪力因子的高度分布并非同一规律；约22%属于本文特定顶部比较。
- PDF file pages 5–6，第2.3节、图1–2：另一独立算例是60 m避雷针，用于时频域与耦合量讨论；该对象没有画到建筑屋顶上。
- PDF file page 4，式(10)；page 5，式(19)：当前科学稿分别记录转写修正与双源排印差异，封面不把它们包装成已经复现的算法。

## 科学边界

- 三个平面不是物理楼层支撑、风压等值线、结果数值或原文全部采样位置。每一个目标截面都可分别评估位移、弯矩和剪力，不能解读成“一层一种响应”。
- 200 m建筑和60 m避雷针是两个独立算例，不是把避雷针安装到建筑屋顶后的组合体系；图中只保留建筑主对象。
- 本文是理论与数值等效荷载研究，封面不添加CFD网格、测压装置、风洞试验或全尺度实测的暗示。
- 不给全部建筑统一增加22%的荷载，也不把“小于2%”画成通用误差或耦合幅值保证；两个数字都须保留原算例、指标和记号差异。
- 顺风向数值例证不等于横风、扭转、非线性失稳或全部高阶模态已验证。来源公式与参考文献疑点保留，不称完成独立算法复现或外部书目核验。

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

- horizontal_composition: 左侧保留清晰文字区，右侧单座高层建筑以沿高三个目标截面提示研究问题；没有三张数据卡或一高度一响应的图标分配。 色系为浅蓝文字区、深青绿色标签与浅绿色标签字，保持结构抗风系列层级。
- review_provenance: 本记录继承后续独立成品审查的实际900／360／120像素观察。本次编写重新核对每篇各自成品与记录的字节、尺寸及证据，不声称另做一次开图视觉检查。
- 900 × 383：文字完整、水平正体，建筑与三个目标截面清楚；已移除误导性的分层响应箭头，未合并避雷针算例。
- 360 px宽：主副标题可辨，建筑沿高选取目标截面的关系仍可识别。
- 120 px宽：建筑主体与系列身份可识别；截面细节及全部文字不保证可读。
- historical_producer_state: 早期制作者记录中的待独立复核、未采用及测量器的未批准字段原样保留；它们是制作时点的历史状态，不覆盖后续独立科学／视觉审查和当前采用确认，也没有被回填成历史通过。早期正文记录中的封面未制作与独立审查待完成同样按历史时点解释。
- current_independent_review: `passed`；科学稿来源审查与封面科学／视觉审查分别有据，不以标签测量通过代替二者。
- crop_support_evidence: `pending`；本地缩略诊断不证明微信当前裁切规则，未宣称支持独立方形裁切或方形资产。
- backend_preview_checked: false
- cover_image_checked: false
- backend_upload_and_mobile_preview: `not performed`
- completion_note: 采用与本地视觉通过不等于main提交／推送、网站部署、图片上传、后台草稿创建、真实手机浅色／深色预览或文章发布批准。公开资产绑定由后续获授权集成步骤完成；本记录未改变这些外部状态。
