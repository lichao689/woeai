const { chromium } = require('playwright-core');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
(async () => {
  const b = await chromium.launch({ executablePath: CHROME });
  for (const [name, url] of [['en', 'file:///tmp/woeai-sphinx-html/en/index.html'], ['zh', 'file:///tmp/woeai-sphinx-html/index.html']]) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 } });
    await p.goto(url, { waitUntil: 'load' });
    const info = await p.evaluate(() => {
      const doc = document.documentElement;
      return [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && (b.right > doc.clientWidth + 1 || b.left < -1); })
        .map(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return { tag: e.tagName, cls: e.className, text: (e.textContent || '').trim().slice(0, 30), left: Math.round(r.left), right: Math.round(r.right), w: Math.round(r.width), pos: cs.position }; });
    });
    console.log(name, JSON.stringify(info, null, 2));
    await p.close();
  }
  await b.close();
})();
