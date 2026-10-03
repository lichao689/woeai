#!/usr/bin/env bash
# Credential-free smoke test using existing public-safe sample assets.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
source scripts/cloud-workflow-env.sh
OUT="$ROOT/wechat/.local/cloud-check"
mkdir -p "$OUT"
python scripts/check-public-safe-content.py
python -m unittest discover -s tests
python wechat/tools/wechat_draft.py preflight --publication-ref ref-zhao2026-BS > "$OUT/preflight.json"
python wechat/tools/wechat_draft.py dry-run --publication-ref ref-zhao2026-BS > "$OUT/dry-run.json"
python wechat/tools/render-copy-ready.py wechat/articles/draft-public-safe/ref-zhao2026-BS.md --math-renderer mathjax-svg --theme academic-clean -o "$OUT/article.html"
python .agents/skills/wechat-cover/scripts/cover_preview.py wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png > "$OUT/cover.json"
python - <<'PY'
from html.parser import HTMLParser
import json
from pathlib import Path
from PIL import Image
out = Path('wechat/.local/cloud-check')
class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.formulas = 0
        self.images = []
        self.errors = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'mjx-container':
            assert attrs.get('data-formula'), 'Formula metadata missing'
            self.formulas += 1
        if tag == 'img':
            self.images.append(attrs.get('src', ''))
        self.errors += 'data-mjx-error' in attrs
check = Audit()
check.feed((out / 'article.html').read_text())
assert check.formulas > 0 and not check.errors, 'Missing or invalid formulas'
assert check.images and all(src.startswith('data:image/') for src in check.images)
for filename in ['preflight.json', 'dry-run.json']:
    record = json.loads((out / filename).read_text())
    assert record['ok']
    for flag in ['will_read_credentials', 'will_contact_wechat', 'will_create_or_update_draft']:
        assert record[flag] is False
cover = json.loads((out / 'cover.json').read_text())
assert cover['ok']
assert len(cover['covers']) == 1, 'Expected one sample cover'
cover_item = cover['covers'][0]
for flag in ['exists', 'target_ratio_match', 'file_size_ok']:
    assert cover_item[flag] is True, f'Cover check failed: {flag}'
assert (cover_item['width'], cover_item['height']) == (900, 383)
for path in Path('wechat/assets/public-safe/ref-zhao2026-BS').glob('*.png'):
    with Image.open(path) as im:
        im.verify()
print(f'Offline sample PASS: {check.formulas} formulas, {len(check.images)} embedded images')
PY
