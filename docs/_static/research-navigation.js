/* Keep bookmarks to the former combined research page at their original topic. */
(() => {
    const destinations = {
        'research-direction-structural-wind': 'StructuralWindEngineering.html',
        'structural-wind-engineering': 'StructuralWindEngineering.html',
        'building-wind-project-support': 'StructuralWindEngineering.html#building-wind-project-support',
        'research-project': 'StructuralWindEngineering.html#building-wind-project-support',
        id1: 'StructuralWindEngineering.html#numerical-wind-tunnel',
        id2: 'StructuralWindEngineering.html#structural-wind-resistance',
        'research-direction-floating-wind': 'MarineEnergyStructures.html',
        'floating-offshore-wind-turbine': 'MarineEnergyStructures.html',
        'marine-energy-structures': 'MarineEnergyStructures.html',
        'floating-wind-project-support': 'MarineEnergyStructures.html#floating-wind-project-support',
        id3: 'MarineEnergyStructures.html#floating-wind-integrated-analysis',
        id4: 'MarineEnergyStructures.html#concrete-floating-structures',
        id5: 'MarineEnergyStructures.html#numerical-wave-basin',
        id6: 'MarineEnergyStructures.html#floating-wind-figures',
        id7: 'MarineEnergyStructures.html#floating-wind-project-support',
        id8: 'MarineEnergyStructures.html#floating-wind-dimensions-figure',
        id9: 'MarineEnergyStructures.html#concrete-floater-design-figure',
        id10: 'MarineEnergyStructures.html#floating-wind-coupling-figure',
    };
    const englishDestinations = {
        'structural-wind-engineering': 'StructuralWindEngineering.html',
        'marine-energy-structures': 'MarineEnergyStructures.html',
        'floating-offshore-wind': 'MarineEnergyStructures.html',
    };
    const followBookmark = () => {
        if (!location.pathname.endsWith('/Research.html')) return;
        const targets = location.pathname.endsWith('/en/Research.html') ? englishDestinations : destinations;
        let fragment;
        try { fragment = decodeURIComponent(location.hash.slice(1)); }
        catch { return; }
        if (!Object.hasOwn(targets, fragment)) return;
        location.replace(new URL(targets[fragment], location.href).href);
    };
    followBookmark();
    addEventListener('hashchange', followBookmark);
})();
