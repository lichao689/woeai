# WOEAI Peer Site Benchmark

Date: 2026-06-06

Decision owner: WOEAI site owner / implementation agent

Outcome priority: 招生 Recruitment > 产业合作 Industry collaboration > 学术可信度 Academic credibility

## Purpose

This benchmark informs the first upgrade cycle for the WOEAI website. The goal is not to copy another site. The goal is to identify which public patterns help a research group convert qualified applicants, make industry cooperation legible, and support academic credibility.

## Benchmark Summary

| Site | URL | First-Viewport Signal | Recruitment Path | Cooperation Path | Proof Signals | Notes For WOEAI |
| --- | --- | --- | --- | --- | --- | --- |
| Industrial AI Center | https://www.iaicenter.com/join-the-center | Direct hiring language and open roles | Explicit MS/PhD/postdoc call with email subject format | Industry AI framing and real-world data emphasis | Research themes, partner-facing AI language | Useful pattern for WOEAI recruitment: tell applicants exactly who should apply and how. |
| Urban Resilience.AI Lab | https://www.urbanresilience.ai/opportunities | "Join our lab" plus mission and values | Clear PhD/postdoc/visiting scholar/undergraduate opportunities | Mentions global and industry partners | Alumni, interdisciplinary scope, response expectations | Useful for tone: applicant-centered, explicit expectations, avoids hiding contact steps. |
| Geoelements Research Group | https://autonomy.oden.utexas.edu/geoelements-research-group | Short identity around Physical AI | Contact email visible through PI profile | Research applications in autonomous/physical systems | Grants, open-source tools, research pipeline | Useful for AI positioning: name concrete capabilities instead of generic "AI empowerment". |
| EOLOS Wind Energy Research Consortium | https://eolos.umn.edu/ | Consortium identity and mission | Workforce training is visible but not a direct applicant path | Industry-driven research is central | Field-scale demonstrations and current projects | Useful for WOEAI industry page: explain why partners should care before listing projects. |
| WindSTAR I/UCRC | https://www.uml.edu/Research/WindSTAR/about/ | NSF Industry/University Cooperative Research Center | Student training appears as part of mission | Cooperation model is explicit | Research areas, member needs, university capability | Useful for partner copy: structure around industry needs and university capability. |
| National Wind Institute, Texas Tech | https://www.depts.ttu.edu/nwi/research/ | Long-running wind research authority | Education/workforce appears institutionally | External partners are part of institute identity | Research history and interdisciplinary scope | Useful for credibility: heritage and breadth help only after user paths are clear. |
| South China University of Technology Wind Tunnel Laboratory | https://www2.scut.edu.cn/wind/ | Chinese wind-engineering institutional identity | News and student achievements imply training pipeline | Lab/platform credibility for engineering services | Lab status, news, awards, facilities | Useful Chinese reference: credible platform facts and recent updates matter. |
| Tongji Bridge and Structural Wind Resistance Laboratory | https://weng.tongji.edu.cn/gk.htm | Chinese structural wind resistance lab identity | Mentions large numbers of trained graduate students and postdocs | Lab history and wind tunnel capability imply cooperation | Staff, facility history, talent training | Useful Chinese reference: training outcomes and platform history can support recruitment. |

## Patterns To Adopt

- Put recruitment above generic research navigation. Applicants should see fit, openings, and contact steps before exploring the archive.
- Make industry cooperation a first-class path. Do not bury partner signals under a raw project list.
- Use concrete AI capabilities: 3D Gaussian Splatting, graph neural networks, turbulence generation, wind-field reconstruction, and optimization.
- Show proof close to each user path. Recruitment proof differs from industry proof and academic proof.
- Give public-safe states for missing material. Empty sections should say they are being updated or stay hidden.

## Patterns To Avoid

- A documentation-theme homepage that leads with a generic toctree.
- Half-translated pages where Chinese and English labels are mixed without a clear reader path.
- News pages without an owner, cadence, or source.
- Broad claims like "AI empowered" without representative publications or project evidence.

## First-Cycle Theme And Page Decision

Use Sphinx and ReadTheDocs for the first upgrade cycle, but do not treat the default RTD layout as the final homepage design.

Decision:

- Keep `sphinx-rtd-theme` for this first implementation because current blockers are content architecture, source quality, and verification.
- Use CSS and page structure to make the homepage recruitment-first.
- Revisit `pydata-sphinx-theme` or a custom static site only after the first-cycle content, source packet, and verification gates are stable.

## First-Cycle Page Strategy

1. Homepage: recruitment-first, then industry cooperation, then academic proof.
2. Recruitment page: who should join, openings, requirements, benefits, contact path, and public-safe unknowns.
3. Industry collaboration page: partner-facing capability summary, project evidence, cooperation fit, contact path.
4. Research overview: connects three research directions to publications and projects.
5. Publications and projects: proof archive, not the first user journey.

## Open Questions For Site Owner

- Are the current annual master, PhD, and postdoctoral opening numbers still valid?
- Is the postdoctoral salary/subsidy text current for 2026?
- Which project examples are approved for partner-facing cooperation copy?
- Are there lab/facility/student photos that can be published?
- Should GroupNews have an owner and update cadence, or remain a verified recent-updates page?
