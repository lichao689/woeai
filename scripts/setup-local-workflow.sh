#!/usr/bin/env bash
# Rebuild the repository-owned runtime on the local machine, without credentials.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
"$ROOT/scripts/setup-cloud-workflow.sh"
"$ROOT/.venv/bin/python" -m pip install -r "$ROOT/docs/requirements.txt"
"$ROOT/.venv/bin/python" -m pip check
printf '%s\n' 'Local runtime ready. From the repository root: source scripts/local-workflow-env.sh'
