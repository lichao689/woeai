// Capture the *built* homepage (not the standalone prototype) so the review
// images show exactly what the Sphinx build ships.
//
// Section crops use page.screenshot({clip}) rather than element screenshots:
// the theme's `.site-skip` link is `position: fixed; top: -100px`, and Playwright
// paints fixed elements at odd offsets when it has to stitch an element taller
// than the viewport, which put a fake "跳到主要内容" box on top of a card.
const { chromium } = require('playwright-core');
const path = require('path');

const OUT = __dirname;
const URL = 'file:///tmp/woeai-sphinx-html/index.html';
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

async function shoot(browser, name, viewport) {
  const page = await browser.newPage({ viewport, deviceScaleFactor: 2 });
  await page.goto(URL, { waitUntil: 'load' });
  // Sweep the page once so `loading="lazy"` images (paper covers, WeChat QR)
  // have actually decoded before any crop is taken.
  await page.evaluate(async () => {
    const step = window.innerHeight * 0.8;
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
  });
  await page.waitForTimeout(600);

  const metrics = await page.evaluate(() => {
    const doc = document.documentElement;
    const over = [];
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width === 0) continue;
      if (r.right > doc.clientWidth + 1 || r.left < -1) {
        over.push({ tag: el.tagName, cls: el.className, right: Math.round(r.right) });
      }
    }
    const rect = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return {
        x: 0,
        y: Math.round(r.top + window.scrollY),
        width: doc.clientWidth,
        height: Math.round(r.height),
      };
    };
    const cards = [...document.querySelectorAll('#research-lines .direction-card')].map((c) => {
      const r = c.getBoundingClientRect();
      return { w: Math.round(r.width), h: Math.round(r.height) };
    });
    const ctas = [...document.querySelectorAll('#research-lines .direction-body > .text-link')].map((a) => {
      const r = a.getBoundingClientRect();
      return Math.round(r.top + window.scrollY);
    });
    return {
      scrollWidth: doc.scrollWidth,
      clientWidth: doc.clientWidth,
      height: Math.round(doc.scrollHeight),
      crops: {
        hero: rect('.home-hero'),
        research: rect('#research-lines'),
        work: rect('#selected-work'),
        join: rect('#join-contact'),
      },
      directionCards: cards,
      ctaTops: ctas,
      overflowing: over.slice(0, 8),
    };
  });

  for (const [label, clip] of Object.entries(metrics.crops)) {
    if (!clip) continue;
    await page.screenshot({ path: path.join(OUT, `landed-${name}-${label}.png`), clip, fullPage: true });
  }
  await page.screenshot({ path: path.join(OUT, `landed-${name}-full.png`), fullPage: true });
  await page.close();
  return metrics;
}

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME });
  const desktop = await shoot(browser, 'desktop', { width: 1440, height: 900 });
  const mobile = await shoot(browser, 'mobile', { width: 390, height: 844 });
  await browser.close();
  console.log(JSON.stringify({ desktop, mobile }, null, 2));
})();
