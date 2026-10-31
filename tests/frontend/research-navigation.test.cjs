const assert = require('node:assert/strict');
const {test} = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const script = fs.readFileSync(path.join(__dirname, '../../docs/_static/research-navigation.js'), 'utf8');

function visit(fragment, pathname = '/zh-cn/latest/Research.html') {
    const redirects = [];
    const listeners = {};
    const location = {pathname, hash: fragment, href: 'https://winddee.cn' + pathname + fragment,
        replace: target => redirects.push(target)};
    vm.runInNewContext(script, {location, URL, addEventListener: (name, fn) => { listeners[name] = fn; }});
    return {redirects, listeners, location};
}

test('legacy bookmarks preserve their topic and deployment prefix', () => {
    for (const [fragment, target] of [
        ['research-direction-structural-wind', 'StructuralWindEngineering.html'],
        ['id1', 'StructuralWindEngineering.html#numerical-wind-tunnel'],
        ['research-project', 'StructuralWindEngineering.html#building-wind-project-support'],
        ['floating-offshore-wind-turbine', 'MarineEnergyStructures.html'],
        ['id4', 'MarineEnergyStructures.html#concrete-floating-structures'],
        ['id10', 'MarineEnergyStructures.html#floating-wind-coupling-figure'],
        ['floating-wind-project-support', 'MarineEnergyStructures.html#floating-wind-project-support'],
    ]) assert.deepEqual(visit('#' + fragment).redirects, ['https://winddee.cn/zh-cn/latest/' + target]);
});

test('overview, unknown/malformed hashes and unrelated routes stay put', () => {
    for (const hash of ['', '#research', '#unknown', '#%ZZ', '#toString'])
        assert.deepEqual(visit(hash).redirects, []);
    assert.deepEqual(visit('#id1', '/zh-cn/latest/en/Research.html').redirects, []);
    assert.deepEqual(visit('#id1', '/StructuralWindEngineering.html').redirects, []);
});

test('bookmarks followed while the overview is open also redirect', () => {
    const state = visit('');
    state.location.hash = '#id5';
    state.listeners.hashchange();
    assert.deepEqual(state.redirects, ['https://winddee.cn/zh-cn/latest/MarineEnergyStructures.html#numerical-wave-basin']);
});
