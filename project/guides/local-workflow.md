# WOEAI 本机工作环境

后续工作使用用户指定的本机主仓库。临时副本用于隔离检查时，须有明确授权；已有
未提交工作、私有资料和历史版本应先保全，再更新主仓库。`AGENTS.md` 是唯一 agent
入口，详细规则按其中的权威指南执行。本文不保存机器绝对路径、账号或凭据。

## 安装与启动

要求 Python 3.12+、Node 20+、npm、Git；PDF 工具使用 Poppler 的 `pdfinfo`、
`pdftotext`、`pdftoppm`、`pdfimages`。中文字体以本机实际安装为准，不把字体回退
当作与其他机器相同的版式。

在主仓库根目录执行：

```bash
./scripts/setup-local-workflow.sh
bash
source scripts/local-workflow-env.sh
```

默认 shell 为 zsh 时也先进入 bash，再 source；每个新 bash 会话都要重新加载。
两个 local 入口复用现有共享脚本，名称含 cloud 不会启动云端环境。安装会访问
Python/npm 包仓库并写入 `.venv`、`wechat/runtime/node_modules` 和忽略的缓存。
它不读取公众号凭据、不调用微信 API。

Python 依赖按 `wechat/runtime/requirements.lock.txt` 锁定版本，文档依赖另由
`docs/requirements.txt` 补齐并执行 `pip check`；Python 锁未包含发行包哈希。
npm 使用 `package-lock.json` 与 `npm ci`，Node/npm 和系统字体不属于完全固定的环境，
不承诺跨系统像素一致或环境完全可复现。

## 离线检查

```bash
./scripts/check-docs.sh
node --test tests/frontend/*.test.cjs
./scripts/check-cloud-workflow.sh
```

source 后，标准文档检查使用本仓库 `.venv` 和 `docs/_build/html`；不加载 local
环境时，标准脚本仍使用其默认临时环境和构建目录。文档构建会重建输出目录，不能
将独有原始资料放在构建产物目录中。完整门禁包括公开安全、登记/生成产物检查、
Python 测试和严格 Sphinx 构建；前端及离线微信检查按变更范围另验。

离线成功不代表科学审核、实际账号/索引核验、后台手机预览或发布完成。真实微信
操作仍须明确授权，核对既有草稿并防止重复；不自动发布或群发。

## 原论文与私有运行资料

ChatGPT Library 为原论文主源，本机 PDF 为缓存；优先采用用户后补的完整版本。
具体获取、完整性、身份及版本差异规则只由
[论文源文件与证据指南](paper-sources-and-evidence.md)维护；不能因未找到本地缓存
或哈希不同就判断用户未提供过。Zotero 原库保留，题录核对保持只读。

缓存、原文提取、整页图、草稿映射、操作 journal、回查及恢复材料只放忽略的
`wechat/.local/` 等私有目录；不能进入公开 Git。凭据和 token 继续使用仓库外的
安全配置，不复制到项目、恢复资料的普通交付包或对话。迁移时保留旧版本并逐文件
核验，公开脱敏成功回执不能代替私有原稿、目标映射和防重复操作日志。

清理旧 clone 前，确认所有分支提交已保全、独有未提交/ignored 资料已迁移、没有
运行任务依赖，并验证恢复备份。先使用可恢复归档；不通配符删除父目录，不清理
Zotero、Library 或具有独立未提交工作的预览仓库。

## 历史记录

[2026-10-07 本机迁移摘要](../archive/local-workflow-2026-10-07.md)只描述当次观察；
其提交号、文件数量、测试数和运行状态不代表当前状态。
