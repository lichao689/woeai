# ref-chen2024-POF 封面简报

## 当前有效封面（2026-10-14）

本节为当前选图唯一入口。下方历史记录中的旧分类、旧路径、旧评分和旧后台说明均不代表本次状态。

- cover_design_contract: `WOEAI-cover-v5`
- current_secondary_direction: `数值风洞`
- cover_text_confirmation: `user-confirmed-batch-editorial`；用户已授权本批依据原文拟定并复核后采用，不逐篇重复选五选一。
- current_cover_text: `数值风洞 | 压住虚假脉动 / 三种 RAPF 方法对比`
- selected candidate: `20261014-v5`
- final cover path: `wechat/assets/public-safe/ref-chen2024-POF/cover-wechat-900x383-20261014-v5.png`
- current_final_sha256: `4e107919ed4a97c7903c0d506e321f55f4ba77f8320730682d296ecf80a4fc6f`
- final_dimensions: `900 × 383 px`
- current_local_state: 本地全图、宽图及缩略图诊断通过，独立视觉复核通过。
- rendering_route: 工程插画由内置 imagegen 生成；文字与徽标按本轮用户授权固定排版。最终文件是明确记录的组合排版，不宣称一次生成直出。
- typography: Noto Sans CJK SC；徽标 24 px / 700，主标题 48 px / 700，副标题 24 px / 400，期刊年份 18 px / 400；全部水平正体。
- badge_actual_outer_bounds: `[36, 32, 196, 72]`，实测 160×40 px；圆角渲染参数 6 px。
- badge_actual_ink_bounds: `[69, 40, 162, 64]`，实际墨迹高 24 px；与名义字号分列。
- badge_geometry_gate: `pass`；实际字形、内边距与圆角同时目视检查。
- evidence_anchor: 已审核三种 RAPF 方法比较与孤立高层压力验证。
- selection_and_science_review: 清理旧文字并修正方法示意；拒绝初版第三路神经网络外观。保留三种方法的定性比较与孤立建筑，不冒充准确算法框图、压力等值图或定量结果。
- source_scope: 概念插画，不是论文计算图、实测照片、原图尺寸复刻或已建成项目。
- local_preview: 已检查完整 900×383、360 px 与 120 px 宽图；缩略图只诊断分类、主对象及标题层级，不要求最小图所有小字可读。
- current_backend_state: 本次上传与回读以同篇正式投递记录为准；本地审核不等于已提交。
- backend_preview_status: `pending`；实际微信手机端预览尚未核验。
- rtd_cover_state: 本轮不改既有 RTD 封面引用。

## 历史记录与本轮过程（不作为当前选图入口）

### ref-chen2024-POF 封面简报

- 文章标题: 数值风洞 | LES 高层建筑风荷载评估中人工压力脉动抑制方法对比
- 分类标签: 数值风洞
- 期刊年份: Physics of Fluids · 2024
- 核心问题: 高层建筑风荷载 LES 中，入口质量失衡和压力参考处理会引入人工压力脉动，需要比较 IMC、DFC 和 LPC 三类 RAPF 方法的适用取舍。
- 关键方法/发现: IMC 与 DFC 更适合全流场抑制人工压力脉动，LPC 更能保持原始入口湍流但具有局部性；只看整体力/力矩可能掩盖局部表面风压污染。
- 目标读者: 关注 WOEAI 论文、数值风洞、LES 入流、建筑结构抗风和工程风荷载评估的公众号读者
- 避免: 私密项目名称、未确认合作方、复杂小字、虚构 UI 标签、夸张宣传语、泛化科技壁纸、与高层建筑/LES/RAPF 无关的视觉
- cover_execution_mode: image-gen
- cover_text_confirmation: user-confirmed
- confirmed_cover_text: 数值风洞 | 压住虚假脉动 / 三种 RAPF 方法对比
- confirmed_text_mode: image-gen-text
- publication_metadata_line: Physics of Fluids · 2024
- confirmation_note: confirmed in chat as option 1

