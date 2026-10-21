/* Enumerate the built routes and audit every directory fragment's final geometry. */
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const {chromium}=require('playwright');
const {launchOptions}=require('./check-paper-citations.cjs');
const DIRECTORY='.wy-menu-vertical a[href],.site-nav a[href],.site-mobile-navigation nav a[href],.contents a[href],.hero-actions a[href]';
const routesIn=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?routesIn(path.join(dir,e.name)):[path.join(dir,e.name)]).filter(f=>f.endsWith('.html'));
const frames=page=>page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
async function settle(page){
  await page.evaluate(async()=>{
    document.querySelectorAll('img[loading="lazy"]').forEach(img=>{img.loading='eager';});
    await Promise.all([...document.images].map(img=>img.complete?Promise.resolve():new Promise(r=>{img.addEventListener('load',r,{once:true});img.addEventListener('error',r,{once:true});})));
    await document.fonts.ready;
  });
  await page.waitForFunction(()=>[...document.querySelectorAll('.math')].every(node=>node.querySelector('mjx-container')),null,{timeout:15000});
  await page.evaluate(async()=>{
    await document.fonts.ready;
    let last=-1,stable=0;const end=performance.now()+10000;
    while(stable<6&&performance.now()<end){
      await new Promise(requestAnimationFrame);
      const current=document.documentElement.scrollHeight;
      stable=current===last?stable+1:0;last=current;
    }
    if(stable<6)throw Error('visual math/image layout did not settle');
  });
  await frames(page);
}
async function geometry(page,target){
  return page.evaluate(({fragment,headingIndex})=>{
    const node=headingIndex>=0?document.querySelectorAll('h1,h2,h3,h4,h5,h6')[headingIndex]:document.getElementById(fragment);
    if(!node)return {missing:true};
    const rect=node.getBoundingClientRect();
    const bars=[document.querySelector('.site-header'),document.querySelector('.wy-nav-top')].filter(Boolean).map(e=>e.getBoundingClientRect());
    const occlusion=Math.max(0,...bars.filter(r=>r.height>0&&r.top>=-1&&r.top<innerHeight).map(r=>r.bottom));
    const gap=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--anchor-gap'))||22;
    const top=scrollY+rect.top,max=Math.max(0,document.documentElement.scrollHeight-innerHeight);
    const expected=Math.min(max,Math.max(0,top-occlusion-gap));
    return {heading:node.textContent.replace(/\uf0c1/g,'').trim().slice(0,160),top:rect.top,scrollY,maximum:max,occlusion,gap,error:Math.abs(scrollY-expected),bottomConstrained:top-occlusion-gap>max+1,headerTop:bars[0]?.top,scrollRoot:document.scrollingElement===document.documentElement};
  },target);
}
async function clickTarget(page,origin,route,target){
  const candidates=await page.locator(DIRECTORY).evaluateAll((links,{origin,route,fragment})=>links.flatMap((a,index)=>{
    const u=new URL(a.href);return u.origin===origin&&u.pathname==='/'+route&&decodeURIComponent(u.hash.slice(1))===fragment?[index]:[];
  }),{origin,route,fragment:target.fragment});
  for(const index of candidates){
    const link=page.locator(DIRECTORY).nth(index);
    const inSidebar=await link.evaluate(a=>!!a.closest('.wy-menu-vertical'));
    if(inSidebar){
      const toggle=page.locator('.reader-toggle');
      if(await toggle.isVisible() && await toggle.getAttribute('aria-expanded')==='false')await toggle.click();
      await link.evaluate(a=>{
        const ancestors=[];let li=a.closest('li')?.parentElement?.closest('li');
        while(li){ancestors.unshift(li);li=li.parentElement?.closest('li');}
        for(const parent of ancestors)if(!parent.classList.contains('current'))parent.querySelector(':scope > a > button.toctree-expand')?.click();
      });
    }
    if(await link.isVisible()){
      await link.click();await frames(page);return 'directory-click';
    }
  }
  // Historical aliases can be linked from a different page's directory only.
  // Exercise the browser hash route without inventing an invisible test link.
  await page.evaluate(fragment=>{location.hash=encodeURIComponent(fragment);},target.fragment);
  await frames(page);return 'hash-route';
}
async function inventory(page,root,origin){
  const rows=routesIn(root).sort().map(file=>({route:path.relative(root,file).split(path.sep).join('/'),html:fs.readFileSync(file,'utf8')}));
  return page.evaluate(({rows,origin,DIRECTORY})=>{
    const parsed=new Map(rows.map(row=>[row.route,new DOMParser().parseFromString(row.html,'text/html')]));
    const edges=[],missing=[],targets=new Map(),pages=[];
    for(const [route,doc]of parsed){
      pages.push(route);
      for(const a of doc.querySelectorAll(DIRECTORY)){
        const u=new URL(a.getAttribute('href'),origin+'/'+route);if(u.origin!==origin)continue;
        const destination=decodeURIComponent(u.pathname.slice(1))||'index.html',fragment=decodeURIComponent(u.hash.slice(1));
        const edge={source:route,href:a.getAttribute('href'),destination,fragment};edges.push(edge);
        const dest=parsed.get(destination),element=fragment&&dest?.getElementById(fragment);
        if(!dest||(fragment&&!element)){missing.push(edge);continue;}
        if(!fragment)continue;
        const headings=[...dest.querySelectorAll('h1,h2,h3,h4,h5,h6')];
        let heading=null;
        if(element.matches('h1,h2,h3,h4,h5,h6'))heading=element;
        else if(element.getAttribute('aria-labelledby'))heading=dest.getElementById(element.getAttribute('aria-labelledby').split(/\s+/)[0]);
        else if(element.matches('section'))heading=[...element.children].find(e=>/^H[1-6]$/.test(e.tagName));
        else if(element.matches('span')&&!element.textContent.trim()){
          let next=element.nextElementSibling;
          while(next?.matches('span')&&!next.textContent.trim())next=next.nextElementSibling;
          if(next&&/^H[1-6]$/.test(next.tagName))heading=next;
        }
        targets.set(destination+'#'+fragment,{route:destination,fragment,headingIndex:headings.indexOf(heading)});
      }
    }
    return {pages,edges,targets:[...targets.values()],missing};
  },{rows,origin,DIRECTORY});
}
async function hierarchy(page,origin,width,colorScheme){
  await page.setViewportSize({width,height:900});await page.emulateMedia({colorScheme});
  const result=[];
  for(const route of ['Research.html','en/Research.html']){
    await page.goto(origin+'/'+route);if(width<900)await page.locator('.reader-toggle').click();
    if(route==='Research.html')await page.locator('.toctree-l2 > a[href="#structural-wind-engineering"] button').click();
    const styles=await page.locator('.wy-menu-vertical li > a').evaluateAll(links=>links.map(a=>({
      depth:Number(a.parentElement.className.match(/toctree-l(\d+)/)?.[1]),font:parseFloat(getComputedStyle(a).fontSize),weight:Number(getComputedStyle(a).fontWeight),indent:parseFloat(getComputedStyle(a).paddingLeft),color:getComputedStyle(a).color,visible:!!a.getClientRects().length,clipped:a.scrollWidth>a.clientWidth+1,
    })));
    const one=styles.find(s=>s.depth===1),two=styles.find(s=>s.depth===2);
    assert.ok(one&&two&&one.font>two.font&&one.weight>two.weight&&two.indent>one.indent,'semantic first/second level distinction: '+route);
    assert.ok(styles.filter(s=>s.visible).every(s=>!s.clipped),'long titles wrap without clipping');
    const buttons=await page.locator('button.toctree-expand').evaluateAll(nodes=>nodes.map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})).filter(r=>r.width));
    assert.ok(buttons.every(r=>r.width>=24&&r.height>=24),'expand controls retain usable hit areas');
    result.push({route,width,colorScheme,first:one,second:two,passed:true});
  }
  return result;
}
async function main(){
  const root=path.resolve(process.argv[2]||'/tmp/woeai-sphinx-html'),reportFile=process.argv[3]||'/tmp/woeai-anchor-audit.json';
  const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.woff2':'font/woff2'};
  const server=http.createServer((req,res)=>{
    const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));
    if(path.relative(root,file).startsWith('..')){res.writeHead(403).end();return;}
    res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');const stream=fs.createReadStream(file);stream.on('error',()=>{if(!res.headersSent)res.writeHead(404);res.end();});stream.pipe(res);
  });
  await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
  const browser=await chromium.launch(launchOptions()),context=await browser.newContext();
  const ledger={pages:[],edges:[],targets:[],missing:[],measurements:[],hierarchy:[],failures:[],runtimeWarnings:[],visits:[],exclusions:[]};
  try{
    const collector=await context.newPage();Object.assign(ledger,await inventory(collector,root,origin));await collector.close();
    await Promise.all([1440,390].map(async width=>{
      const page=await context.newPage();await page.setViewportSize({width,height:900});
      page.on('pageerror',error=>{const item={width,type:'script',message:error.message};
        // Pre-existing optional SRE worker is not the visual MathJax-ready signal.
        if(/importScripts.*speech-worker\.js.*failed to load/.test(error.message))ledger.runtimeWarnings.push(item);
        else ledger.failures.push(item);
      });
      for(const route of ledger.pages){
        try{
          const response=await page.goto(origin+'/'+route);assert.equal(response.status(),200,route);await settle(page);
          assert.ok(await page.locator('.site-header').isVisible(),'page identity and shell');
          ledger.visits.push({route,width,assetsAndVisualMathSettled:true});
          for(const target of ledger.targets.filter(t=>t.route===route)){
            const mode=await clickTarget(page,origin,route,target),measure=await geometry(page,target);
            const item={route,fragment:target.fragment,width,mode,...measure};ledger.measurements.push(item);
            if(measure.missing||measure.error>3||Math.abs(measure.headerTop)>1||!measure.scrollRoot)ledger.failures.push(item);
          }
          fs.writeFileSync(reportFile+'.checkpoint.json',JSON.stringify({pages:ledger.pages,visits:ledger.visits,completedGeometry:ledger.measurements.length,expectedGeometry:ledger.targets.length*2,failures:ledger.failures,runtimeWarnings:ledger.runtimeWarnings},null,2));
          console.log('Audited '+width+' '+route);
        }catch(error){ledger.failures.push({route,width,message:error.message});}
      }
      for(const colorScheme of ['light','dark']){
        try{ledger.hierarchy.push(...await hierarchy(page,origin,width,colorScheme));}catch(error){ledger.failures.push({width,colorScheme,type:'hierarchy',message:error.message});}
      }
      await page.close();
    }));
  }finally{
    ledger.summary={builtPages:ledger.pages.length,pageViewportVisits:ledger.visits.length,directoryEdges:ledger.edges.length,hashEdges:ledger.edges.filter(e=>e.fragment).length,uniqueHashTargets:ledger.targets.length,geometryChecks:ledger.measurements.length,expectedGeometryChecks:ledger.targets.length*2,actualDirectoryClicks:ledger.measurements.filter(m=>m.mode==='directory-click').length,hashRouteChecks:ledger.measurements.filter(m=>m.mode==='hash-route').length,bottomConstrained:ledger.measurements.filter(m=>m.bottomConstrained).length,runtimeWarnings:ledger.runtimeWarnings.length,missingTargets:ledger.missing.length,failures:ledger.failures.length,exclusions:ledger.exclusions.length};
    fs.writeFileSync(reportFile,JSON.stringify(ledger,null,2));console.log(JSON.stringify(ledger.summary));
    await browser.close();await new Promise(r=>server.close(r));
  }
  assert.equal(ledger.missing.length+ledger.failures.length,0,'complete anchor audit must have no failures');
  assert.equal(ledger.measurements.length,ledger.targets.length*2,'every unique target must be measured at both widths');
}
if(require.main===module)main().catch(e=>{console.error(e);process.exitCode=1;});
module.exports={geometry,settle,frames};
