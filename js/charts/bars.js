// Bars animation: grow from baseline in a stagger
export function animateBars() {
    const bars = document.querySelectorAll('.bars .bar');
    if (!bars.length) return;
    const tlBars = gsap.timeline({ defaults: { ease: 'power2.out' } });
    bars.forEach((rect, i) => {
        const y = Number(rect.getAttribute('y'));
        const h = Number(rect.getAttribute('height'));
        gsap.set(rect, { attr: { y: y + h, height: 0 } });
        tlBars.to(rect, { attr: { y, height: h }, duration: 0.6 }, i * 0.08);
    });
}
