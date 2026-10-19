# Complete reading-page citations: diagnosis and repair

Base: 310b5c9170f7fc027b0170071dab30440d74b4eb. Host: lcMacM4.local.
User scope: inspect all live Chinese notes and English highlights, repair missing complete citations and prevent recurrence. The user explicitly approved this round's main submission and deployment after tests and independent review.

## Verified pre-repair inventory

All 44 Chinese notes and six English highlights were actually navigated in the Mac browser. Citation containers were opened where present, body text read and computed visibility checked. After a temporary HTTP429, the unvisited pages alone were resumed at a lower frequency; the final inventory contains all 50 HTTP200 page results. No access/network settings were changed.

Nine Chinese pages had a visible complete-citation heading with only a record backlink; six further Chinese pages had no closing citation section. Twenty-nine Chinese notes and all six English highlights had visible citation content. The site has six English highlights, not 44 English translations. No CSS-hidden citation cases were found. A nonempty backlink is not a complete citation.

| Defect | Publication | Live URL |
|---|---|---|
| missing_citation_body | Numerical research on nonlinear liquid sloshing and vibration control performance of tuned liquid damper | https://winddee.cn/zh-cn/latest/paper-notes/ref-he2024-JBE.html |
| missing_citation_body | Large eddy simulation of wind loads on a long-span spatial lattice roof | https://winddee.cn/zh-cn/latest/paper-notes/ref-li2010-WAS.html |
| missing_citation_body | A revised empirical model and CFD simulations for 3D axisymmetric steady-state flows of downbursts and impinging jets | https://winddee.cn/zh-cn/latest/paper-notes/ref-li2012-JWEIA.html |
| missing_citation_body | Effects of inflow conditions on mountainous/urban wind environment simulation | https://winddee.cn/zh-cn/latest/paper-notes/ref-li2017-BS.html |
| missing_citation_body | Dynamics of a Y-shaped semi-submersible floating wind turbine: a comparison of concrete and steel support structures | https://winddee.cn/zh-cn/latest/paper-notes/ref-li2022-SOS.html |
| missing_citation_body | Super-resolution reconstruction of wind fields with a swin-transformer-based deep learning framework | https://winddee.cn/zh-cn/latest/paper-notes/ref-tang2024-POF.html |
| missing_citation_body | Training and application of graph neural networks for predicting structural responses targeted at tall building structures | https://winddee.cn/zh-cn/latest/paper-notes/ref-tang2025-JBE.html |
| missing_citation_section | Large eddy simulation of turbulent atmospheric boundary layer flow based on a synthetic volume forcing method | https://winddee.cn/zh-cn/latest/paper-notes/ref-wang2023-JWEIA.html |
| missing_citation_body | New consideration of lateral boundary treatment for meso- and micro-scale nested PBL simulations over complex terrain | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2021-AR.html |
| missing_citation_section | Multiscale modelling of planetary boundary layer flow over complex terrain: implementation under near-neutral conditions | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2021-EFM.html |
| missing_citation_body | A novel framework for urban geometry rapid reconstruction utilizing high-resolution stereo satellite imagery for wind environment assessment | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhao2026-BE.html |
| missing_citation_section | Wind tunnel and wave flume testing on directionality dynamic responses of a 10 MW Y-shaped semi-submersible wind turbine | https://winddee.cn/zh-cn/latest/paper-notes/ref-zheng2023-JRSE.html |
| missing_citation_section | Directionality Effects of Aligned Wind and Wave Loads on a Y-Shape Semi-Submersible Floating Wind Turbine under Rated Operational Conditions | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhou2017-E.html |
| missing_citation_section | Importance of platform mounting orientation of Y-shaped semi-submersible floating wind turbines: A case study by using surrogate models | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhou2020-RE.html |
| missing_citation_section | Global sensitivity study on the semisubmersible substructure of a floating wind turbine: Manufacturing cost, structural properties and hydrodynamics | https://winddee.cn/zh-cn/latest/paper-notes/ref-zhou2021-OE.html |

## Root cause and minimal repair

Source-level omissions predate the 981cd76 reader layout and 310b5c9 publication-list refactor. For example, BE's original source-creation commit already had a complete-citation heading followed only by a backlink. Existing syntax/link tests did not require a complete closing citation body. The legacy converter also had an independent warning-and-omit path and a dependency on presentation RST; this is removed without claiming it created every affected page.

A shared registry validator and Sphinx projection provide complete, source-backed citations to every actual reading page. Input validation runs before building; a post-build check verifies every real HTML body and recorded DOI link. Mandatory Chromium CI reads all pages at desktop and narrow widths, including visibility and clipping; negative DOM fixtures prove the checker fails on hidden/missing content. New pages join by source inventory rather than a hardcoded list. Existing science RST, original reference lists, covers, homepage eligibility/problem/contribution and current reader/list layout remain intact.

One unsupported DOI-style placeholder was discovered in GYJZ 2023 metadata. Its existing scientific review explicitly says the supplied first-release paper has no supported DOI. Only that unsupported DOI is removed, with a separate documented non-content review, original evidence preserved and all 40 prior current WeChat qualifications retained. No replacement DOI or scientific claim is invented. Another record has a valid DOI only in structured CSL; projection uses that existing value without changing its record. The two known first-release entries (QHDXXB and GYJZ) retain their already-audited first-release/pagination limits through generic website citation notes, preventing the shared projection from losing source-version context.

## Protected parallel work and release checks

The pre-existing untracked project/plans/2026-10-19-reader-pages-ui-review.md belongs to another session and is excluded from this task. Preserve its exact bytes. No WeChat article/API operation is authorized or performed. Before submission verify the current remote, exact task file hashes, standard docs gate, browser gates and independent Spec/Standards reviews. Verify the exact pushed commit's CI/RTD and all live reading citations after deployment. Temporary raw browser logs and screenshots stay local outside committed content.
