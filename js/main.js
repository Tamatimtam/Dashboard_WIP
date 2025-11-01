// Main app bootstrap (ESM). Keeps concerns separated and DRY.
// GSAP is loaded globally via CDN before this module executes.

import { prepareBodyFade, runEntrance } from './animations/entrance.js';
import { addHoverLift } from './animations/hoverLift.js';
import { animateLineChart } from './charts/lineChart.js';
import { animateBars } from './charts/bars.js';
import { animateDonut } from './charts/donut.js';

// Respect reduced motion early: if set, skip complex animation sequences.
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReduced) {
    prepareBodyFade();
}

window.addEventListener('DOMContentLoaded', () => {
    if (!prefersReduced) {
        runEntrance();
    }
    // Micro-interactions
    addHoverLift('.card', 4);
    addHoverLift('.action-btn', 3);

    // Charts
    if (!prefersReduced) {
        animateLineChart();
        animateBars();
        animateDonut();
    }
});
