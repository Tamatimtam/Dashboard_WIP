// Entrance animation timeline using GSAP
export function runEntrance() {
    const tl = gsap.timeline({ defaults: { ease: 'power2.out' } });
    tl.to(document.body, { opacity: 1, duration: 0.45 })
        .from('.topbar .title span', { y: 20, opacity: 0, stagger: 0.06, duration: 0.6 }, '-=0.1')
        .from('.actions .action-btn', { y: 8, opacity: 0, stagger: 0.05, duration: 0.4 }, '-=0.35')
        .from('.hero-frame', { y: 18, opacity: 0, duration: 0.6 }, '-=0.2')
        .from('.card', { y: 26, opacity: 0, stagger: 0.08, duration: 0.6 }, '-=0.1');
    return tl;
}

export function prepareBodyFade() { gsap.set(document.body, { opacity: 0 }); }
