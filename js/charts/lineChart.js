// Line chart animation: draw from 0 to full length
export function animateLineChart() {
    const path = document.querySelector('.line-chart .line');
    if (!path) return;
    const len = path.getTotalLength();
    gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
    gsap.to(path, { strokeDashoffset: 0, duration: 1.6, ease: 'power2.out', delay: 0.3 });
}
