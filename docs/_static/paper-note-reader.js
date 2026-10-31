/* Paper-note reading layout and an opt-in compact contents control on narrow screens. */
(() => {
  const contents = document.querySelector('.rst-content nav.contents.local');
  if (!contents) return;
  const cover = contents.previousElementSibling;
  if (cover?.matches('a.image-reference')) {
    const lead = document.createElement('div');
    lead.className = 'paper-note-lead';
    contents.parentNode.insertBefore(lead, contents);
    lead.append(cover, contents);
  }

  const mobile = window.matchMedia('(max-width: 760px)');
  const title = contents.querySelector('.topic-title');
  const list = contents.querySelector(':scope > ul');
  if (!title || !list) return;
  const listId = contents.id ? `${contents.id}-list` : 'paper-note-contents-list';
  list.id = listId;
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'paper-contents-toggle';
  button.setAttribute('aria-controls', listId);
  button.setAttribute('aria-expanded', 'false');
  title.after(button);

  function syncContents() {
    if (mobile.matches) {
      const expanded = button.getAttribute('aria-expanded') === 'true';
      list.hidden = !expanded;
      button.hidden = false;
      button.textContent = expanded ? '收起本页目录' : '展开本页目录';
    } else {
      list.hidden = false;
      button.hidden = true;
      button.setAttribute('aria-expanded', 'false');
    }
  }

  button.addEventListener('click', () => {
    button.setAttribute('aria-expanded', button.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
    syncContents();
  });
  mobile.addEventListener('change', syncContents);
  syncContents();
})();
