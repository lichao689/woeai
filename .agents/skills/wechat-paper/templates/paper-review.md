---
publication_ref:
doi:
research_family:
subdirection:
publication_mode: first_publish
wechat_status: drafting
wechat_author:
source_checked: false
copyright_checked: false
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
---

规则入口：[writing-standards.md](../references/writing-standards.md)；[自然写作指南](../references/natural-scientific-writing.md)。

# <publication_ref> 发布说明

填写规则：源文件与证据见 `project/guides/paper-sources-and-evidence.md`；
写作检查见 `writing-standards.md` 与 `review-checklist.md`。
本文件公开：只写存储类别和证据定位，不写私有绝对路径、附件标识、凭据或长段原文。

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/<publication_ref>.md`
- RTD 论文精解页: `docs/source/paper-notes/<publication_ref>.rst`
- 封面素材: <public-safe 路径，或“未生成”>

## 源文件获取记录

- 元数据来源: <Zotero Web API / Zotero Desktop Local API / 注册表快照 / 不可用>
- 附件记录: <已核对 / 不可用>
- 本地 PDF: <存在 / 缺失>
- 已选 PDF 类型: <作者稿 / 出版社正式版 / OA PDF / 预印本 / 其他 / 不可用>
- 低优先级原因: <不适用 / 高优先级缺失 / 不可读 / 法律上不安全 / 图像不适用>
- 私有存储类别: <私有工作区 / Zotero 私有附件 / 未记录>
- Zotero Web API `/file`: <无需 / 已尝试 / 不可用 / 失败>
- 网页 PDF 下载: <未使用 / 用户于 YYYY-MM-DD 批准的公开合法来源：<来源名称>>
- 摘要依据: <Zotero `abstractNote` / PDF 摘要 / 作者稿 / 不可用>
- 正文证据依据: <PDF 正文 / 作者稿 / 仅公开元数据 / 不可用>
- 图片依据: <PDF 嵌入原图 / 作者稿原图 / 重绘 / 不可用>
- PDF 文件页数: <N>

## 关键事实证据定位记录

页码一律为 `PDF file page N`；未核页写 `pending PDF page audit`。

- 摘要: <来源与位置>
- 核心结论与数字:
  - <文章用法> — <PDF file page N，章节 / 表号；指标、基线、工况>
- 所用原图:
  - 论文图 N — PDF file page N
- 所用公式:
  - <原式 (N) — PDF file page N / 编辑解释式，依据 PDF file page N 的……>
- 原文内部矛盾: <两处位置与正文处理方式；无则写“未发现”>

## 工程叙事证据卡

- 本篇主要读者与阅读目标: <希望读者理解的具体问题、判断或方法；兼顾规范中的其他读者>
- 论证线（一句话）: <现有做法在 X 下不够 → 本文改了 Y → 用 Z 检验 → 结果 W → 适用到 V>
- 工程问题与决策者: <真实约束与所需判断，不虚构项目>
- 基线及其局限: <原文比较对象及证据位置>
- 具体改动: <实际改变的环节；证据位置>
- 机制与验证: <解释与验证设计；相关与因果分开>
- 已验证结果: <指标、基线、工况、数值；证据位置>
- 潜在用途: <输入、输出、迁移前所需验证；不是已部署>
- 适用边界: <假设、未测工况、不可推出的结论>
- 标题与导语依据: <对应的已核实事实>
- 从论文到工程的价值主线: <支持什么工程判断、改善什么设计或分析能力>
- 应用潜力的证据与推论: <原文定位；区分已验证结果和有依据的扩展，不虚构落地>
- 结尾编辑判断: <单段；价值占主体；末句条件简短；不复述前置栏目，不以字数比例替代语义审阅>
- 正文限定保留位置: <重要条件所在章节；结尾压缩没有删掉这些条件>
- 封面钩子依据: <不强于正文；文字确认状态见 cover brief>

## 写作审校记录

- 导语首段可单独作为微信摘要: <是 / 需修改>
- 正文各节分工（问题 / 方法 / 证据 / 边界）及是否复述摘要: <说明>
- 自然写作清单（natural-scientific-writing.md 第 2 节）检查结果: <说明>
- 数字、单位、条件、归因与确定程度对照: <通过 / 修改项>
- 是否新增原文不支持的事实、经历、情绪、动机或因果: <否 / 需修改>

## 图片使用记录

1. 论文图 N:
   - 用途: <在论证中的作用>
   - 素材文件: <public-safe 路径>
   - 来源 / 复用: <团队作者原图 / 已确认复用权利>
   - 抽取方式: <pdfimages / 条带拼接 / 页面渲染裁切>
   - 移动端预览: 未检查

## 公式检查

- 使用公式: <原式 (N) / 编辑解释式>
- 渲染路线: `mathjax-svg`（使用其他路线时写明原因）
- 手机浅色模式: 未检查
- 手机深色模式: 未检查

## 链接

- 延伸阅读: <核实过同号正式发表证据的文字链接，默认3篇（调用方可调，正文必要引用另算） / 省略：无合格相关文章>
- 相关文章依据: <同二级方向；跨方向时逐项记录 publication_ref 与相关理由>
- 正式链接与证据: <见注册表 publication_record 的审定标题、永久URL、来源及证据文件；不填预览链接>
- 自动装配检查: <延伸阅读不重复，AI声明仍唯一且最后；未自动修改已发表文章>
- `content_source_url`: <默认 RTD 精解页 / 显式覆盖 / 显式留空>

## 发布前任务

- [ ] 作者、期刊、DOI、公式、图题与原文一致。
- [ ] 按 `review-checklist.md` 完成写作与公开安全检查。
- [ ] 实际微信手机浅色预览：正文、公式、图片、链接。
- [ ] 实际微信手机深色预览：正文、公式、图片、链接。
- [ ] 发布后回填 `latest_published_url` 与状态。

## 检查记录

- public-safety: <命令与结果>
- preflight / dry-run: <命令与结果>
