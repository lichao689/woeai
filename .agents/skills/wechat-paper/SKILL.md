---
name: wechat-paper
description: Use when generating, reviewing, or updating WOEAI WeChat Official Account paper introductions, evidence notes, figures, formulas, and backlog state. Coordinate separately requested independent RTD full-paper deep dives through project/guides/paper-deep-dive-rst.md. Covers cloud content production, offline rendering, and explicitly authorized official draft API delivery; never derive a new RTD deep dive from WeChat Markdown.
---

# WeChat Paper Article Skill

为一篇已发表的 WOEAI 期刊论文制作公众号导读：读者正文、公开素材和独立的
review 记录。本技能只规定**执行顺序**；规则内容以下表文件为准，不在此复述。

| 需要什么 | 读哪里 |
| --- | --- |
| 项目边界、检查命令、授权要求 | `AGENTS.md` |
| 术语 | `CONTEXT.md` |
| 源文件获取、证据定位、原图抽取 | `project/guides/paper-sources-and-evidence.md` |
| 写作规则与文章结构 | `wechat/STYLE.md` |
| 去 AI 味审校流程与示例 | [references/natural-scientific-writing.md](references/natural-scientific-writing.md) |
| 正文 / review / 清单模板 | `wechat/templates/paper-explainer.md`、`paper-review.md`、`review-checklist.md` |
| 渲染、公式 SVG、草稿 API、状态回写、凭据 | `wechat/README.md` |
| 云端运行环境 | `project/guides/cloud-wechat-workflow.md` |
| 封面 | `wechat-cover` 技能 |
| RTD 全文精解（独立任务） | `project/guides/paper-deep-dive-rst.md`、`project/guides/rtd-translation-style.md` |

## 不可越过的边界

- 一篇文章只讲一篇论文；公众号导读与 RTD 精解相互独立，不互相生成或覆盖。
- 不编造论文没有的事实；源文件缺失时停下并记录 `需要同步 PDF 或提供作者稿`。
- 内容制作阶段不读取凭据、不联系微信、不上传图片。
- 创建或更新草稿前，必须说明将读取私有凭据、上传已批准图片、操作哪个草稿，
  并得到明确确认（如“确认创建公众号草稿”）；“继续”“可以”不算。
- 不自动发布、群发或点击后台发布按钮。

## 执行步骤

1. **选题与核对。** 在 `docs/data/publications.json`（生成视图为
   `wechat/backlog/selected-papers.yml`）确认 `publication_ref`、
   `custom.content_production: included`、DOI 与 `docs/source/Publications.rst` 条目。
2. **取源与核证。** 按源文件指南获取 PDF，建立事实核对单：结论、数字（指标 / 基线 /
   工况）、原文定位、限制、原文内部矛盾。
3. **写论证线。** 先在 review 的“工程叙事证据卡”里写出一句话论证线，
   写不出就回到论文。
4. **选图。** 按源文件指南抽取 3–5 张原图到 `wechat/assets/public-safe/<publication_ref>/`。
5. **起草正文。** 从 `wechat/templates/paper-explainer.md` 起草
   `wechat/articles/draft-public-safe/<publication_ref>.md`，结构按 STYLE 第 2 节。
   交付前删除所有尖括号提示与注释。
6. **去 AI 味审校。** 按 natural-scientific-writing.md 的六步执行，并逐项对照第 2 节清单。
7. **写 review。** 从 `paper-review.md` 建立或更新
   `wechat/articles/review/<publication_ref>.review.md`。已有核验记录的 review 若改动会使
   注册表指纹失效，改稿记录另建 `<publication_ref>.language.review.md`（同样须含两个必需小节）。
8. **封面（如在范围内）。** 交给 `wechat-cover` 技能，遵守文字确认门槛。
9. **离线检查。** 运行下面的命令，逐项核对 `review-checklist.md`。
10. **草稿投递（仅在用户要求时）。** 按 `wechat/README.md` 的授权流程执行；已有草稿默认更新，
    只有用户要求时才新建。只有成功的 live 操作才能推进状态。
11. **人工发布之后。** 用户确认发布后回填 `latest_published_url` 与状态。

后台预览中改动的文字，先改回 Markdown 源文件再重新生成草稿；不要同步到 RTD。

## 离线检查命令

在仓库根目录：

```bash
./scripts/setup-cloud-workflow.sh          # 首次或环境更新后
source scripts/cloud-workflow-env.sh
python3 scripts/check-public-safe-content.py
python3 wechat/tools/wechat_draft.py preflight --publication-ref <publication_ref> --theme academic-clean
python3 wechat/tools/wechat_draft.py dry-run --publication-ref <publication_ref> --theme academic-clean
git diff --check
```

这些命令不读取凭据、不联系微信。`config-check`、`token-check`、`ip-check` 属于单独授权的
诊断，不放进这组命令。纯公众号正文与 review 改动不需要 Sphinx 构建（网站标签来自注册表
`custom.rtd.public_title`，不随公众号标题变化）。改动注册表或站点页面时，按 `AGENTS.md`
运行注册表与 `./scripts/check-docs.sh` 检查。

## 交付时报告

- 正文、review、素材路径；
- 使用的源文件证据与仍未解决的事实问题；
- 图片复用与手机预览要求、公式浅色 / 深色预览要求；
- 每项检查的结果：通过、失败、受阻或未运行，以及原因。

手机后台预览检查公式和图片之前，不称文章“可发布”。
