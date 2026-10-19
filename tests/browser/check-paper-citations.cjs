/* Real Chromium contract for every registry-backed reading page. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');

const normalize = text => text.normalize('NFKC').replace(/\s+/gu, ' ').trim();
const launchOptions = () => ({headless: true, ...(process.env.WOEAI_BROWSER_EXECUTABLE
  ? {executablePath: process.env.WOEAI_BROWSER_EXECUTABLE} : {})});

async function assertCitation(page, expected) {
  const body = page.locator('.paper-full-citation');
  assert.equal(await body.count(), 1, expected.docname + ': exactly one citation body');
  await body.evaluate(element => {
    for (let node = element.parentElement; node; node = node.parentElement) {
      if (node.tagName === 'DETAILS') node.open = true;
    }
  });
  assert.ok(await body.isVisible(), expected.docname + ': citation must be visible');
  await body.scrollIntoViewIfNeeded();
  const state = await body.evaluate(element => {
    const rect = element.getBoundingClientRect();
    let visible = rect.width > 0 && rect.height > 0;
    let clipped = false;
    const transparent = color => /rgba\([^)]*,\s*0(?:\.0+)?\)/.test(color)
      || /\/\s*0(?:\.0+)?\s*\)$/.test(color);
    // innerText includes opacity:0 and transparent descendants. Inspect each
    // substantive text node through its entire ancestor chain as well.
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    for (let textNode = walker.nextNode(); textNode; textNode = walker.nextNode()) {
      if (!textNode.textContent.trim()) continue;
      const range = document.createRange();
      range.selectNodeContents(textNode);
      const textRects = [...range.getClientRects()].filter(box => box.width > 0 && box.height > 0);
      visible = visible && textRects.length > 0;
      const textCss = getComputedStyle(textNode.parentElement);
      visible = visible && !transparent(textCss.color)
        && !transparent(textCss.webkitTextFillColor) && parseFloat(textCss.fontSize) > 0;
      for (let node = textNode.parentElement; node; node = node.parentElement) {
        const css = getComputedStyle(node), bounds = node.getBoundingClientRect();
        visible = visible && css.display !== 'none' && css.visibility === 'visible'
          && Number(css.opacity) > 0;
        if (css.clipPath !== 'none') clipped = true;
        for (const box of textRects) {
          if (/hidden|clip/.test(css.overflowY)
            && (box.top < bounds.top - 1 || box.bottom > bounds.bottom + 1)) clipped = true;
          if (/hidden|clip/.test(css.overflowX)
            && (box.left < bounds.left - 1 || box.right > bounds.right + 1)) clipped = true;
        }
      }
    }
    return {text: element.innerText, visible, clipped,
      overflow: element.scrollWidth > element.clientWidth + 1};
  });
  assert.ok(state.visible && !state.clipped && !state.overflow, expected.docname + ': readable citation, no hiding or clipping');
  assert.equal(normalize(state.text), normalize(expected.text), expected.docname + ': complete recorded citation text');
  if (expected.doi) {
    assert.equal(await body.locator('a').evaluateAll((links, doi) => links.filter(link =>
      link.getAttribute('href') === 'https://doi.org/' + doi).length, expected.doi), 1,
      expected.docname + ': recorded DOI link');
  }
  return state;
}

async function main() {
  const root = path.resolve(__dirname, '../..');
  const outdir = path.resolve(process.argv[2] || '/tmp/woeai-sphinx-html');
  const pages = JSON.parse(execFileSync(process.env.PYTHON_BIN || 'python3',
    [path.join(root, 'tools/publications/citations.py'), '--manifest'], {cwd: root, encoding: 'utf8'}));
  const contentType = {'.html':'text/html; charset=utf-8', '.js':'text/javascript',
    '.css':'text/css', '.png':'image/png', '.svg':'image/svg+xml', '.woff2':'font/woff2'};
  const server = http.createServer((request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    const filename = path.resolve(outdir, '.' + (pathname.endsWith('/') ? pathname + 'index.html' : pathname));
    if (path.relative(outdir, filename).startsWith('..')) {response.writeHead(403).end();return;}
    const stream = fs.createReadStream(filename);
    stream.on('error', () => {if (!response.headersSent) response.writeHead(404);response.end();});
    response.setHeader('Content-Type', contentType[path.extname(filename)] || 'application/octet-stream');
    stream.pipe(response);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  const results = [];
  try {
    browser = await chromium.launch(launchOptions());
    const context = await browser.newContext();
    // Only local built output is needed for citation checks; no ads or remote MathJax.
    await context.route('**/*', route => new URL(route.request().url()).hostname === '127.0.0.1'
      ? route.continue() : route.abort());
    const page = await context.newPage();
    for (const width of [1280, 390]) {
      await page.setViewportSize({width, height: 900});
      for (const expected of pages) {
        const response = await page.goto('http://127.0.0.1:' + server.address().port + '/' + expected.docname + '.html',
          {waitUntil: 'domcontentloaded'});
        assert.equal(response.status(), 200, expected.docname);
        await assertCitation(page, expected);
        results.push({docname: expected.docname, width, passed: true});
      }
    }
    console.log(JSON.stringify({pages: pages.length, viewports: 2, checked: results.length, ok: true, results}));
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}

module.exports = {assertCitation, launchOptions};
if (require.main === module) main().catch(error => {console.error(error.message);process.exitCode = 1;});
