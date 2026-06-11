# RTD Homepage And Project Evidence Redesign

Date: 2026-06-11

## Goal

Redesign the WOEAI Read the Docs homepage so the first impression follows this approved priority order:

1. Engineering applications
2. Recruitment
3. Academic credibility

At the same time, remove the standalone `项目实践 Project Evidence` page by moving its content into the pages where readers need that evidence.

## Approved Direction

Use the engineering-problem homepage direction. The homepage should no longer read mainly as a group introduction plus page index. It should first answer: what engineering problems can WOEAI help explain or evaluate, and where is the public evidence?

The content-area logo on `docs/source/index.rst` should be removed. The RTD theme already uses `html_logo` from `docs/source/conf.py` to display the logo at the top of the sidebar, so repeating the same logo in the page body weakens the first screen.

## Site Structure

Delete `docs/source/Projects.rst` as a public page instead of keeping it as a compatibility shell or hidden full archive.

Remove `Projects` from the hidden toctree in `docs/source/index.rst`. The remaining top-level public navigation should keep the current docs-site shape:

- `Research`
- `EngineeringApplications`
- `Publications`
- `Teaching`
- `Privacy`

All internal references that currently point to `Projects` or its anchors must be updated to point to the new receiving sections.

Sphinx source files should remain reachable through a toctree unless intentionally excluded. Because this redesign deletes `Projects.rst`, the implementation should avoid leaving an orphaned source file behind.

## Homepage Content Design

The homepage should use a concise engineering-entry story:

1. Opening statement
   - Use a stronger headline such as: "把风与海洋工程研究转化为可验证的工程能力".
   - Keep the WOEAI full name on first mention.
   - Briefly identify the active domains: building structural wind resistance, floating offshore wind energy, wind/ocean environmental actions, and AI-enabled engineering modeling.
   - Do not add partner names, awards, facilities, quotas beyond existing recruitment planning, or new publication claims.

2. Primary action paths
   - Present three entry paths in this order:
     - `工程应用 Engineering Applications`
     - `加入 WOEAI Recruitment`
     - `学术进展 Academic Progress`
   - The engineering entry should be the most concrete. It should mention public application scenarios such as urban wind environment, high-rise wind response, floating wind turbine systems, floating concrete platforms, and wind-wave model testing.
   - Recruitment should stay direct: suitable backgrounds, annual recruitment planning, contact route, and application context.
   - Academic progress should remain a preview, not an archive.

3. Recruitment section
   - Preserve the current annual recruitment planning from `docs/source/index.rst`.
   - Compress policy-heavy prose. State that policy details depend on current public policy and team confirmation.
   - Keep the page useful for prospective master's students, doctoral students, and postdocs.

4. Latest academic progress
   - Continue showing the newest 10 RTD paper companion pages.
   - Keep the full narrative and archive role on `docs/source/Research.rst`.
   - Link readers toward `Research` and `Publications` for deeper evidence.

5. Footer/contact material
   - Preserve public contact channels, privacy notice, and site statement.
   - Keep factual boundaries: no unconfirmed partner names, project status, or institution-position claims.

## Project Evidence Migration

Move the former `Projects.rst` content into purpose-specific pages:

### Research Pages

`docs/source/Research.rst` should gain a concise section such as `公开科研项目支撑 Public Research Project Support`. It should explain that government and vertical research projects support the two public research families, then point to the two direction pages for details.

`docs/source/BuildingStructuralWindResistance.rst` should receive building-wind-related government project records, including:

- 2018-2021 national project on numerical atmospheric turbulent boundary layer generation;
- 2014-2016 national project on rough-wall-corrected equilibrium atmospheric boundary layer LES;
- 2014-2016 university-level project on three-dimensional self-balanced turbulent boundary layer wind fields;
- 2013-2015 university-level project on atmospheric boundary layer numerical wind tunnel LES;
- 2020-2023 municipal project on high-rise aerodynamic shape optimization under wind load and response.

`docs/source/FloatingOffshoreWindEnergy.rst` should receive floating-offshore-wind-related government project records, including:

- floating wind turbine system integrated analysis and optimization;
- FRP-steel composite reinforcement and seawater sea-sand concrete semi-submersible foundation design;
- floating offshore wind turbine balancing and vibration control;
- semi-submersible foundation technology;
- vertical-axis turbine pitch control where it is used as historical offshore-wind support.

### Engineering Applications Page

`docs/source/EngineeringApplications.rst` should receive enterprise project evidence and integrate it under application scenarios rather than as a separate archive:

- micro-scale typhoon wind field for transmission lines;
- wind tunnel testing and wind vibration analysis for an anonymized renewable-energy plant;
- wind-wave model testing for a reinforced-concrete semi-submersible floating wind turbine system;
- preliminary design for a reinforced-concrete offshore wind turbine local buoyancy foundation.

The enterprise evidence should stay anonymized and public-safe. It may show approved capability direction, problem type, year, and role. It should not disclose partner names, exact facilities, current cooperation status, or unpublished project details.

## Link And Anchor Requirements

Replace the old `projects-*` anchor dependencies with new anchors on the receiving pages.

Suggested new anchors:

- `research-public-project-support`
- `building-wind-project-support`
- `floating-wind-project-support`
- `engineering-enterprise-project-evidence`
- scenario-level anchors in `EngineeringApplications.rst` for any section that receives an inbound `:ref:` link

All changed links should use Sphinx `:doc:` or `:ref:` roles that pass a warning-as-error build.

## Constraints

- Treat this repository as a Sphinx documentation site, not an application package.
- Preserve the public taxonomy from `CONTEXT.md`: first-level research families are `建筑结构抗风` and `海上漂浮风电`; `数值风洞` remains a subdirection, not a first-level family.
- Do not invent new public facts.
- Do not turn homepage academic credibility into a long archive. The homepage should remain a concise visibility surface.
- Do not introduce a new frontend framework or theme change.
- Keep copy bilingual where the current public page already uses bilingual headings.

## Verification

Run the required docs check before claiming implementation complete:

```bash
./scripts/check-docs.sh
```

Also verify:

- `rg -n "Projects|项目实践|projects-" docs/source` returns only intentional historical or removed references.
- The homepage body no longer contains the duplicate `logoGroup.png` image.
- The RTD/sidebar logo still works through `html_logo`.
- `EngineeringApplications.rst` contains enterprise evidence without partner-name disclosure.
- `Research.rst` and the two direction pages contain government project support without recreating a standalone project archive.

## External Documentation Notes

The implementation should align with:

- Sphinx `toctree`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
- Read the Docs Sphinx theme configuration: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

Relevant points: Sphinx uses `toctree` to define document hierarchy and reachability; hidden toctrees define hierarchy without inserting body links; the RTD theme builds left navigation from toctrees and uses `html_logo` for the sidebar logo.
