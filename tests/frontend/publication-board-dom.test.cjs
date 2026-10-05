// Runs the actual board script against a small DOM double, not browser/visual QA.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const script = fs.readFileSync(path.join(__dirname, '../../docs/_static/publication-board.js'), 'utf8');
const fixture = fs.readFileSync(path.join(__dirname, '../../docs/_static/publication-board-data.json'), 'utf8');
const walk = node => [node, ...node.children.flatMap(walk)];
const cards = column => column.children.filter(node => node.tag === 'article');
const count = column => Number(column.children[0].children[0].textContent);
function freeze(value) {
  if (value && typeof value === 'object') {
    Object.values(value).forEach(freeze);
    Object.freeze(value);
  }
  return value;
}

function boot(response) {
  let focused;
  class Element {
    constructor(tag, text = '') {
      Object.assign(this, {tag, textContent: text, children: [], listeners: {},
        dataset: {}, attributes: {}, disabled: false, value: '', checked: false});
    }
    append(...nodes) {
      nodes.forEach(node => { node.parent = this; this.children.push(node); });
    }
    replaceChildren(...nodes) {
      this.children.forEach(node => { node.parent = null; });
      this.children = [];
      this.append(...nodes);
      if (this.tag === 'select') this.value = nodes[0]?.value || '';
    }
    replaceWith(node) {
      const parent = this.parent;
      node.parent = parent;
      parent.children.splice(parent.children.indexOf(this), 1, node);
      this.parent = null;
    }
    setAttribute(key, value) { this.attributes[key] = value; }
    addEventListener(type, listener) {
      (this.listeners[type] ||= []).push(listener);
    }
    emit(type, event = {}) {
      if (this.disabled) return;
      (this.listeners[type] || []).forEach(listener => listener(event));
    }
    add(node) { this.append(node); }
    focus() { focused = this; }
    querySelector(tag) { return walk(this).slice(1).find(node => node.tag === tag) || null; }
  }
  const ids = Object.fromEntries(['publication-board', 'board-filters', 'board-results',
    'board-summary', 'board-notice', 'board-reset'].map(id => [id, new Element('div')]));
  const form = ids['board-filters'];
  form.elements = Object.fromEntries(['query', 'year', 'direction', 'status', 'unfinished']
    .map(name => [name, new Element(['year', 'direction', 'status'].includes(name) ? 'select' : 'input')]));
  form.reset = () => Object.values(form.elements).forEach(control => {
    control.value = ''; control.checked = false;
  });
  const tracks = ['rtd', 'wechat'].map(track => {
    const button = new Element('button');
    button.dataset.boardTrack = track;
    return button;
  });
  const controls = [...Object.values(form.elements), ids['board-reset'], ...tracks];
  controls.forEach(control => { control.disabled = true; });
  ids['publication-board'].dataset.source = '_static/publication-board-data.json';
  const data = freeze(JSON.parse(fixture));
  const requests = [];
  const document = {
    getElementById: id => ids[id],
    createElement: tag => new Element(tag),
    querySelectorAll(selector) {
      if (selector === '[data-board-track]') return tracks;
      if (selector === '#board-filters :disabled, [data-board-track]:disabled') {
        return controls.filter(control => control.disabled);
      }
      throw new Error(`Unsupported test DOM selector: ${selector}`);
    }
  };
  const context = vm.createContext({
    document, window: {},
    Option: function (text, value) {
      const option = new Element('option', text); option.value = value; return option;
    },
    fetch: async (url, options) => {
      requests.push({url, options: JSON.parse(JSON.stringify(options))});
      return response ? response() : {ok: true, json: async () => data};
    }
  });
  vm.runInContext(script, context);
  return {ids, form, tracks, controls, data, requests, get focused() { return focused; },
    ready: new Promise(resolve => setImmediate(resolve))};
}

