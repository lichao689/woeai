# <publication_ref> 封面简报

Copy to `wechat/articles/review/<publication_ref>.cover-brief.md`. Resolve the
contract from the repository root:
`.agents/skills/wechat-cover/references/cover-standards.md`.
Detailed machine reports and experiments stay in ignored storage; public notes
record public-safe results, not private paths or identifiers.

## 当前设计任务

- cover_design_contract: `WOEAI-cover-v5`
- scope: <新封面 / 已批准候选修复 / 仅维护规范，不生成、不改正文或后台>
- migration_state: pending
- 文章与证据记录: <对应正文及 review>
- 二级方向: <注册表中的数值风洞 / 结构抗风 / 一体化分析 / 混凝土浮体 / 数值水池>
- 工程问题、基线 → 改动: <审核后的具体差异及证据定位>
- 主要科学对象与关系: <真实几何、连接、材料、物理意义及原文位置>
- 已验证 / 潜在用途 / 必要限定: <分开记录，不虚构杆件、重心或幅值结果>
- horizontal_composition: <横向叙事、主次与留白；位置可调，不把内容挤入中央方框>
- crop_support_evidence: <实际微信界面/日期/观察；未核验写 pending，方图仅诊断>

## 文字确认

- cover_execution_mode: <image-gen / prompt-only / guidance-only>
- cover_text_confirmation: pending
- confirmed_cover_text: <实际确认的二级方向 | hook / subtitle>
- confirmed_text_mode: `image-gen-text`
- publication_metadata_line: <已核实公开期刊名和年份；缺失则记原因>
- confirmation_note: <真实批准记录；已授权修复可复用原文，不擅自改词>

## 候选和修复

1. 研究场景: <横向科学对象和重点>
2. 方法机制: <证据支持的改变环节>
3. 工程应用: <与已验证结果区分的潜在用途>

- requested_candidate_scope: <新设计三候选 / 用户指定方向或局部修复>
- actual_generation_and_edit_tools: <实际使用工具、参数能力及导出步骤，不夸大>
- same_problem_attempts: <0–2，逐次记录失败；两次仍失败即停止同策略重试>
- rejected_reasons_and_strategy_change: <实测缺陷、换策略内容或所需批准>
- invariants_rechecked_after_repair: <每次完整重检，不只检查局部>

## 最终栅格验收

- selected_candidate / final_cover: <实际文件；未通过不能称已修正成品>
- final_image_sha256: <最终文件哈希，换图后旧验收失效>
- measured_canvas: <实际像素；必须900 × 383>
- badge_target: <依据契约固定160 × 40，名义24px粗体700，圆角6；不随构图放大>
- badge_measurement_method: <真实像素检测/人工边界检查；方法、阈值、误差>
- badge_search_region: <仅搜索范围，不是测量结论>
- badge_outer_bbox_xyxy: <[x0,y0,x1,y1)，右/下边界不含>
- badge_measured_width_height: <实际W × H；允许158–162 × 38–42，不扩大容差>
- badge_ink_bbox_and_height: <实际字形墨迹边界及高度，不等同24px字号>
- badge_nominal_typography_evidence: <渲染设置或视觉核对及不确定性，不从墨迹反推字号>
- badge_radius_and_padding_review: <6px圆角目标的检查、最多±1px边缘误差、文字内边距>
- badge_geometry_status: pending
- exact_text_status: pending
- typography_and_radius_status: pending
- scientific_evidence_status: pending
- horizontal_composition_status: pending
- local_diagnostic_views: <完整图、360px宽、120px宽；方形/5:4的信息损失记录>
- design_contract_checked: pending
- backend_preview_checked: false
- completion_note: <任何失败均否决；提示词、尺寸检测或预览成功不等于成品通过>
