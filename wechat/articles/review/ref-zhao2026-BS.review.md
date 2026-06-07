---
publication_ref: ref-zhao2026-BS
zotero_key: CGKPKZ8I
doi: 10.1007/s12273-025-1379-7
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: drafting
source_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
---

# ref-zhao2026-BS 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`

## 证据来源

- WOEAI 官网条目: https://winddee.cn/zh-cn/latest/Publications.html#ref-zhao2026-BS
- DOI: https://doi.org/10.1007/s12273-025-1379-7
- Zotero: `CGKPKZ8I`
- PDF / 作者稿: 用户确认其为论文作者，可以直接使用该论文 PDF 中的图片；本稿图片已从 PDF 内嵌图片条带抽取并拼接为正文素材。

## 图片使用记录

1. Figure 1: Workflow of the proposed framework
   - 用途: 方法总览首图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-01-workflow.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - 公众号图注: 预计算 CFD 数据库框架：将城市微尺度风场计算前置，并面向快速预测和工程应用调用。
   - 移动端预览: pending WeChat backend mobile preview
2. Figure 2: Schematic diagram of block division of buildings in Shenzhen
   - 用途: 解释 `1 km x 1 km` 区块数据库
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-02-block-division.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - 公众号图注: 深圳建筑区块划分示意：城市区域被组织为可计算、可拼接、可入库的微尺度风场单元。
   - 移动端预览: pending WeChat backend mobile preview
3. Figure 21: Locations and observation environment of meteorological automatic stations
   - 用途: 展示实测验证数据来源
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-21-stations.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - 公众号图注: 气象自动站位置与观测环境：用现场监测数据检验区块 CFD 数据库的预测能力。
   - 移动端预览: pending WeChat backend mobile preview
4. Figure 25: Visual representation of wind speed and wind pressure data on WebGIS
   - 用途: 展示 WebGIS 平台应用效果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-25-webgis.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - 公众号图注: WebGIS 平台中的风速和风压数据展示：让预计算 CFD 数据库具备查询、展示和工程沟通能力。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes
- 呈现方式: direct text formula, not image
- 移动端预览: pending WeChat backend mobile preview

## 公开安全

- [x] No WeChat AppSecret, token, cookie, or credential appears.
- [x] No Zotero API key appears.
- [x] No private partner name appears.
- [x] No unconfirmed project status appears.
- [x] Reader-facing Markdown has no production notes, pending placeholders, or private paths.

## 发布前任务

- [x] 用 Zotero/PDF 核对作者、期刊、页码、DOI、公式和图题。
- [x] 导入已确认可用的原始高清图。
- [ ] 公众号后台手机预览正文、公式和图片。
- [ ] 发布后回填 `latest_published_url` 和 `wechat_status`。

## 检查记录

- image extraction: `pdfimages -all` from paper PDF, then `ffmpeg` vertical stitching of embedded image strips
- public-safety: passed (`/opt/homebrew/bin/python3.12 scripts/check-public-safe-content.py`)
- markdown whitespace: passed (`git diff --check` on WeChat article-related files)
- image links: passed (4 Markdown image links resolve to local public-safe assets)
- docs-check: skipped; this is a WeChat article update, not a Sphinx page update
