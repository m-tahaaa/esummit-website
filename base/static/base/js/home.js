gsap.registerPlugin(ScrollTrigger) 
const tl = gsap.timeline({
    scrollTrigger: {
        trigger: "#hero",
        start: "top top",
        end: "bottom top",
        scrub: 0.2
    }
});
const sectionTrigger = {
    trigger: ".about-section",
    start: "top 40%",
    end: "top 30%",
    scrub: 1,
    markers: false
}
// const tl2 = gsap.timeline({
//     scrollTrigger: {
//         trigger: ".about-section",
//         start: "top 60%",
//         end: "top 50%",
//         scrub: true ,
//         markers: true
//     }
// });

gsap.utils.toArray(".layer").forEach(layer => {
    const depth = layer.dataset.depth;
    const scale = layer.dataset.scale;
    const movement = -(layer.offsetHeight * depth)
    tl.to(layer, { y: movement, ease: "none", scale:scale, duration: .2}, 0)
});


gsap.from(".lamp",{
    scrollTrigger: sectionTrigger,
    scale: .5,
    opacity: .2,
    y: 200,
    duration: .3
})

gsap.from(".about-content",{
    scrollTrigger: sectionTrigger,
    opacity: 0,
    y: 50,
    duration: .3
})