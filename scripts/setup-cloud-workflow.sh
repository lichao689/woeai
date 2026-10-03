#!/usr/bin/env bash
# Install the content-production runtime only; never read publication credentials.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
"$PYTHON_BIN" -c 'import sys; assert sys.version_info >= (3, 12), "Python 3.12+ required"'
node -e 'if (+process.versions.node.split(".")[0] < 20) throw Error("Node 20+ required")'
"$PYTHON_BIN" -m venv "$ROOT/.venv"
"$ROOT/.venv/bin/python" -m pip install --no-cache-dir -r "$ROOT/wechat/runtime/requirements.lock.txt"
npm --cache "$ROOT/wechat/.local/npm-cache" --prefix "$ROOT/wechat/runtime" ci --ignore-scripts --no-audit --no-fund
mkdir -p "$ROOT/wechat/.local/cache"
printf '%s\n' 'Ready. From the repository root: source scripts/cloud-workflow-env.sh'
