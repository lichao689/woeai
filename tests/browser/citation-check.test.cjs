const {test, before, after} = require('node:test');
const assert = require('node:assert/strict');
const {chromium} = require('playwright');
const {assertCitation, launchOptions} = require('./check-paper-citations.cjs');
let browser, page;
const expected = {docname: 'future-reader', text: 'Author. A checked title. Journal, 2025.'};
const valid = '<p class="paper-full-citation">' + expected.text + '</p>';

before(async () => {browser = await chromium.launch(launchOptions());page = await browser.newPage();});
after(async () => {if (browser) await browser.close();});

test('visible full citation is readable after opening a collapsed container', async () => {
  await page.setContent('<details><summary>Full citation</summary>' + valid + '</details>');
  await assertCitation(page, expected);
  assert.ok(await page.locator('details').evaluate(node => node.open));
});

test('real DOM checks reject missing, empty, placeholder, hidden and clipped citation bodies', async () => {
  for (const html of [
    '<h2>Full citation</h2><a>Publication record</a>',
    '<p class="paper-full-citation"></p>',
    '<p class="paper-full-citation">TODO</p>',
    '<div style="display:none">' + valid + '</div>',
    '<div style="opacity:0">' + valid + '</div>',
    '<div style="height:1px;overflow:hidden">' + valid + '</div>',
    '<p class="paper-full-citation" style="clip-path:inset(50%)">' + expected.text + '</p>',
    '<div style="clip-path:inset(50%)">' + valid + '</div>',
    '<p class="paper-full-citation"><span style="opacity:0">' + expected.text + '</span></p>',
    '<p class="paper-full-citation"><span style="color:transparent">' + expected.text + '</span></p>',
    '<p class="paper-full-citation"><span style="font-size:0">' + expected.text + '</span></p>',
    '<div style="width:1px;overflow-x:hidden"><div style="width:500px">' + valid + '</div></div>',
    valid + valid,
  ]) {
    await page.setContent(html);
    await assert.rejects(() => assertCitation(page, expected));
  }
});


test('known DOI must have exactly one matching link', async () => {
  const withDoi = {...expected, doi: '10.1000/checked'};
  const link = '<a href="https://doi.org/10.1000/checked">' + expected.text + '</a>';
  await page.setContent('<p class="paper-full-citation">' + link + '</p>');
  await assertCitation(page, withDoi);
  for (const html of [valid, '<p class="paper-full-citation">' +
    link.replace('10.1000/checked', '10.1000/wrong') + '</p>']) {
    await page.setContent(html);
    await assert.rejects(() => assertCitation(page, withDoi));
  }
});
