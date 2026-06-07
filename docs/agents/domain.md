# Domain Docs

How the engineering skills should consume this repo's domain documentation when
exploring the codebase.

## Before exploring, read these

- `AGENTS.md` at the repo root for WOEAI site priorities, content boundaries,
  required checks, and editing rules
- `CONTEXT.md` at the repo root as the editable WOEAI project glossary and
  semantic constraint source, if it exists
- `docs/adr/`, reading ADRs that touch the area you're about to work in, if
  the directory exists
- `docs/source/` for public website content and navigation truth
- `docs/superpowers/source-packets/` for source-supported public facts
- `docs/superpowers/plans/` for durable implementation plans
- `docs/superpowers/research/` for benchmark and research notes

Agents may read, maintain, and modify root `CONTEXT.md` when a task needs to
preserve or refine WOEAI public-site language. If `CONTEXT.md` or `docs/adr/` do
not exist, proceed silently. Do not flag their absence or suggest creating them
upfront. The producer skill (`/grill-with-docs`) creates them lazily when terms
or decisions actually get resolved.

## Layout

This is a single-context docs-site repo. Treat the repository root as the one
context for domain language and architectural decisions.

Expected optional structure:

```text
/
|-- CONTEXT.md
|-- docs/
|   |-- adr/
|   |-- agents/
|   |-- source/
|   `-- superpowers/
|       |-- plans/
|       |-- research/
|       `-- source-packets/
`-- scripts/
```

## Use The Project Vocabulary

When your output names a domain concept, issue title, refactor proposal,
hypothesis, or test name, use the WOEAI site vocabulary from `AGENTS.md`,
`CONTEXT.md` if present, and the current `docs/source/` pages.

For public-facing WOEAI content, preserve the repo's source-supported language
and avoid inventing facts. Unknown public facts belong in planning notes as "to
be confirmed", not in published pages as definite claims.

## Flag ADR Conflicts

If your output contradicts an existing ADR, surface it explicitly rather than
silently overriding it.
