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
async function main(){
 const root=path.resolve(process.argv[2]||'/tmp/woeai-sphinx-html'),results=[];
 const server=http.createServer((q,s)=>{const f=path.resolve(root,'.'+new URL(q.url,'http://local').pathname);if(path.relative(root,f).startsWith('..')){s.writeHead(403).end();return;}
 const types={'.js':'text/javascript','.css':'text/css','.html':'text/html','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'};s.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');const stream=fs.createReadStream(f);stream.on('error',()=>{if(!s.headersSent)s.writeHead(404);s.end();});stream.pipe(s);});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch(launchOptions());try{
 for(const width of [1440,390]){
  const page=await browser.newPage({viewport:{width,height:900}});
  await page.goto(origin+'/index.html');await settle(page);
  await page.locator('.direction-card a[href="Research.html#research-direction-structural-wind"]').click();await settle(page);
  results.push({width,case:'cross-page-card-alias',...await expectPosition(page,'research-direction-structural-wind','1 结构风工程')});
  await page.reload();await settle(page);results.push({width,case:'refresh-with-hash',...await expectPosition(page,'research-direction-structural-wind','1 结构风工程')});
  if(width<900){
    await page.locator('.reader-toggle').click();
    assert.ok(await page.locator('.wy-nav-side').evaluate(sidebar=>sidebar.contains(document.activeElement)&&document.activeElement.tagName==='A'),'drawer opens on navigation, not the hosted search popup');
  }
  const button=page.locator('.toctree-l2 > a[href="#structural-wind-engineering"] button');
  if(!await page.locator('.wy-menu-vertical a[href="#id2"]').isVisible())await button.click();
  await page.locator('.wy-menu-vertical a[href="#id2"]').click();
  results.push({width,case:'same-page-click',...await expectPosition(page,'id2','1.2 结构抗风')});
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