test('DOM: loading gates controls; show-all preserves totals and focuses the first new detail', async () => {
  const ui = boot();
  assert(ui.controls.every(control => control.disabled));
  await ui.ready;
  assert(ui.controls.every(control => !control.disabled));
  const columns = ui.ids['board-results'].children;
  assert.equal(columns.length, 5);
  assert.equal(columns.reduce((sum, column) => sum + count(column), 0), ui.data.papers.length);
  for (const column of columns) {
    assert.equal(cards(column).length, Math.min(count(column), 4));
    const more = column.children.find(node => node.className === 'board-show-more');
    if (count(column) <= 4) { assert.equal(more, undefined); continue; }
    assert.match(more.attributes['aria-label'], /显示全部/);
    more.emit('click');
    assert.equal(cards(column).length, count(column));
    assert.equal(ui.focused, cards(column)[4].querySelector('summary'));
    assert(!column.children.includes(more));
  }
  assert.equal(columns.reduce((sum, column) => sum + cards(column).length, 0), ui.data.papers.length);
  assert(!walk(ui.ids['board-results']).some(node =>
    ['input', 'select', 'textarea', 'form'].includes(node.tag) || node.attributes.contenteditable));
  for (const section of walk(ui.ids['board-results']).filter(node => node.className === 'board-track-detail')) {
    const gaps = section.children.find(node => node.className === 'board-gaps');
    const checks = section.children.find(node => node.className === 'board-checks');
    for (const gap of gaps?.children || []) {
      assert(!checks.children.some(check => check.textContent.startsWith(gap.textContent)),
        'Check results should appear once, not duplicated in gaps');
    }
  }
  assert.equal(JSON.stringify(ui.data), JSON.stringify(JSON.parse(fixture)));
  assert.deepEqual(ui.requests, [{url: '_static/publication-board-data.json',
    options: {credentials: 'omit', cache: 'no-cache'}}]);
});

test('DOM: hidden papers remain searchable; empty results, reset and repeated track switches work', async () => {
  const ui = boot();
  await ui.ready;
  const fields = ui.form.elements;
  // Select a paper outside every initially rendered column, then search all data.
  const visibleTitles = new Set(walk(ui.ids['board-results'])
    .filter(node => node.tag === 'h3').map(node => node.textContent));
  const hidden = ui.data.papers.find(paper => !visibleTitles.has(paper.title));
  assert(hidden);
  fields.query.value = hidden.title;
  ui.form.emit('input');
  assert(walk(ui.ids['board-results']).some(node => node.tag === 'h3' && node.textContent === hidden.title));
  fields.query.value = 'this-paper-does-not-exist-987654321';
  ui.form.emit('input');
  assert.equal(ui.ids['board-results'].children[0].className, 'board-empty-results');
  assert.match(ui.ids['board-notice'].textContent, /显示 0 \//);
  fields.query.value = hidden.title;
  fields.year.value = String(hidden.year);
  fields.direction.value = hidden.family;
  fields.unfinished.checked = true;
  for (let i = 0; i < 6; i++) {
    const selected = ui.tracks[i % 2];
    fields.status.value = 'blocked';
    selected.emit('click');
    assert.equal(fields.status.value, '');
    assert.equal(fields.query.value, hidden.title);
    assert.equal(fields.year.value, String(hidden.year));
    assert.equal(fields.direction.value, hidden.family);
    assert.equal(fields.unfinished.checked, true);
    assert.equal(selected.attributes['aria-pressed'], 'true');
    assert.equal(ui.tracks[(i + 1) % 2].attributes['aria-pressed'], 'false');
    assert.equal(fields.status.children.length, i % 2 === 0 ? 7 : 9);
  }
  ui.ids['board-reset'].emit('click');
  assert.equal(ui.tracks[1].attributes['aria-pressed'], 'true');
  assert.equal(ui.focused, fields.query);
  for (const field of Object.values(fields)) { assert.equal(field.value, ''); assert.equal(field.checked, false); }
  assert.equal(ui.ids['board-results'].children.reduce((sum, column) => sum + count(column), 0), ui.data.papers.length);
  let prevented = false;
  ui.form.emit('submit', {preventDefault() { prevented = true; }});
  assert(prevented);
  assert.equal(ui.requests.length, 1);
  assert.equal(JSON.stringify(ui.data), JSON.stringify(JSON.parse(fixture)));
});

test('DOM: network, HTTP, malformed JSON and unsupported schema failures remain read-only', async () => {
  const failures = [
    () => { throw new Error('offline'); },
    () => ({ok: false}),
    () => ({ok: true, json: async () => { throw new Error('invalid JSON'); }}),
    () => ({ok: true, json: async () => ({schema_version: 999, papers: []})})
  ];
  for (const response of failures) {
    const ui = boot(response);
    await ui.ready;
    assert(ui.controls.every(control => control.disabled));
    assert.equal(ui.ids['board-results'].children.length, 0);
    assert.match(ui.ids['board-notice'].textContent, /加载失败.*仓库中的进度清单/);
    assert.equal(ui.requests.length, 1);
  }
});
