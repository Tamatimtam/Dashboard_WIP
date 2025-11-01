// Donut animation: sweep to target percent from text content
export function animateDonut() {
    const slice = document.querySelector('.donut .slice');
    const percentEl = document.querySelector('.donut .percent');
    if (!slice || !percentEl) return;
    const r = Number(slice.getAttribute('r'));
    const c = 2 * Math.PI * r;
    const target = Math.max(0, Math.min(1, parseInt(percentEl.textContent, 10) / 100));
    gsap.set(slice, { strokeDasharray: c, strokeDashoffset: c });
    gsap.to(slice, { strokeDashoffset: c * (1 - target), duration: 1.2, ease: 'power2.out', delay: 0.4 });
}
