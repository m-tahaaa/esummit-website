gsap.registerPlugin(ScrollTrigger) 
const tl = gsap.timeline({
    scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom top",
        scrub: true
    }
});

gsap.utils.toArray(".layer").forEach(layer => {
    const depth = layer.dataset.depth;
    const scale = layer.dataset.scale;
    const movement = -(layer.offsetHeight * depth)
    tl.to(layer, { y: movement, ease: "none",scale:scale }, 0)
});