#### 候选方向

1. research scene: 高层建筑置于 LES 数值风洞中，风流线穿过计算域，右侧显示建筑表面风压云图或压力测点。
2. method: 用三条方法路径表达 IMC、DFC、LPC 的对比，底部技术路线从入口湍流、RAPF 方法到建筑风压误差。
3. engineering impact: 强调“局部风压可信度”，以高层建筑表面压力云图、测点散点和整体力谱形成工程判断场景。

#### 封面文字选项记录

1. `数值风洞 | 压住虚假脉动 / 三种 RAPF 方法对比`
2. `数值风洞 | 让压力更可信 / LES 风荷载方法对比`
3. `数值风洞 | 入口如何修正 / 人工压力脉动抑制`
4. `数值风洞 | 别被假脉动骗 / 看懂 LES 风压误差`
5. `数值风洞 | 三法压住脉动 / IMC DFC LPC 的取舍`
6. Custom cover text supplied by the user

#### 生成要求

- 模式: image-gen
- 文本模式: image-gen-text
- 输出尺寸: `900 x 383 px`
- 比例: about `2.35:1`
- 左侧 `38-45%` 为融合式文字安全区，不使用硬分割、白卡片或明显竖线。
- 右侧 `55-62%` 为高层建筑 LES、入口湍流、压力云图或方法对比的工程视觉。
- 底部技术路线条: 入口合成湍流 -> IMC/DFC/LPC -> 空域压力检查 -> 建筑表面风压误差。
- 只允许出现已确认的三段中文主文字和 `Physics of Fluids · 2024` 元数据行；不添加英文翻译、假图例、假 UI、地图标签、Logo 或水印。

#### 生成记录

- 用户确认封面文字: `数值风洞 | 压住虚假脉动 / 三种 RAPF 方法对比`
- 最终封面来源: user-provided cover image supplied in chat after option 1 confirmation
- 源图副本: `wechat/.local/cover-candidates/ref-chen2024-POF/cover-option1-user-provided-source.png`
- 前序候选记录: three local programmatic composition candidates were generated and then superseded by the user-provided cover image
- 前序候选总览: `wechat/.local/cover-candidates/ref-chen2024-POF/cover-option1-contact-sheet.png`
- 正式封面: `wechat/assets/public-safe/ref-chen2024-POF/cover-wechat-900x383.png`
- 正式尺寸: `900 x 383 px`
- 本地裁剪预览: `wechat/.local/cover-previews/cover-wechat-900x383.cover-preview.html`
- 质量评分: article_specificity=5, main_subject_clarity=5, click_appeal=5, engineering_credibility=5, small_thumbnail_readability=5, crop_safety=5, text_quality=5
- WeChat 后台手机预览: pending

#### 系列规范迁移（2026-10-05）

- cover_design_contract: `WOEAI-cover-v2`
- 规范: [统一网格、字号、配色与裁切](../../../.agents/skills/wechat-cover/references/cover-standards.md)
- 本文方向: `数值风洞`，依据对应正文标题；仅用该方向固定色彩令牌，不另起画风
- 证据入口: [本文事实审阅](ref-chen2024-POF.review.md)；生成前完成工程叙事证据卡
- 文字来源: 保留历史确认记录，旧请求文字不自动视为新一轮批准；缩短或改写须重新确认
- 科学元素: 选择一个已核实主对象；路线为已验证输入 → 方法 → 输出；潜在用途与结果分开
- 构图: 900 × 383 px；左文区 x=36–396；关键科学对象 x=420–620、y=56–276；底部三节点路线
- 历史复用限制: 既有提示词、概念和选图仅供溯源，不直接当新一轮完整提示词；重新按 v2 及审阅证据编写
- migration_status: specification-updated; existing-image-not-regenerated
- design_contract_checked: pending; 尺寸一致不证明旧图符合新布局、字级或科学对象裁切
- backend_preview_status: unchanged; 此次简报维护没有新增后台手机预览
