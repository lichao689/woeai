/* Keep bookmarks to the former combined research page at their original topic. */
(() => {
    const destinations = {
        'research-direction-structural-wind': 'StructuralWindEngineering.html',
        'structural-wind-engineering': 'StructuralWindEngineering.html',
        'building-wind-project-support': 'StructuralWindEngineering.html#building-wind-project-support',
        'research-project': 'StructuralWindEngineering.html#building-wind-project-support',
        id1: 'NumericalWindTunnel.html',
        id2: 'StructuralWindResistance.html',
        'research-direction-floating-wind': 'MarineEnergyStructures.html',
        'floating-offshore-wind-turbine': 'MarineEnergyStructures.html',
        'marine-energy-structures': 'MarineEnergyStructures.html',
        'floating-wind-project-support': 'MarineEnergyStructures.html#floating-wind-project-support',
        id3: 'IntegratedAnalysis.html',
        id4: 'ConcreteFloatingStructures.html',
        id5: 'NumericalWaveBasin.html',
        id6: 'IntegratedAnalysis.html#floating-wind-figures',
        id7: 'MarineEnergyStructures.html#floating-wind-project-support',
        id8: 'IntegratedAnalysis.html#floating-wind-dimensions-figure',
        id9: 'ConcreteFloatingStructures.html#concrete-floater-design-figure',
        id10: 'IntegratedAnalysis.html#floating-wind-coupling-figure',
    };
    const englishDestinations = {
        'structural-wind-engineering': 'StructuralWindEngineering.html',
        'marine-energy-structures': 'MarineEnergyStructures.html',
        'floating-offshore-wind': 'MarineEnergyStructures.html',
    };
    const movedTopics = {
        'numerical-wind-tunnel': 'NumericalWindTunnel.html',
        'structural-wind-resistance': 'StructuralWindResistance.html',
        'floating-wind-integrated-analysis': 'IntegratedAnalysis.html',
        'concrete-floating-structures': 'ConcreteFloatingStructures.html',
        'numerical-wave-basin': 'NumericalWaveBasin.html',
        'floating-wind-figures': 'IntegratedAnalysis.html#floating-wind-figures',
        'floating-wind-dimensions-figure': 'IntegratedAnalysis.html#floating-wind-dimensions-figure',
        'concrete-floater-design-figure': 'ConcreteFloatingStructures.html#concrete-floater-design-figure',
        'floating-wind-coupling-figure': 'IntegratedAnalysis.html#floating-wind-coupling-figure',
        'story-ref-chen2024-jcp': 'NumericalWindTunnel.html#story-ref-chen2024-jcp',
        'story-ref-zhao2026-bs': 'NumericalWindTunnel.html#story-ref-zhao2026-bs',
        'story-ref-tang2025-jbe': 'StructuralWindResistance.html#story-ref-tang2025-jbe',
        'story-ref-zhou2023-ae': 'IntegratedAnalysis.html#story-ref-zhou2023-ae',
        'story-ref-zheng2023-jrse': 'IntegratedAnalysis.html#story-ref-zheng2023-jrse',
        'story-ref-he2026-oe-structural': 'ConcreteFloatingStructures.html#story-ref-he2026-oe-structural',
    };
    const englishMovedTopics = Object.fromEntries(Object.entries(movedTopics).flatMap(([anchor, target]) => {
        const translated = target.replace('#', '#en-');
        return [[anchor, translated], ['en-' + anchor, translated]];
    }));
    // IDs audited against the published 21a11d4 first-level HTML.
    const firstLevelDestinations = {
    "StructuralWindEngineering.html": {
        "id2": "StructuralWindEngineering.html",
        "id3": "StructuralWindEngineering.html",
        "id4": "StructuralWindEngineering.html#family-method-links",
        "id5": "NumericalWindTunnel.html",
        "id6": "StructuralWindResistance.html",
        "id7": "StructuralWindEngineering.html#subdirection-pages",
        "id8": "NumericalWindTunnel.html#story-ref-chen2024-jcp",
        "id9": "NumericalWindTunnel.html#story-ref-zhao2026-bs",
        "id10": "StructuralWindResistance.html#story-ref-tang2025-jbe",
        "id11": "StructuralWindEngineering.html",
        "id12": "StructuralWindEngineering.html#building-wind-project-support",
        "id13": "StructuralWindEngineering.html#wind-method-overview-figure",
        "id14": "NumericalWindTunnel.html#research-figure-ref-chen2024-jcp-fig17",
        "id15": "NumericalWindTunnel.html#research-figure-ref-chen2024-jcp-fig28",
        "id16": "NumericalWindTunnel.html#research-figure-ref-zhao2026-bs-fig02",
        "id17": "NumericalWindTunnel.html#research-figure-ref-zhao2026-bs-fig25",
        "id18": "StructuralWindResistance.html#research-figure-ref-tang2025-jbe-fig06",
        "id19": "StructuralWindResistance.html#research-figure-ref-tang2025-jbe-fig09"
    },
    "MarineEnergyStructures.html": {
        "id2": "MarineEnergyStructures.html",
        "id3": "MarineEnergyStructures.html",
        "id4": "MarineEnergyStructures.html#family-method-links",
        "id5": "IntegratedAnalysis.html",
        "id6": "ConcreteFloatingStructures.html",
        "id7": "NumericalWaveBasin.html",
        "id8": "MarineEnergyStructures.html#subdirection-pages",
        "id9": "IntegratedAnalysis.html#story-ref-zhou2023-ae",
        "id10": "ConcreteFloatingStructures.html#story-ref-he2026-oe-structural",
        "id11": "IntegratedAnalysis.html#story-ref-zheng2023-jrse",
        "id12": "MarineEnergyStructures.html",
        "id13": "MarineEnergyStructures.html#floating-wind-project-support",
        "id14": "IntegratedAnalysis.html#floating-wind-figures",
        "id15": "MarineEnergyStructures.html#marine-method-overview-figure",
        "id22": "IntegratedAnalysis.html#floating-wind-dimensions-figure",
        "id23": "ConcreteFloatingStructures.html#concrete-floater-design-figure",
        "id24": "IntegratedAnalysis.html#floating-wind-coupling-figure",
        "id16": "IntegratedAnalysis.html#research-figure-ref-zhou2023-ae-fig07",
        "id17": "IntegratedAnalysis.html#research-figure-ref-zhou2023-ae-fig23",
        "id18": "ConcreteFloatingStructures.html#research-figure-ref-he2026-oe-structural-fig07",
        "id19": "ConcreteFloatingStructures.html#research-figure-ref-he2026-oe-structural-fig16",
        "id20": "IntegratedAnalysis.html#research-figure-ref-zheng2023-jrse-fig07",
        "id21": "IntegratedAnalysis.html#research-figure-ref-zheng2023-jrse-fig17"
    }
};
    const englishFirstLevelDestinations = {
    "StructuralWindEngineering.html": {
        "id1": "StructuralWindEngineering.html#en-wind-method-overview-figure",
        "background": "StructuralWindEngineering.html",
        "research-questions": "StructuralWindEngineering.html",
        "open-questions": "StructuralWindEngineering.html",
        "methods-and-contributions": "StructuralWindEngineering.html#family-method-links",
        "evidence-in-practice": "StructuralWindEngineering.html#subdirection-pages",
        "publications-and-projects": "StructuralWindEngineering.html#en-building-wind-project-support",
        "cmrfg-coherent-mass-balanced-inflow": "NumericalWindTunnel.html#en-story-ref-chen2024-jcp",
        "urban-cfd-precompute-once-query-locally": "NumericalWindTunnel.html#en-story-ref-zhao2026-bs",
        "tbgnn-structural-connectivity-meets-storey-features": "StructuralWindResistance.html#en-story-ref-tang2025-jbe"
    },
    "MarineEnergyStructures.html": {
        "id1": "MarineEnergyStructures.html#en-marine-method-overview-figure",
        "background": "MarineEnergyStructures.html",
        "research-questions": "MarineEnergyStructures.html",
        "open-questions": "MarineEnergyStructures.html",
        "methods-and-contributions": "MarineEnergyStructures.html#family-method-links",
        "evidence-in-practice": "MarineEnergyStructures.html#subdirection-pages",
        "publications-and-projects": "MarineEnergyStructures.html#en-floating-wind-project-support",
        "long-term-optimisation-costfatigue-trade-offs": "IntegratedAnalysis.html#en-story-ref-zhou2023-ae",
        "concrete-platforms-from-long-term-response-to-strength": "ConcreteFloatingStructures.html#en-story-ref-he2026-oe-structural",
        "windwave-testing-heading-and-system-response": "IntegratedAnalysis.html#en-story-ref-zheng2023-jrse",
        "integrated-analysis": "IntegratedAnalysis.html"
    }
};
    const followBookmark = () => {
        if (!/\/(Research|StructuralWindEngineering|MarineEnergyStructures)\.html$/.test(location.pathname)) return;
        const english = /\/en\/[^/]+$/.test(location.pathname);
        const overview = location.pathname.endsWith('/Research.html');
        const page = location.pathname.split('/').pop();
        const targets = {...(overview ? (english ? englishDestinations : destinations) :
            (english ? englishFirstLevelDestinations[page] : firstLevelDestinations[page])),
            ...(english ? englishMovedTopics : movedTopics)};
        let fragment;
        try { fragment = decodeURIComponent(location.hash.slice(1)); }
        catch { return; }
        if (!Object.hasOwn(targets, fragment)) return;
        const target = new URL(targets[fragment], location.href).href;
        if (target === location.href) return;
        location.replace(target);
    };
    followBookmark();
    addEventListener('hashchange', followBookmark);
})();
