# Source from bash. This only configures the checkout-local rendering runtime.
WOEAI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PATH="$WOEAI_ROOT/.venv/bin:$PATH"
export WOEAI_MATHJAX_NODE_MODULE_DIR="$WOEAI_ROOT/wechat/runtime/node_modules"
export XDG_CACHE_HOME="$WOEAI_ROOT/wechat/.local/cache"
export PYTHONPATH="$WOEAI_ROOT${PYTHONPATH:+:$PYTHONPATH}"
mkdir -p "$XDG_CACHE_HOME"
