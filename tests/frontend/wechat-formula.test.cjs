const test = require('node:test');
const assert = require('node:assert/strict');
const { withFormulaMetadata } = require('../../wechat/tools/render_mathjax_svg.cjs');
const sample = '<mjx-container jax="SVG"><svg viewBox="0 -800 1200 1000" style="vertical-align:-0.2ex"><g fill="currentColor" stroke="currentColor"><path d="M0 0L1 1"/><path fill="none" d="M1 1"/></g></svg></mjx-container>';
for (const display of [false, true]) {
 test(`formula uses standard containers and inherits text paint without a background, display=${display}`, () => {
  const out = withFormulaMetadata(sample, {tex:'x<y', display});
  assert.doesNotMatch(out, /<rect|background|#ffffff|#1f2933|mjx-container/);
  assert.match(out, /fill="currentColor"/);
  assert.match(out, /stroke="currentColor"/);
  assert.match(out, /style="fill:currentColor;stroke:currentColor;"/);
  assert.match(out, display ? /^<section/ : /^<span/);
  assert.match(out, /fill="none"/);
  assert.match(out, /data-formula="x&lt;y"/);
  assert.match(out, /d="M0 0L1 1"/);
  assert.match(out, /vertical-align:-0.2ex/);
  if (display) assert.match(out, /text-align:center/);
 });
}
test('invalid SVG dimensions fail visibly instead of producing an invisible formula', () => {
 assert.throws(() => withFormulaMetadata('<mjx-container><svg></svg></mjx-container>', {tex:'x',display:false}), /viewBox/);
});

test('MathJax error nodes are rejected rather than wrapped as valid formulas', () => {
 assert.throws(() => withFormulaMetadata(sample.replace('<path ', '<g data-mml-node="merror"></g><path '), {tex:'bad',display:false}), /could not render/);
});

const { spawnSync } = require('node:child_process');
const path = require('node:path');
const render = (tex) => spawnSync(process.execPath, [path.resolve(__dirname, '../../wechat/tools/render_mathjax_svg.cjs')], {
 input: JSON.stringify({formulas:[{tex,display:true}]}), encoding:'utf8', timeout:10000,
 env: {...process.env, WOEAI_MATHJAX_NODE_MODULE_DIR: process.env.WOEAI_MATHJAX_NODE_MODULE_DIR || path.resolve(__dirname, '../../wechat/runtime/node_modules')},
});
const probe = render('x');
const missingRuntime = /Missing mathjax-full/.test(probe.stdout || '');
test('real MathJax keeps fraction, matrix and superscript geometry renderable', {skip:missingRuntime && 'Install pinned WeChat runtime for integration test'}, () => {
 for (const tex of ['\\frac{x}{y}', 'x_1^2', '\\begin{matrix}1&2\\\\3&4\\end{matrix}']) {
  const r=render(tex); assert.equal(r.status,0,r.stdout+r.stderr);
  const body=JSON.parse(r.stdout).items[0].html;
  if (tex.includes("frac")) assert.match(body, /<rect /);
  assert.match(body,/fill:currentColor;stroke:currentColor;/); assert.doesNotMatch(body,/background|fill="#ffffff"|data-mml-node="merror"/);
 }
});
test('real unknown TeX fails instead of publishing red literal commands', {skip:missingRuntime && 'Install pinned WeChat runtime for integration test'}, () => {
 const r=render('\\definitelyNotACommand{x}'); assert.notEqual(r.status,0);
 assert.equal(JSON.parse(r.stdout).ok,false);
});
