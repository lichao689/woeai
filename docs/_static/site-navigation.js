/* Keep the native RTD reader drawer accessible; site navigation uses details. */
document.addEventListener('DOMContentLoaded', () => {
    const siteMenu = document.querySelector('.site-mobile-navigation');
    const sidebar = document.querySelector('.wy-nav-side');
    const toggle = document.querySelector('.reader-toggle');
    const backdrop = document.querySelector('.reader-backdrop');
    const narrow = window.matchMedia('(max-width: 900px)');

    const closeReader = () => {
        document.querySelectorAll('[data-toggle="wy-nav-shift"], [data-toggle="rst-versions"]')
            .forEach(element => element.classList.remove('shift'));
    };
    const syncReader = () => {
        if (!sidebar || !toggle) return;
        const open = narrow.matches && sidebar.classList.contains('shift');
        toggle.setAttribute('aria-expanded', String(open));
        sidebar.inert = narrow.matches && !open;
        sidebar.setAttribute('aria-hidden', String(narrow.matches && !open));
        if (backdrop) backdrop.hidden = !open;
        if (open) {
            if (siteMenu) siteMenu.open = false;
            if (!sidebar.contains(document.activeElement)) {
                // Hosted RTD opens its search dialog when this input receives
                // focus. Opening contents should start at the current link.
                const initial = sidebar.querySelector('.wy-menu-vertical a.current, .wy-menu-vertical li.current > a')
                    || sidebar.querySelector('.reader-home-link');
                initial?.focus({preventScroll: true});
                if (initial?.closest('.wy-menu-vertical')) initial.scrollIntoView();
            }
        } else if (sidebar.contains(document.activeElement)) {
            toggle.focus();
        }
    };
    if (sidebar && toggle) {
        sidebar.id = 'reader-navigation';
        toggle.setAttribute('aria-controls', sidebar.id);
        new MutationObserver(syncReader).observe(sidebar, {attributes: true, attributeFilter: ['class']});
        backdrop?.addEventListener('click', closeReader);
        narrow.addEventListener('change', () => { closeReader(); syncReader(); });
        syncReader();
    }
    siteMenu?.addEventListener('toggle', () => { if (siteMenu.open) closeReader(); });
    document.addEventListener('click', event => {
        const link = event.target.closest('a[href]');
        if (siteMenu?.open && (!siteMenu.contains(event.target) || link)) siteMenu.open = false;
        if (link?.closest('.wy-menu-vertical')) closeReader();
    });
    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') {
            if (siteMenu?.open) {
                siteMenu.open = false;
                siteMenu.querySelector('summary').focus();
            }
            closeReader();
        }
        if (event.key !== 'Tab' || !narrow.matches || !sidebar?.classList.contains('shift')) return;
        const targets = [...sidebar.querySelectorAll('a[href], button, input, [tabindex="0"]')]
            .filter(element => element.getClientRects().length && !element.disabled);
        const first = targets[0], last = targets[targets.length - 1];
        if (event.shiftKey && document.activeElement === first) { last.focus(); event.preventDefault(); }
        else if (!event.shiftKey && document.activeElement === last) { first.focus(); event.preventDefault(); }
    });
});
