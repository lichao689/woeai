/* Progressive publication filtering. Without JS, the complete bibliography remains unchanged. */
(() => {
  const slot = document.querySelector('.publication-browser-slot');
  if (!slot) return;
  const entries = Array.from(document.querySelectorAll('.rst-content .pub-entry'));
  if (!entries.length) return;

  const english = document.documentElement.lang === 'en';
  const normalize = value => value.toLocaleLowerCase().replace(/\s+/g, ' ').trim();
  const text = {
    searchLabel: english ? 'Search title, author, journal or DOI' : '搜索题名、作者、期刊或 DOI',
    searchPlaceholder: english ? 'Search publications' : '输入关键词',
    yearLabel: english ? 'Year' : '年份',
    directionLabel: english ? 'Research direction' : '研究方向',
    allYears: english ? 'All years' : '全部年份',
    allDirections: english ? 'All directions' : '全部方向',
    notesOnly: english ? 'With reading notes' : '只看有论文精解',
    reset: english ? 'Reset' : '清除筛选',
    count: (visible, total) => english ? `${visible} of ${total} publications` : `显示 ${visible} / ${total} 篇论文`,
    empty: english ? 'No matching publications. Clear the filters to see the full catalogue.' : '没有匹配的论文，可清除筛选后查看完整目录。'
  };

  entries.forEach(entry => {
    const meta = entry.querySelector('.pub-meta')?.textContent.replace(/\s+/g, ' ').trim() || '';
    const fullText = entry.textContent.replace(/\s+/g, ' ').trim();
    const year = fullText.match(/\b(?:19|20)\d{2}\b/)?.[0] || '';
    const metaParts = meta.split('·').map(part => part.trim());
    entry.dataset.year = year;
    entry.dataset.direction = metaParts.length > 1 ? metaParts.slice(1).join(' · ') : '';
    entry.dataset.search = normalize(fullText);
    entry.dataset.hasNote = entry.querySelector('.pub-title a[href*="paper-notes/"]') ? 'true' : 'false';
  });

  const years = [...new Set(entries.map(entry => entry.dataset.year).filter(Boolean))].sort().reverse();
  const directions = [...new Set(entries.map(entry => entry.dataset.direction).filter(Boolean))].sort();
  const hasNoteFilter = entries.some(entry => entry.dataset.hasNote === 'true');
  const form = document.createElement('form');
  form.className = 'publication-browser';
  form.setAttribute('role', 'search');
  form.setAttribute('aria-label', english ? 'Filter publications' : '筛选学术成果');

  const searchId = 'publication-query';
  const yearId = 'publication-year';
  const directionId = 'publication-direction';
  const noteId = 'publication-notes-only';
  form.innerHTML = `
    <div class="publication-filter publication-filter-search">
      <label for="${searchId}">${text.searchLabel}</label>
      <input id="${searchId}" type="search" placeholder="${text.searchPlaceholder}" autocomplete="off">
    </div>
    <div class="publication-filter">
      <label for="${yearId}">${text.yearLabel}</label>
      <select id="${yearId}"><option value="">${text.allYears}</option>${years.map(year => `<option value="${year}">${year}</option>`).join('')}</select>
    </div>
    ${directions.length ? `<div class="publication-filter"><label for="${directionId}">${text.directionLabel}</label><select id="${directionId}"><option value="">${text.allDirections}</option>${directions.map(direction => `<option value="${direction}">${direction}</option>`).join('')}</select></div>` : ''}
    ${hasNoteFilter ? `<label class="publication-note-filter" for="${noteId}"><input id="${noteId}" type="checkbox"><span>${text.notesOnly}</span></label>` : ''}
    <div class="publication-browser-status"><output aria-live="polite"></output><button type="button" class="publication-filter-reset">${text.reset}</button></div>
    <p class="publication-empty" hidden>${text.empty}</p>`;
  slot.replaceWith(form);

  const query = form.querySelector(`#${searchId}`);
  const year = form.querySelector(`#${yearId}`);
  const direction = form.querySelector(`#${directionId}`);
  const notesOnly = form.querySelector(`#${noteId}`);
  const output = form.querySelector('output');
  const empty = form.querySelector('.publication-empty');
  const sections = [];
  entries.forEach(entry => {
    let section = entry.closest('section');
    while (section && !section.querySelector(':scope > h1')) {
      if (!sections.includes(section)) sections.push(section);
      section = section.parentElement.closest('section');
    }
  });

  function applyFilters() {
    const needle = normalize(query.value);
    let visible = 0;
    entries.forEach(entry => {
      const matches = (!needle || entry.dataset.search.includes(needle))
        && (!year.value || entry.dataset.year === year.value)
        && (!direction || !direction.value || entry.dataset.direction === direction.value)
        && (!notesOnly || !notesOnly.checked || entry.dataset.hasNote === 'true');
      entry.hidden = !matches;
      if (matches) visible += 1;
    });
    sections.forEach(section => {
      const sectionEntries = entries.filter(entry => section.contains(entry));
      section.hidden = sectionEntries.length > 0 && !sectionEntries.some(entry => !entry.hidden);
    });
    output.value = text.count(visible, entries.length);
    empty.hidden = visible !== 0;
  }

  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', applyFilters);
  form.addEventListener('change', applyFilters);
  form.querySelector('.publication-filter-reset').addEventListener('click', () => {
    form.reset();
    applyFilters();
    query.focus();
  });
  applyFilters();
})();
