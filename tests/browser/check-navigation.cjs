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
    assert.doesNotMatch(link.text,/^\d+(?:\.\d+)*\s+/, 'global navigation has no body numbers');
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
  for (const [name,doc,child] of [['结构风工程','StructuralWindEngineering','数值风洞'],['海洋能源结构','MarineEnergyStructures','一体化分析']]) {
    await page.goto(origin+'/Research.html');
    if(width<900)await toggle.click();
    const link=menu.locator('.toctree-l2 > a').filter({hasText:new RegExp('^'+name+'$')});
    assert.ok(await link.isVisible());
    await link.click();
    await page.waitForLoadState('domcontentloaded');
    assert.ok(page.url().endsWith('/'+doc+'.html'),'family opens its topic page');
    if(width<900)await toggle.click();
    assert.ok(await menu.getByRole('link',{name:child,exact:true}).isVisible(),'topic navigation reveals subdirection');
    await assertChineseMenu(page);
    assert.equal(await page.locator('.site-nav a[aria-current="page"]').textContent(),'研究方向');
  }
  await page.goto(origin+'/Research.html');
  for (const id of ['research-direction-structural-wind','structural-wind-engineering',
    'building-wind-project-support','research-project','marine-energy-structures','floating-wind-project-support']) {
    assert.ok(await page.evaluate(id=>!!document.getElementById(id),id),'existing anchor retained: '+id);
  }
  if (width<900) {
    await page.keyboard.press('Escape');
    assert.equal(await toggle.getAttribute('aria-expanded'),'false','mobile closes after expanded checks');
  }
}

async function assertBodyNumbering(page, origin) {
  const cases = [
    ['Research',[]],
    ['StructuralWindEngineering',['1 科研项目']],
    ['MarineEnergyStructures',['1 科研项目']],
    ['Teaching',['1 教学工作','2 学生培养']],
    ['EngineeringApplications',['1 应用场景','2 企业项目证据','3 工程问题交流']],
    ['About',['1 隐私说明','2 版权与引用','3 技术致谢']],
    ['Recruitment',['1 研究与培养','2 申请类型与公开信息','3 如何联系']],
    ['en/Research',['1 AI across both fields','2 Research highlights']],
    ['en/StructuralWindEngineering',['1 Project support']],
    ['en/MarineEnergyStructures',['1 Project support']],
    ['en/JoinUs',['1 Research fit','2 Academic contact','3 Official application']],
    ['en/highlights/ref-chen2024-JCP',['1 The problem','2 The contribution','3 Engineering significance','Source paper']],
  ];
  for(const prefix of ['', 'en/']) {
    for(const doc of ['NumericalWindTunnel','StructuralWindResistance','IntegratedAnalysis','ConcreteFloatingStructures','NumericalWaveBasin']) {
      const labels=prefix ? ['Methods and contributions',...(doc==='NumericalWaveBasin'?[]:['Evidence in practice']),'Open questions','Publications and projects'] : ['方法与创新',...(doc==='NumericalWaveBasin'?[]:['代表成果与验证']),'仍待解决的问题','论文与项目',...(doc==='IntegratedAnalysis'?['技术详情：系统分析框架']:doc==='ConcreteFloatingStructures'?['技术详情：混凝土平台框架']:[])];
      cases.push([prefix+doc,labels.map((label,i)=>(i+1)+' '+label)]);
    }
  }
  const headingTexts=async selector=>page.locator(selector).evaluateAll(nodes=>nodes.map(e=>{
    const copy=e.cloneNode(true);copy.querySelectorAll('.headerlink').forEach(n=>n.remove());return copy.textContent.trim();
  }));
  for(const [doc,expectedH2] of cases) {
    await page.goto(origin+'/'+doc+'.html');
    assert.deepEqual(await headingTexts('.document h2'),expectedH2,doc+' body H2');
    assert.equal(await page.locator('.document h1 .body-section-number,.document h4 .body-section-number,.document h5 .body-section-number,.document h6 .body-section-number').count(),0,'only H2/H3 receive counters');
    assert.equal(await page.locator('.wy-nav-side .body-section-number,.wy-breadcrumbs .body-section-number,header .body-section-number').count(),0,'shell labels stay unnumbered');
    assert.equal(await page.locator('.document .unnumbered-reference .body-section-number').count(),0,'citations stay unnumbered');
    for(const heading of await page.locator('.document h2,.document h3').all()) {
      if(await heading.evaluate(e=>!!e.closest('.unnumbered-reference')))continue;
      assert.equal(await heading.locator('.body-section-number').count(),1,'one accessible real prefix');
      assert.ok(await heading.locator('.body-section-number').isVisible());
    }
    const links=await page.locator('.wy-menu-vertical a.reference').allTextContents();
    for(const text of links)assert.doesNotMatch(text.trim(),/^\d+(?:\.\d+)*\s+/,'global navigation has no section counters');
    assert.ok(!await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),doc+' has no horizontal overflow');
    if(doc==='Teaching')assert.deepEqual(await headingTexts('.document h3'),['1.1 本科生','1.2 研究生','1.3 教改探索','2.1 博士生','2.2 硕士生']);
    if(doc==='EngineeringApplications')assert.deepEqual(await headingTexts('.document h4'),['数值风洞','结构抗风','一体化分析','混凝土浮体','数值水池']);
  }
  for(const doc of ['index','en/index','Publications','PublicationsByYear','GroupNews','en/Publications','paper-notes/ref-chen2024-JCP']) {
    await page.goto(origin+'/'+doc+'.html');
    assert.equal(await page.locator('.body-section-number').count(),0,'excluded page: '+doc);
    if(doc.startsWith('paper-notes/')) {
      const h2=await headingTexts('.document h2'), h4=await headingTexts('.document h4');
      assert.ok(h2.includes('摘要') && h2.includes('1 引言'));
      assert.ok(h4.includes('2.2.1 入口质量平衡条件'),'original paper third-level number preserved');
    }
  }
}

