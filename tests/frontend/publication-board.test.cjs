const test = require('node:test');
const assert = require('node:assert/strict');
const board = require('../../docs/_static/publication-board.js');
const paper = (ref, rtd, wechat, extra={}) => ({ref,title:'Wind loading',doi:'10.1000/wind',year:2026,family:'建筑结构抗风',subdirection:'数值风洞与湍动入流',rtd:{status:rtd,verification_current:rtd==='verified'},wechat:{status:wechat,verification_current:wechat==='published'},...extra});
test('independent tracks preserve unknown, audit and publication boundaries', () => {
  assert.equal(board.columnFor(paper('a','awaiting_audit','draft_created').rtd,'rtd'),'review');
  assert.equal(board.columnFor(paper('a','awaiting_audit','draft_created').wechat,'wechat'),'review');
  assert.equal(board.columnFor({status:'ready_to_publish',verification_current:true},'wechat'),'review');
  assert.equal(board.columnFor({status:'verified',verification_current:false},'rtd'),'review');
  assert.equal(board.columnFor({status:'unregistered'},'rtd'),'unknown');
  assert.equal(board.columnFor({status:'future_unknown'},'rtd'),'unknown');
});
test('search, year, direction, exact state, track and unfinished combine without mutation', () => {
  const papers = [paper('a','verified','draft_created'),paper('b','unregistered','published',{year:2025}),paper('c','awaiting_audit','unregistered',{title:'Ocean platform',doi:'10.1000/ocean',family:'海上漂浮风电',subdirection:'浮式混凝土平台结构设计'})];
  const original = JSON.stringify(papers);
  assert.deepEqual(board.filterPapers(papers,{track:'rtd',unfinished:true}).map(p=>p.ref),['b','c']);
  assert.deepEqual(board.filterPapers(papers,{track:'wechat',unfinished:true}).map(p=>p.ref),['a','c']);
  assert.deepEqual(board.filterPapers(papers,{track:'rtd',query:'  WIND ',year:'2026',direction:'建筑结构抗风',status:'verified'}).map(p=>p.ref),['a']);
  assert.deepEqual(board.filterPapers(papers,{track:'rtd',query:'HTTPS://DOI.ORG/10.1000/OCEAN',direction:'浮式混凝土平台结构设计'}).map(p=>p.ref),['c']);
  assert.equal(board.filterPapers(papers,{query:'missing'}).length,0);
  assert.equal(board.filterPapers(papers,{}).length,3);
  assert.equal(JSON.stringify(papers),original);
});
test('repeated track switches and reset never accumulate filters or mutate source', () => {
  const papers = [paper('a','verified','draft_created'),paper('b','drafting','published'),paper('c','unregistered','unregistered')];
  for (let i=0; i<20; i++) {
    assert.deepEqual(board.filterPapers(papers,{track:'rtd',status:'verified'}).map(p=>p.ref),['a']);
    assert.deepEqual(board.filterPapers(papers,{track:'wechat',status:'draft_created'}).map(p=>p.ref),['a']);
    assert.equal(board.filterPapers(papers,{track:'wechat'}).length,3);
  }
});
test('every supported state has a conservative column and readable label', () => {
  for (const [state,column] of Object.entries({unregistered:'unknown',planned:'working',drafting:'working',awaiting_audit:'review',verified:'complete',blocked:'blocked'})) {
    assert.equal(board.columnFor({status:state,verification_current:true},'rtd'),column);
    assert.equal(typeof board.STATUS[state],'string');
  }
  for (const [state,column] of Object.entries({unregistered:'unknown',planned:'working',drafting:'working',awaiting_review:'review',draft_created:'review',ready_to_publish:'review',published:'complete',blocked:'blocked'})) {
    assert.equal(board.columnFor({status:state,verification_current:true},'wechat'),column);
  }
  assert.equal(board.columnFor({status:'published',verification_current:null},'wechat'),'review');
  assert.equal(board.columnFor({status:'verified',verification_current:null},'rtd'),'review');
});
