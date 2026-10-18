# Source from bash; keep the shared runtime configuration in one place.
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/cloud-workflow-env.sh"
export WOEAI_DOCS_VENV="$WOEAI_ROOT/.venv"
export WOEAI_DOCS_BUILD="$WOEAI_ROOT/docs/_build/html"
