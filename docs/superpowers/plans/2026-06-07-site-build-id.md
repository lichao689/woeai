# WOEAI Site Build ID Plan

Date: 2026-06-07

Goal: replace software-style semantic version strings in the Sphinx project metadata with a public website update identifier that fits this docs-only ReadTheDocs site.

## Confirmed Rule

- Use a Site Build ID instead of semantic versioning for the public website.
- `docs/source/conf.py` remains the only file updated by the release-bump script.
- `release` uses Beijing time in `YYYY.MM.DD-HHMM` form.
- `version` uses the same Beijing date in `YYYY.MM.DD` form.
- `.readthedocs.yaml` `version: "2"` is the ReadTheDocs configuration schema version and must not be changed by this workflow.
- Git commits remain the authoritative technical history; the Site Build ID is a public-facing update marker.

## Implementation

- Add `scripts/bump-site-release.py`.
- The default command updates `docs/source/conf.py` using the current `Asia/Shanghai` time.
- For deterministic tests and future automation, the script accepts:
  - `--conf-path PATH`
  - `--datetime YYYY-MM-DDTHH:MM[:SS][+HH:MM]`
- Add behavior tests under `tests/`.
- Run the tests from `scripts/check-docs.sh` before the strict Sphinx build.

## Verification

Run before claiming completion:

```bash
python3 -m unittest discover -s tests
./scripts/check-docs.sh
git diff --check
```
