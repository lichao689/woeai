#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${WOEAI_DOCS_VENV:-/tmp/woeai-docs-venv}"
BUILD_DIR="${WOEAI_DOCS_BUILD:-/tmp/woeai-sphinx-html}"

mkdir -p "$(dirname "${VENV_DIR}")" "$(dirname "${BUILD_DIR}")"
"${PYTHON_BIN}" - <<'PY'
import sys

if sys.version_info < (3, 12):
    raise SystemExit("Python 3.12+ is required for WOEAI docs checks")
PY
"${PYTHON_BIN}" "${ROOT_DIR}/scripts/check-public-safe-content.py"
"${PYTHON_BIN}" -m unittest discover -s "${ROOT_DIR}/tests"
"${PYTHON_BIN}" -m venv "${VENV_DIR}"
"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/python" -m pip install -r "${ROOT_DIR}/docs/requirements.txt"
rm -rf "${BUILD_DIR}"
"${VENV_DIR}/bin/sphinx-build" -b html -W --keep-going -E "${ROOT_DIR}/docs/source" "${BUILD_DIR}"
echo "WOEAI docs build succeeded: ${BUILD_DIR}"
