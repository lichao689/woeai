/* Read-only publication workflow board. No storage, mutations or external API. */
(function (root) {
  'use strict';
  const STATUS = {
    unregistered: '未登记', planned: '已计划', drafting: '制作中',
    awaiting_audit: '待全文核验', verified: '已核验', blocked: '受阻',
    awaiting_review: '待审核', draft_created: '草稿已创建 · 待预览',
    ready_to_publish: '已预览 · 待发布', published: '已发布'
  };
  const COLUMNS = [['unknown', '未登记'], ['working', '制作中'], ['review', '待核验 / 审核'], ['blocked', '受阻'], ['complete', '已完成']];
  function columnFor(workflow, track) {
    const status = workflow.status;
    if ((track === 'rtd' && status === 'verified') || (track === 'wechat' && status === 'published')) {
      return workflow.verification_current === true ? 'complete' : 'review';
    }
    if (['awaiting_audit', 'awaiting_review', 'draft_created', 'ready_to_publish'].includes(status)) return 'review';
    if (status === 'blocked') return 'blocked';
    if (['planned', 'drafting'].includes(status)) return 'working';
    return 'unknown';
  }
  function filterPapers(papers, filters) {
    const track = filters.track || 'rtd';
    const query = (filters.query || '').trim().toLowerCase().replace(/^https?:\/\/(?:dx\.)?doi\.org\//, '');
    return papers.filter(paper =>
      (!query || `${paper.title} ${paper.doi}`.toLowerCase().includes(query)) &&
      (!filters.year || String(paper.year) === filters.year) &&
      (!filters.direction || [paper.family, paper.subdirection].includes(filters.direction)) &&
      (!filters.status || paper[track].status === filters.status) &&
      (!filters.unfinished || columnFor(paper[track], track) !== 'complete')
    );
  }
  const api = { columnFor, filterPapers, STATUS, COLUMNS };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.PublicationBoard = api;
})(typeof window !== 'undefined' ? window : globalThis);

(function () {
  'use strict';
  if (typeof document === 'undefined') return;
  const host = document.getElementById('publication-board');
  if (!host) return;
  const { columnFor, filterPapers, STATUS } = window.PublicationBoard;
  const controls = document.getElementById('board-filters');
  const results = document.getElementById('board-results');
  const summary = document.getElementById('board-summary');
  const notice = document.getElementById('board-notice');
  let papers = [];
  let track = 'rtd';
  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  function appendLinks(container, links) {
    links.forEach(link => {
      // Generated links are allowlisted; retain defense in depth at the DOM sink.
      if (!/^(https:\/\/(github\.com\/lichao689\/woeai\/blob\/main\/|doi\.org\/|mp\.weixin\.qq\.com\/s)|paper-notes\/ref-[\w-]+\.html$|Publications\.html#ref-[\w-]+$)/.test(link.url)) return;
      const a = el('a', link.label);
      a.href = link.url;
      container.append(a);
    });
  }
  function statusText(workflow) {
    const label = STATUS[workflow.status] || '未知状态';
    return workflow.verification_current === false ? `${label} · 核验已失效` : label;
  }
  function detailTrack(paper, channel) {
    const workflow = paper[channel];
    const section = el('section', undefined, 'board-track-detail');
    section.append(el('h4', channel === 'rtd' ? 'RTD 全文精解' : '微信公众号'));
    section.append(el('p', statusText(workflow), 'board-detail-status'));
    if (channel === 'rtd') section.append(el('p', `页面类型：${{legacy_intro:'历史导读',full_paper:'全文型',unregistered:'未登记'}[workflow.kind] || '未登记'}`));
    else section.append(el('p', `公众号选题：${workflow.selected ? '已选' : '未选'}`));
    const gaps = el('ul', undefined, 'board-gaps');
    const checkWarnings = new Set((workflow.checks || [])
      .filter(check => check.value !== true)
      .map(check => `${check.label}：${check.value === false ? '未通过' : '未记录'}`));
    (workflow.gaps || []).filter(gap => !checkWarnings.has(gap))
      .forEach(gap => gaps.append(el('li', gap)));
    if (gaps.children.length) section.append(gaps);
    const checks = el('ul', undefined, 'board-checks');
    (workflow.checks || []).forEach(check => {
      const value = check.value === true ? '已记录通过' : check.value === false ? '未通过' : '未记录';
      const stage = check.stage ? `（${STATUS[check.stage] || check.stage}阶段）` : '';
      checks.append(el('li', `${check.label}：${value}${stage}`));
    });
    section.append(checks);
    const links = el('div', undefined, 'board-links');
    appendLinks(links, workflow.links || []);
    (workflow.issues || []).forEach((url, index) => {
      if (!/^https:\/\/github\.com\/[\w.-]+\/[\w.-]+\/issues\/[1-9]\d*$/.test(url)) return;
      const a = el('a', `任务 Issue ${index + 1}`); a.href = url; links.append(a);
    });
    if (!links.children.length) links.append(el('span', '暂无已登记的内容或任务链接'));
    section.append(links);
    return section;
  }
  function paperRows(paper, index) {
    const row = el('tr', undefined, 'board-paper-row');
    const title = el('th', paper.title, 'board-title');
    title.setAttribute('scope', 'row');
    const direction = el('td', undefined, 'board-direction');
    direction.append(el('span', paper.family), el('span', paper.subdirection, 'board-subdirection'));
    row.append(title, el('td', String(paper.year || '未登记'), 'board-year'), direction);
    ['rtd', 'wechat'].forEach(channel => {
      const cell = el('td', statusText(paper[channel]), `board-status board-status-${columnFor(paper[channel], channel)}`);
      row.append(cell);
    });
    const action = el('td', undefined, 'board-action');
    const toggle = el('button', '查看详情');
    toggle.type = 'button';
    toggle.setAttribute('aria-label', `查看详情：${paper.title}`);
    toggle.setAttribute('aria-expanded', 'false');
    const detailRow = el('tr', undefined, 'board-detail-row');
    detailRow.id = `board-detail-${index}`;
    detailRow.hidden = true;
    toggle.setAttribute('aria-controls', detailRow.id);
    toggle.addEventListener('click', () => {
      detailRow.hidden = !detailRow.hidden;
      toggle.setAttribute('aria-expanded', String(!detailRow.hidden));
      toggle.textContent = detailRow.hidden ? '查看详情' : '收起详情';
      toggle.setAttribute('aria-label', `${toggle.textContent}：${paper.title}`);
    });
    action.append(toggle); row.append(action);
    const cell = el('td');
    cell.setAttribute('colspan', '6');
    const details = el('div', undefined, 'board-paper-detail');
    details.append(el('p', `DOI：${paper.doi || '未登记'}`, 'board-doi'));
    const sourceLabels = {unregistered:'未登记',planned:'已计划',acquired:'已取得',awaiting_audit:'待核验',verified:'已核验',blocked:'受阻'};
    details.append(el('p', `原论文来源核验：${sourceLabels[paper.source.status] || '未登记'}`));
    const bibliographyLinks = el('div', undefined, 'board-links');
    appendLinks(bibliographyLinks, paper.links || []); details.append(bibliographyLinks);
    const workflows = el('div', undefined, 'board-detail-workflows');
    workflows.append(detailTrack(paper, 'rtd'), detailTrack(paper, 'wechat'));
    details.append(workflows); cell.append(details); detailRow.append(cell);
    return [row, detailRow];
  }
  function values() {
    return {track, query: controls.elements.query.value, year: controls.elements.year.value,
      direction: controls.elements.direction.value, status: controls.elements.status.value,
      unfinished: controls.elements.unfinished.checked};
  }
  function render() {
    const matches = filterPapers(papers, values());
    notice.textContent = `${track === 'rtd' ? 'RTD 全文精解' : '微信公众号'} 筛选 · 显示 ${matches.length} / ${papers.length} 篇，按年份倒序`;
    results.replaceChildren();
    if (!matches.length) {
      results.append(el('p', '没有符合条件的论文。请调整筛选条件，或点击“重置筛选”。', 'board-empty-results'));
      return;
    }
    const table = el('table', undefined, 'board-table');
    table.append(el('caption', '论文制作进度：每行一篇论文，RTD 与公众号状态独立展示'));
    const head = el('thead');
    const headings = el('tr');
    ['题目', '年份', '研究方向', 'RTD 状态', '公众号状态', '详情'].forEach(label => {
      const heading = el('th', label); heading.setAttribute('scope', 'col'); headings.append(heading);
    });
    head.append(headings); table.append(head);
    const body = el('tbody');
    matches.forEach((paper, index) => body.append(...paperRows(paper, index)));
    table.append(body); results.append(table);
  }

  function populateStatuses() {
    const select = controls.elements.status;
    select.replaceChildren(new Option('全部状态', ''));
    const statuses = track === 'rtd' ? ['unregistered','planned','drafting','awaiting_audit','verified','blocked'] : ['unregistered','planned','drafting','awaiting_review','draft_created','ready_to_publish','published','blocked'];
    statuses.forEach(status => select.add(new Option(STATUS[status], status)));
  }
  document.querySelectorAll('[data-board-track]').forEach(button => button.addEventListener('click', () => {
    track = button.dataset.boardTrack;
    document.querySelectorAll('[data-board-track]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    populateStatuses(); render();
  }));
  controls.addEventListener('submit', event => event.preventDefault());
  controls.addEventListener('input', render);
  controls.addEventListener('change', render);
  document.getElementById('board-reset').addEventListener('click', () => {
    controls.reset(); render(); controls.elements.query.focus();
  });
  async function load() {
    try {
      const response = await fetch(host.dataset.source, {credentials:'omit', cache:'no-cache'});
      if (!response.ok) throw new Error('Board data unavailable');
      const data = await response.json();
      if (data.schema_version !== 1 || !Array.isArray(data.papers)) throw new Error('Board data format unsupported');
      papers = data.papers.slice().sort((a, b) => (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title));
      const metrics = [[papers.length,'论文总数'],[papers.filter(p=>p.rtd.status==='awaiting_audit').length,'RTD 待全文核验'],[papers.filter(p=>p.wechat.status==='draft_created').length,'公众号草稿待预览'],[papers.filter(p=>p.wechat.status==='published' && p.wechat.verification_current===true).length,'公众号已发布']];
      summary.replaceChildren();
      metrics.forEach(([count, label]) => { const metric=el('div'); metric.append(el('strong',String(count)),el('span',label)); summary.append(metric); });
      [...new Set(papers.map(p=>p.year).filter(Boolean))].sort((a,b)=>b-a).forEach(year=>controls.elements.year.add(new Option(String(year),String(year))));
      [...new Set(papers.map(p=>p.family))].forEach(family=>{
        controls.elements.direction.add(new Option(family,family));
        [...new Set(papers.filter(p=>p.family===family).map(p=>p.subdirection))].forEach(direction=>controls.elements.direction.add(new Option(`　${direction}`,direction)));
      });
      populateStatuses();
      document.querySelectorAll('#board-filters :disabled, [data-board-track]:disabled').forEach(control=>control.disabled=false);
      render();
    } catch (error) {
      notice.textContent = '进度数据加载失败。请刷新页面重试，或查看仓库中的进度清单。';
      results.replaceChildren();
    }
  }
  load();
})();
