# RTD 论文精解 RST 提示词

把此篇 Journal Paper 写成 RST 格式的论文精解。不要编造论文没有的信息。

写作要求：

- 标题使用中文精解题名；页面顶部保留 `.. _paper-note-<publication_ref>:` 锚点。
- 标题下方预留精简版微信公众号文章链接；没有已发布链接时写“精简版微信公众号文章：待发布”，不要伪造 URL。
- 按论文 PDF/批准稿的章节顺序忠实翻译和整理，保留摘要、引言、方法、结果、讨论/结论、参考文献等原有结构。
- 保留完整公式、公式编号、变量含义、图、表、图表编号、文内引用和参考文献。公式用 Sphinx `.. math::` 或 `:math:`，不要用截图替代可编辑公式。
- 图表从pdf源文件中提取，保留原文最高的清晰度，并在 RST 中使用相对路径；不得引用本机私有绝对路径。
- 图题、表题和图表说明用中文，忠实对应原文；必要时保留英文术语。
- 文内参考文献引用要能对应到末尾参考文献列表；不要删除引用链。
- 页面末尾保留“完整引用”小节，并链接到 `:ref:`WOEAI 学术成果页对应条目 <<publication_ref>>``。
- 可在末尾加入“相关论文精解”站内导航，但只能链接已经存在的 `docs/source/paper-notes/*.rst`。
- 公开内容不得包含凭据、私有路径、抓取日志、未确认授权说明、待办清单或 `pending` 占位。

完成后运行：

```bash
python3 tools/publications/artifacts.py --check
python3 scripts/check-public-safe-content.py
./scripts/check-docs.sh
```
