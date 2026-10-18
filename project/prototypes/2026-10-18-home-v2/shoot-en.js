const { chromium } = require('playwright-core');
const path = require('path');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

async function shoot(b, name, vp, url, out) {
  const p = await b.newPage({ viewport: vp, deviceScaleFactor: 2 });
  await p.goto(url, { waitUntil: 'load' });
  await p.evaluate(async () => {
    const step = window.innerHeight * 0.8;
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    window.scrollTo(0, 0);
  });
  await p.waitForTimeout(600);
  const m = await p.evaluate(() => {
    const doc = document.documentElement;
    const r = (sel) => { const e = document.querySelector(sel); if (!e) return null; const b = e.getBoundingClientRect(); return { x: 0, y: Math.round(b.top + scrollY), width: doc.clientWidth, height: Math.round(b.height) }; };
    const over = [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && (b.right > doc.clientWidth + 1 || b.left < -1); }).slice(0, 5).map(e => e.className || e.tagName);
    return { sw: doc.scrollWidth, cw: doc.clientWidth, h: doc.scrollHeight, hero: r('.home-hero'), footer: r('.home-footer'), over };
  });
  await p.screenshot({ path: path.join(__dirname, `${out}-hero.png`), clip: m.hero, fullPage: true });
  await p.screenshot({ path: path.join(__dirname, `${out}-footer.png`), clip: m.footer, fullPage: true });
  console.log(name, JSON.stringify(m));
  await p.close();
}

(async () => {
  const b = await chromium.launch({ executablePath: CHROME });
  await shoot(b, 'en-desktop', { width: 1440, height: 900 }, 'file:///tmp/woeai-sphinx-html/en/index.html', 'en-desktop');
  await shoot(b, 'en-mobile', { width: 390, height: 844 }, 'file:///tmp/woeai-sphinx-html/en/index.html', 'en-mobile');
  await shoot(b, 'zh-footer', { width: 1440, height: 900 }, 'file:///tmp/woeai-sphinx-html/index.html', 'zh-desktop');
  await b.close();
})();