async function assertReaderPresentation(page, origin, width) {
  for (const route of ['index.html', 'en/index.html']) {
    await page.goto(origin + '/' + route);
    const geometry = await page.evaluate(() => {
      const hero = document.querySelector('.home-hero');
      const visual = document.querySelector('.english-hero-diagram');
      return {
        columns: getComputedStyle(hero).gridTemplateColumns.split(' ').length,
        heroWidth: hero.getBoundingClientRect().width,
        visualWidth: visual.getBoundingClientRect().width,
        overflow: document.documentElement.scrollWidth > innerWidth + 1,
      };
    });
    assert.equal(geometry.overflow, false, route + ' has no horizontal overflow');
    if (width < 900) {
      assert.equal(geometry.columns, 1, route + ' mobile hero is one column');
      assert.ok(geometry.visualWidth > geometry.heroWidth * .95, route + ' mobile visual is full width');
    }
  }
  await page.goto(origin + '/Publications.html');
  assert.equal(await page.locator('.pub-entry:visible').count(), 75, 'all Chinese records start visible');
  await page.locator('#publication-query').fill('satellite');
  const filtered = await page.locator('.pub-entry:visible').count();
  assert.ok(filtered > 0 && filtered < 75, 'Chinese keyword filter reduces results');
  await page.locator('.publication-filter-reset').click();
  assert.equal(await page.locator('.pub-entry:visible').count(), 75, 'reset restores Chinese records');
  await page.locator('#publication-notes-only').check();
  assert.ok(await page.locator('.pub-entry:visible').count() > 0, 'reading-note filter has results');
  await page.goto(origin + '/en/Publications.html');
  assert.equal(await page.locator('.pub-entry:visible').count(), 75, 'all English records start visible');
  await page.locator('#publication-query').fill('graph neural');
  assert.ok(await page.locator('.pub-entry:visible').count() > 0, 'English keyword filter has results');
  await page.goto(origin + '/paper-notes/ref-tang2025-JBE.html');
  assert.equal(await page.locator('.paper-note-lead').count(), 1, 'paper cover and contents share the lead');
  const contents = page.locator('.paper-note-lead .contents > ul');
  if (width < 900) {
    assert.equal(await contents.isHidden(), true, 'mobile paper contents starts collapsed');
    await page.locator('.paper-contents-toggle').click();
    assert.equal(await contents.isVisible(), true, 'mobile paper contents expands');
  } else {
    assert.equal(await contents.isVisible(), true, 'desktop paper contents stays visible');
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
          if(doc==='Research' && id!=='research')continue; // Moved sections are checked through their old URLs below.
          const actual=await page.evaluate(id=>{
            const section=document.getElementById(id);
            const heading=section?.querySelector('h1,h2,h3,h4')?.cloneNode(true);
            heading?.querySelectorAll('.body-section-number').forEach(n=>n.remove());
            return heading?.textContent.replace(/\uf0c1/g,'').trim();
          },id);
          assert.equal(actual,title,doc+'#'+id+' must retain its original destination');
        }
      }
      for(const [fragment,title] of Object.entries(anchors.Research)) {
        if(fragment==='research')continue;
        await page.goto(origin+'/Research.html#'+fragment);
        await page.waitForFunction(()=>!location.pathname.endsWith('/Research.html'));
        const actual=await page.evaluate(()=>{
          const target=location.hash?document.getElementById(decodeURIComponent(location.hash.slice(1))):document.querySelector('.document h1');
          const heading=target?.closest('section')?.querySelector('h1,h2,h3,h4')?.cloneNode(true);
          heading?.querySelectorAll('.body-section-number,.headerlink').forEach(n=>n.remove());
          return heading?.textContent.trim();
        });
        assert.equal(actual,title,'Research#'+fragment+' keeps its semantic destination');
      }
      await assertBodyNumbering(page,origin);
      await assertReaderPresentation(page,origin,width);
      await page.goto(origin+'/en/Research.html');
      const english=await page.locator('.wy-menu-vertical a.reference').allTextContents();
      assert.deepEqual(english.slice(0,4),['Research','Publications','Join Us','Search']);
      assert.ok(english.length>4,'English highlights retained');
      assert.ok(await page.getByRole('heading',{name:/^1 AI across both fields/}).isVisible());
    }
    console.log('PASS: navigation, anchors, body numbering, bilingual home geometry, publication filters and paper-note contents at desktop/mobile widths.');
  } finally {if(browser)await browser.close();await new Promise(r=>server.close(r));}
}
if(require.main===module)main().catch(error=>{console.error(error);process.exitCode=1;});
