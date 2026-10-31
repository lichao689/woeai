/* Real route, reload, delayed image and manual-scroll regressions. */
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const {chromium}=require('playwright');
const {launchOptions}=require('./check-paper-citations.cjs');
const {geometry,settle,frames}=require('./check-anchor-navigation.cjs');
async function expectPosition(page,fragment,headingText){
  const headingIndex=await page.locator('h1,h2,h3,h4,h5,h6').evaluateAll((nodes,text)=>nodes.findIndex(n=>n.textContent.replace(/\uf0c1/g,'').trim()===text),headingText);
  assert.ok(headingIndex>=0,'actual semantic heading: '+headingText);
  await frames(page);const measure=await geometry(page,{fragment,headingIndex});
  assert.ok(measure.error<=3&&Math.abs(measure.headerTop)<=1,JSON.stringify(measure));return measure;
}
async function expectTopicTop(page){
  assert.ok(page.url().endsWith('/StructuralWindEngineering.html'),'topic entry has no fragment');
  assert.equal(await page.evaluate(()=>scrollY),0,'new document opens at its natural top');
  assert.ok(await page.locator('.document h1').isVisible(),'topic identity is visible');
  assert.match(await page.locator('.document h1').textContent(),/结构风工程/);
  return {passed:true,scrollY:0};
}
async function main(){
 const root=path.resolve(process.argv[2]||'/tmp/woeai-sphinx-html'),results=[];
 const server=http.createServer((q,s)=>{const f=path.resolve(root,'.'+new URL(q.url,'http://local').pathname);if(path.relative(root,f).startsWith('..')){s.writeHead(403).end();return;}
 const types={'.js':'text/javascript','.css':'text/css','.html':'text/html','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'};s.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');const stream=fs.createReadStream(f);stream.on('error',()=>{if(!s.headersSent)s.writeHead(404);s.end();});stream.pipe(s);});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch(launchOptions());try{
 for(const width of [1440,390]){
  const page=await browser.newPage({viewport:{width,height:900}});
  await page.goto(origin+'/index.html');await settle(page);
  await page.locator('.direction-card a[href="StructuralWindEngineering.html"]').click();await settle(page);
  results.push({width,case:'cross-page-card',...await expectTopicTop(page)});
  await page.goto(origin+'/Research.html#research-direction-structural-wind');
  await page.waitForURL('**/StructuralWindEngineering.html');await settle(page);
  results.push({width,case:'legacy-cross-page-alias',...await expectTopicTop(page)});
  await page.goto(origin+'/Research.html#id2');
  await page.waitForURL('**/StructuralWindResistance.html');await settle(page);
  await page.goto(origin+'/StructuralWindResistance.html#structural-wind-resistance-methods');await settle(page);
  await page.reload();await settle(page);results.push({width,case:'refresh-with-hash',...await expectPosition(page,'structural-wind-resistance-methods','1 方法与创新')});
  if(width<900){
    await page.locator('.reader-toggle').click();
    assert.ok(await page.locator('.wy-nav-side').evaluate(sidebar=>sidebar.contains(document.activeElement)&&document.activeElement.tagName==='A'),'drawer opens on navigation, not the hosted search popup');
  }
  const button=page.locator('.toctree-l3 > a[href="#"] button');
  if(!await page.locator('.wy-menu-vertical a[href="#structural-wind-resistance-methods"]').isVisible())await button.click();
  await page.locator('.wy-menu-vertical a[href="#structural-wind-resistance-methods"]').click();
  results.push({width,case:'same-page-click',...await expectPosition(page,'structural-wind-resistance-methods','1 方法与创新')});
  if(width<900)await page.locator('.reader-toggle').click();
  const before=await page.evaluate(()=>scrollY);await button.click();await button.click();await frames(page);
  assert.ok(Math.abs(await page.evaluate(()=>scrollY)-before)<2,'expansion itself must not scroll article');
  if(width<900)await page.keyboard.press('Escape');
  await page.goto(origin+'/index.html');await settle(page);
  if(width<900)await page.locator('.site-mobile-navigation summary').click();
  await page.locator(width<900?'.site-mobile-navigation a[href="#join-contact"]':'.site-nav a[href="#join-contact"]').click();
  const bottom=await expectPosition(page,'join-contact','交流与合作');
  if(width===1440)assert.ok(bottom.bottomConstrained,'natural page-bottom clamp recorded, no artificial padding');
  if(width<900)assert.ok(!await page.locator('.site-mobile-navigation').evaluate(e=>e.open),'menu closes before final placement');
  results.push({width,case:'home-menu-and-bottom',...bottom});
  for(const [route,title] of [['index.html','近期学术进展'],['en/index.html','Recent academic progress']]){
    await page.goto(origin+'/'+route+'#latest-progress');await settle(page);
    results.push({width,case:'historical-home-progress-alias',route,...await expectPosition(page,'latest-progress',title)});
  }
  for(const [legacy,topic] of [['structural-wind-engineering','StructuralWindEngineering'],['marine-energy-structures','MarineEnergyStructures'],['floating-offshore-wind','MarineEnergyStructures']]){
    await page.goto(origin+'/en/Research.html#'+legacy);
    await page.waitForURL('**/en/'+topic+'.html');await settle(page);
    assert.ok(await page.locator('.document h1').isVisible());
    const language=page.locator('.site-language');
    assert.equal(await language.getAttribute('href'),'../'+topic+'.html');
    await language.click();await settle(page);
    assert.equal(await page.locator('.site-language').getAttribute('href'),'en/'+topic+'.html');
    results.push({width,case:'bilingual-topic-and-legacy',legacy,passed:true});
  }
  for(const doc of ['NumericalWindTunnel','StructuralWindResistance','IntegratedAnalysis','ConcreteFloatingStructures','NumericalWaveBasin']) {
    await page.goto(origin+'/'+doc+'.html');await settle(page);
    assert.ok(!await page.locator('.document h2').allTextContents().then(texts=>texts.some(t=>/研究背景|核心问题/.test(t))),'opening has no background/question headings');
    await page.locator('.site-language').click();await settle(page);
    assert.ok(page.url().endsWith('/en/'+doc+'.html'));
    assert.equal(await page.locator('.wy-breadcrumbs a').count(),3,'home, research, parent family');
    await page.locator('.site-language').click();await settle(page);
    assert.ok(page.url().endsWith('/'+doc+'.html'));
    results.push({width,case:'subdirection-language-round-trip',doc,passed:true});
  }
  for(const [legacy,doc,target] of [['id8','IntegratedAnalysis','floating-wind-dimensions-figure'],['id9','ConcreteFloatingStructures','concrete-floater-design-figure'],['id10','IntegratedAnalysis','floating-wind-coupling-figure']]){
    await page.goto(origin+'/Research.html#'+legacy);
    await page.waitForURL('**/'+doc+'.html#'+target);await settle(page);
    assert.ok(await page.locator('.research-technical').evaluate(e=>e.open),'bookmarked technical figure is disclosed');
    const figure=page.locator('#'+target).locator('..');
    assert.ok(await figure.locator('img').isVisible());
    assert.ok(await figure.locator('a.reference.internal').getAttribute('href'),'full-size image is linked');
    results.push({width,case:'legacy-technical-figure-revealed',legacy,passed:true});
  }
  await page.close();
 }
 // Delay an actual figure above the selected paper subsection. This exercises
 // post-load layout rather than a fabricated fixed offset or a cropped fixture.
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 await page.route('**/_images/cover*',async route=>{await new Promise(r=>setTimeout(r,700));await route.continue();});
 await page.goto(origin+'/paper-notes/ref-chen2024-JCP.html#id8',{waitUntil:'domcontentloaded'});await settle(page);
 results.push({case:'math-and-image-settled',...await expectPosition(page,'id8','2.2.1 入口质量平衡条件')});
 // A later content resize must not override a user's deliberate scroll.
 await page.mouse.wheel(0,500);await page.waitForTimeout(100);
 await page.evaluate(()=>{const img=document.querySelector('img');if(img)img.style.marginBottom='100px';});
 await frames(page);const manual=await geometry(page,{fragment:'id8',headingIndex:await page.locator('h1,h2,h3,h4,h5,h6').evaluateAll(nodes=>nodes.findIndex(n=>n.textContent.includes('2.2.1 入口质量平衡条件')))});
 assert.ok(manual.error>100,'manual scrolling cancels late fragment following');results.push({case:'manual-scroll-not-overridden',passed:true});
 await page.close();console.log(JSON.stringify({passed:true,results}));
 }finally{await browser.close();await new Promise(r=>server.close(r));}
}
if(require.main===module)main().catch(e=>{console.error(e);process.exitCode=1;});
