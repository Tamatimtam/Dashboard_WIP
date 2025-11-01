// Reusable hover lift micro-interaction
export function addHoverLift(selector, lift = 6) {
    const items = document.querySelectorAll(selector);
    items.forEach((el) => {
        const enter = () => gsap.to(el, { y: -lift, duration: 0.25, ease: 'power2.out' });
        const leave = () => gsap.to(el, { y: 0, duration: 0.3, ease: 'power2.inOut' });
        el.addEventListener('pointerenter', enter);
        el.addEventListener('pointerleave', leave);
        el.addEventListener('focus', enter);
        el.addEventListener('blur', leave);
    });
}
