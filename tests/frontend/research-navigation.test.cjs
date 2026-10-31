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
        ['structural-wind-engineering', 'StructuralWindEngineering.html'],
        ['building-wind-project-support', 'StructuralWindEngineering.html#building-wind-project-support'],
        ['id1', 'StructuralWindEngineering.html#numerical-wind-tunnel'],
        ['id2', 'StructuralWindEngineering.html#structural-wind-resistance'],
        ['research-project', 'StructuralWindEngineering.html#building-wind-project-support'],
        ['research-direction-floating-wind', 'MarineEnergyStructures.html'],
        ['floating-offshore-wind-turbine', 'MarineEnergyStructures.html'],
        ['marine-energy-structures', 'MarineEnergyStructures.html'],
        ['id3', 'MarineEnergyStructures.html#floating-wind-integrated-analysis'],
        ['id4', 'MarineEnergyStructures.html#concrete-floating-structures'],
        ['id5', 'MarineEnergyStructures.html#numerical-wave-basin'],
        ['id6', 'MarineEnergyStructures.html#floating-wind-figures'],
        ['id7', 'MarineEnergyStructures.html#floating-wind-project-support'],
        ['id8', 'MarineEnergyStructures.html#floating-wind-dimensions-figure'],
        ['id9', 'MarineEnergyStructures.html#concrete-floater-design-figure'],
        ['id10', 'MarineEnergyStructures.html#floating-wind-coupling-figure'],
        ['floating-wind-project-support', 'MarineEnergyStructures.html#floating-wind-project-support'],
    ]) assert.deepEqual(visit('#' + fragment).redirects, ['https://winddee.cn/zh-cn/latest/' + target]);
});

test('English legacy direction bookmarks remain within the English deployment prefix', () => {
    for (const [fragment, target] of [
        ['structural-wind-engineering', 'StructuralWindEngineering.html'],
        ['marine-energy-structures', 'MarineEnergyStructures.html'],
        ['floating-offshore-wind', 'MarineEnergyStructures.html'],
    ]) {
        assert.deepEqual(visit('#' + fragment, '/zh-cn/latest/en/Research.html').redirects,
            ['https://winddee.cn/zh-cn/latest/en/' + target]);
        assert.deepEqual(visit('#' + fragment, '/en/Research.html').redirects,
            ['https://winddee.cn/en/' + target]);
    }
});

test('overview, unknown/malformed hashes and unrelated routes stay put', () => {
    for (const hash of ['', '#research', '#unknown', '#%ZZ', '#toString'])
        assert.deepEqual(visit(hash).redirects, []);
    assert.deepEqual(visit('#id1', '/zh-cn/latest/en/Research.html').redirects, []);
    assert.deepEqual(visit('#id1', '/StructuralWindEngineering.html').redirects, []);
    for (const hash of ['', '#research', '#research-highlights', '#ai-across-both-fields', '#%ZZ'])
        assert.deepEqual(visit(hash, '/zh-cn/latest/en/Research.html').redirects, []);
    assert.deepEqual(visit('#floating-offshore-wind', '/Research.html').redirects, []);
});

test('English hash changes also follow the matching topic', () => {
    const state = visit('', '/zh-cn/latest/en/Research.html');
    state.location.hash = '#floating-offshore-wind';
    state.listeners.hashchange();
    assert.deepEqual(state.redirects, ['https://winddee.cn/zh-cn/latest/en/MarineEnergyStructures.html']);
});

test('bookmarks followed while the overview is open also redirect', () => {
    const state = visit('');
    state.location.hash = '#id5';
    state.listeners.hashchange();
    assert.deepEqual(state.redirects, ['https://winddee.cn/zh-cn/latest/MarineEnergyStructures.html#numerical-wave-basin']);
});
