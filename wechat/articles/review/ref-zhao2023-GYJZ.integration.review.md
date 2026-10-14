# ref-zhao2023-GYJZ 第四批六篇网站与工作流接入复核

## 源文件获取记录

沿用 [ref-zhao2023-GYJZ.review.md](ref-zhao2023-GYJZ.review.md) 的已授权来源、完整 11 页独立科学内容审核及事实定位。当前核验副本 SHA-256：`c86a1e52d74d58bddec7dc9b065552204c58703c0bc6968cf0c859811c9ae8d1`。
历史来源 SHA-256：`c86a1e52d74d58bddec7dc9b065552204c58703c0bc6968cf0c859811c9ae8d1`；与当前副本相同。
本次接入不下载、不替换来源，也不重新声称全文 PDF 审核。

## 关键事实证据定位记录

原 review 保留原文页码、公式、表、图及参考文献覆盖证据。原批六篇冻结168项公开内容；本版其中167项逐字节不变，唯本篇RTD末尾一个相关论文条目引用改为显式链接标题，详见文末限定修复记录。
最终封面及纯 RST 空格/标题下划线的限定变更已在原 review 分开登记。本接入不改任何科学正文、摘要、公式、图片或作者。

## 导航与书目差异

短导航标题登记为：`结构抗风 | 输电塔强风首次超越易损性`。该字段与正文 H1 独立：完整 RTD 页标题按规范保留“论文精解”，导航短标题保留方向前缀、不加冗余后缀。
仅补学术成果所属“工程结构抗风 / 结构抗风”的隐藏子目录和本篇引文的精解链接，保持 anchor/URL 不变；未运行联网全量 Zotero 更新。
本篇不修改书目字段、作者名单或通讯标记。

## 证据与状态边界

来源身份与既有科学内容核验已通过，RTD kind=full_paper，最终接入的浏览器/标准构建尚待确认，故状态保留 awaiting_audit。
公众号为 awaiting_review，保留官方离线 preflight/dry-run/SVG 渲染结果；未创建后台草稿、不填写后台成功时间或私有标识，三个实际手机预览项均为 false。
没有实际微信手机浅色/深色及发布证据，不标记 ready_to_publish 或 published。本批未修改旧17篇任何正文、原图或真实投递历史。

## 冻结内容哈希

- `docs/source/paper-notes/ref-zhao2023-GYJZ.rst`：`e318f9d3944a9287b791663638de31e367ff54c6a56a91c4509223625079c04c`。
- `wechat/articles/draft-public-safe/ref-zhao2023-GYJZ.md`：`f1edde722c6662609180d0c4c7e87c3ad5ddea0c2dd281e5338e8f3a1bd1ce60`。
- `wechat/articles/review/ref-zhao2023-GYJZ.review.md`：`5222b5e6bab52c4505f43ed9b03203ea6f625d3824b5c4fda810e73c965fba81`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/cover-brief.md`：`f085d3c7a42d940d0cf27bab4a3fb5106fff1172a49b896769abddfdab2598f6`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/cover-wechat-900x383-20261014-v5.png`：`a527c5659b870596ceea8defab5b54a7482b8ac6de9c3763940837ee581cfcab`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig01.png`：`98b2fe159f6daa984a58745be1633698d0c96cd62d04778d1b535ce52905bd59`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig02.png`：`b47d23f21c20f5cd2128714e1d105283765878e12c44c90165dee0acc0230027`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig03.png`：`97078c428f9bc66cfb0f2a04e0ae702e3413a1ee15c49a907e8681e603f3d795`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig04.png`：`541f0df5591ac076cc3db781d2304164acecac032bd53a49756d5c11bafe624b`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig05.png`：`b18d4e519f93209c5822d793e83f45f50dced8d0e93e7c779ee857d364b504e0`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig06.png`：`04c596b8505195ae9d3b687b66a2bcee3229a2d91e98597f62f5e3ae073d7ebd`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig07.png`：`26d54b7f3c70b7f3751689356e8689a3cc8bbc59d4e6f4d35bc9ad4c5350b94d`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig08.png`：`830d7d56c0e7af8293f85666a222f7225e9a50463968128536fc5c5d63dcc534`。

## 2026-10-14 v4 页尾交叉引用最小修复

标准整站构建发现：学术成果中的稳定论文锚点位于引用正文前，没有可供裸ref角色自动取用的节标题。本版仅将页尾相关论文条目的ref角色补为显式链接标题“输电塔强风首次超越易损性”，目标ref-zhao2023-GYJZ和链接去向不变。逆向删除该显式标题即可逐字节恢复前版RST；所有科学正文、摘要、公式、表值、参考文献、作者、封面/原图与公众号MD均不变。

以学术成果原有、没有节标题的正文锚点单独复现：原写法在warnings-as-errors下失败，显式标题修正后通过并生成实际可点击锚链接。所有待接入RST还作了同类裸论文引用只读扫描；未扩大修改其他文稿。本限定语法复核不替代标准全站或实际浏览器验收，状态不因修复直接升级。
