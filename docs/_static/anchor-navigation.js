/* Shared fragment navigation. Keep IDs/history native and scroll each container once. */
document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.site-header');
    const tools = document.querySelector('.wy-nav-top');
    const panel = document.querySelector('.wy-side-scroll');
    let following = Boolean(location.hash);
    let focusNext = false;
    let frame;

    // RTD reset() calls link.scrollIntoView() after every hash change. Its default
    // "all ancestors" behavior scrolls the article a second time. Adapt only the
    // theme's menu elements; never change Element.prototype or the theme's tree.
    panel?.querySelectorAll('.wy-menu-vertical a').forEach(link => {
        link.scrollIntoView = () => {
            const item = link.getBoundingClientRect();
            const box = panel.getBoundingClientRect();
            if (item.top < box.top) panel.scrollTop += item.top - box.top;
            else if (item.bottom > box.bottom) panel.scrollTop += item.bottom - box.bottom;
        };
    });

    const fragmentTarget = () => {
        let id;
        try { id = decodeURIComponent(location.hash.slice(1)); }
        catch { return null; }
        const target = document.getElementById(id);
        if (!target) return null;
        const label = target.getAttribute('aria-labelledby');
        if (label) {
            const heading = document.getElementById(label.split(/\s+/)[0]);
            if (heading?.matches('h1,h2,h3,h4,h5,h6')) return heading;
        }
        if (target.matches('section')) {
            return [...target.children].find(node => node.matches('h1,h2,h3,h4,h5,h6')) || target;
        }
        // Docutils keeps historical labels as empty inline spans before a title.
        // A citation/figure/equation label retains its own target, not its section.
        if (target.matches('span') && !target.textContent.trim()) {
            // The homepage's historical label is the first child of a labelled
            // section whose title is nested in a layout wrapper.
            const section = target.parentElement;
            if (!target.previousElementSibling && section?.matches('section[aria-labelledby]')) {
                const heading = document.getElementById(section.getAttribute('aria-labelledby').split(/\s+/)[0]);
                if (heading?.matches('h1,h2,h3,h4,h5,h6')) return heading;
            }
            let next = target.nextElementSibling;
            while (next?.matches('span') && !next.textContent.trim()) next = next.nextElementSibling;
            if (next?.matches('h1,h2,h3,h4,h5,h6')) return next;
        }
        return target;
    };
    const inset = () => {
        const height = element => element && getComputedStyle(element).display !== 'none'
            ? element.getBoundingClientRect().height : 0;
        const gap = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--anchor-gap')) || 0;
        return height(header) + height(tools) + gap;
    };
    const align = () => {
        frame = undefined;
        if (!following) return;
        const target = fragmentTarget();
        if (!target) return;
        const maximum = Math.max(0, document.documentElement.scrollHeight - innerHeight);
        const top = Math.min(maximum, Math.max(0, scrollY + target.getBoundingClientRect().top - inset()));
        // Coordinates already include the measured header stack. scrollIntoView
        // here would apply CSS scroll-margin again and duplicate the offset.
        if (Math.abs(scrollY - top) > 1) scrollTo({top, left: scrollX, behavior: 'instant'});
        if (focusNext) {
            focusNext = false;
            const temporary = !target.hasAttribute('tabindex');
            if (temporary) target.setAttribute('tabindex', '-1');
            target.focus({preventScroll: true});
            if (temporary) target.addEventListener('blur', () => target.removeAttribute('tabindex'), {once: true});
        }
    };
    const schedule = () => {
        if (following && frame === undefined) frame = requestAnimationFrame(align);
    };
    // Content may settle after images, fonts or MathJax. Follow the selected
    // fragment through that layout, but never pull a reader back after input.
    ['wheel', 'touchmove', 'pointerdown', 'keydown'].forEach(type => {
        addEventListener(type, () => { following = false; }, {passive: true});
    });
    addEventListener('hashchange', () => { following = true; schedule(); });
    const content = document.querySelector('.document, .home-main');
    if (content) new ResizeObserver(schedule).observe(content);
    if (header) new ResizeObserver(schedule).observe(header);
    if (tools) new ResizeObserver(schedule).observe(tools);
    addEventListener('load', async () => {
        await document.fonts.ready;
        schedule();
    }, {once: true});
    document.fonts.ready.then(schedule);
    schedule();

    document.addEventListener('click', event => {
        if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        const link = event.target.closest('a[href]');
        if (!link || link.target || link.hasAttribute('download')) return;
        const destination = new URL(link.href, location.href);
        if (destination.origin !== location.origin || destination.pathname !== location.pathname || destination.search !== location.search || !destination.hash) return;
        let id;
        try { id = decodeURIComponent(destination.hash.slice(1)); } catch { return; }
        if (!document.getElementById(id)) return;
        event.preventDefault();
        // Let RTD's delegated click handlers finish their tree update first.
        queueMicrotask(() => {
            const previous = location.href;
            if (destination.href !== previous) history.pushState(null, '', destination.href);
            focusNext = true;
            dispatchEvent(new HashChangeEvent('hashchange', {oldURL: previous, newURL: destination.href}));
        });
    });
});
