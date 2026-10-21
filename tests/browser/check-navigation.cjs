/* Rendered navigation regression: default/collapsed/expanded, desktop/mobile. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const {chromium} = require('playwright');
const anchors = require('./navigation-anchors.json');
const {launchOptions} = require('./check-paper-citations.cjs');

async function assertChineseMenu(page) {
  const links = await page.locator('.wy-menu-vertical a.reference').evaluateAll(nodes => nodes.map(a => ({
    text:a.textContent.trim(),href:a.getAttribute('href')})));
  assert.ok(links.length > 5, 'real sidebar must be present');
  for (const link of links) {
    // Keep scientific abbreviations and original paper navigation titles.
    if (link.href.includes('paper-notes/') || /^\d{4}\s+[A-Z0-9]+\s*\|/.test(link.text)) continue;
    assert.ok(link.text, 'no empty sidebar label');
    if (/\p{Script=Han}/u.test(link.text)) {
      assert.doesNotMatch(link.text.replace(/\b(?:AI|WOEAI)\b/g,''), /[A-Za-z]/,
        'Chinese navigation must not append an English translation: '+link.text);
    }
  }
}

async function assertResearchStates(page, origin, width) {
  await page.setViewportSize({width,height:1000});
  await page.goto(origin+'/Research.html');
  const drawer=page.locator('.wy-nav-side'), toggle=page.locator('.reader-toggle');
  await assertChineseMenu(page); // Checks raw text even in collapsed/inert branches.
  if (width<900) {
    assert.equal(await toggle.getAttribute('aria-expanded'),'false','mobile starts closed');
    assert.equal(await drawer.getAttribute('aria-hidden'),'true');
    await toggle.click();
    assert.equal(await toggle.getAttribute('aria-expanded'),'true','mobile opens');
  }
  const menu=page.locator('.wy-menu-vertical');
  const root=menu.locator('.toctree-l1 > a').filter({hasText:/^科研方向$/});
  for (const name of ['结构风工程','海洋能源结构']) {
    const link=menu.locator('.toctree-l2 > a').filter({hasText:new RegExp('^'+name+'$')});
    assert.equal(await link.count(),1,'exact Chinese family label');
    assert.ok(await link.isVisible(),'family visible by default');
  }
  await root.locator('button.toctree-expand').click();
  assert.ok(!await menu.getByRole('link',{name:'结构风工程',exact:true}).isVisible(),'collapsed root hides children');
  await root.locator('button.toctree-expand').click();
  for (const [name,child] of [['结构风工程','数值风洞'],['海洋能源结构','混凝土浮体']]) {
    const link=menu.locator('.toctree-l2 > a').filter({hasText:new RegExp('^'+name+'$')});
    assert.ok(await link.isVisible());
    await link.locator('button.toctree-expand').click();
    assert.ok(await menu.getByRole('link',{name:child,exact:true}).isVisible(),'expanded family reveals subdirection');
    await assertChineseMenu(page);
  }
  for (const id of ['research-direction-structural-wind','structural-wind-engineering',
    'building-wind-project-support','research-project','marine-energy-structures','floating-wind-project-support']) {
    assert.ok(await page.evaluate(id=>!!document.getElementById(id),id),'existing anchor retained: '+id);
  }
  if (width<900) {
    await page.keyboard.press('Escape');
    assert.equal(await toggle.getAttribute('aria-expanded'),'false','mobile closes after expanded checks');
  }
}

async function main() {
  const outdir=path.resolve(process.argv[2] || '/tmp/woeai-sphinx-html');
  const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.woff2':'font/woff2','.png':'image/png'};
  const server=http.createServer((req,res)=>{
    const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
    const file=path.resolve(outdir,'.'+pathname);
    if(path.relative(outdir,file).startsWith('..')){res.writeHead(403).end();return;}
    const stream=fs.createReadStream(file);stream.on('error',()=>{if(!res.headersSent)res.writeHead(404);res.end();});
    res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');stream.pipe(res);
  });
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  let browser;
  try {
    browser=await chromium.launch(launchOptions());
    const page=await browser.newPage();
    const origin='http://127.0.0.1:'+server.address().port;
    for(const width of [1440,390]) {
      await assertResearchStates(page,origin,width);
      for(const doc of ['EngineeringApplications','Teaching','About','Publications','PublicationsByYear']) {
        await page.goto(origin+'/'+doc+'.html');await assertChineseMenu(page);
      }
      // Frozen pre-fix fragments must still resolve to the same semantic sections.
      for(const [doc, expected] of Object.entries(anchors)) {
        await page.goto(origin+'/'+doc+'.html');
        for(const [id,title] of Object.entries(expected)) {
          const actual=await page.evaluate(id=>{
            const section=document.getElementById(id);
            return section?.querySelector('h1,h2,h3,h4')?.textContent.replace(/\uf0c1/g,'').trim();
          },id);
          assert.equal(actual,title,doc+'#'+id+' must retain its original destination');
        }
      }
      await page.goto(origin+'/en/Research.html');
      const english=await page.locator('.wy-menu-vertical a.reference').allTextContents();
      assert.deepEqual(english.slice(0,4),['Research','Publications','Join Us','Search']);
      assert.ok(english.length>4,'English highlights retained');
      assert.ok(await page.getByRole('heading',{name:/^Structural Wind Engineering/}).isVisible());
    }
    console.log('PASS: Chinese sidebar raw labels; desktop/mobile default/collapse/expand/drawer; other Chinese menus; anchors; English sidebar.');
  } finally {if(browser)await browser.close();await new Promise(r=>server.close(r));}
}
if(require.main===module)main().catch(error=>{console.error(error);process.exitCode=1;});
