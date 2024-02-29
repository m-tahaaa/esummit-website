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
    tl.to(layer, { y: movement, ease: "none", scale: scale, duration: .2 }, 0)
});


gsap.from(".lamp", {
    scrollTrigger: sectionTrigger,
    scale: .5,
    opacity: .2,
    y: 200,
    duration: .3
})

gsap.from(".about-content", {
    scrollTrigger: sectionTrigger,
    opacity: 0,
    y: 50,
    duration: .3
})

// const speakers = document.querySelector('.speakers')
// const items = gsap.utils.toArray('.speakers item')
// const texts = gsap.utils.toArray('.item_info')
// const mask = document.querySelector('.mask')

// let scrollTween = gsap.to(div, {
//     xPercent: -100 * (div.length - 1),
//     ease: "none",
//     scrollTrigger: {
//         trigger: ".speakers",
//         pin: true,
//         scrub: 1,
//         end: "+=3000"
//     }
// })
// gsap.to(mask, {
//     width: "100%",
//     scrollTrigger: {
//         trigger: ".wrapper",
//         start: "top left",
//         scrub: 1

//     }
// })
// items.forEach(section => {
//     let text = div.querySelectorAll('.item')

//     gsap.from(text, {
//         y: -130,
//         opacity: 0,
//         durtion: 2,
//         ease: "elastic",
//         stagger: 0.1,
//         scrollTrigger: {
//             trigger: div,
//             containerAnimation: scrollTween,
//             start: "left center",
//             // markers: true
//         }
//     })
// })

gsap.registerPlugin(ScrollTrigger);

const cards = gsap.utils.toArray(".speaker");

const cardsWrapper = document.querySelector(".speaker-container");

gsap.to(cardsWrapper, {
    x: () => window.innerWidth - cardsWrapper.scrollWidth,
    ease: "none",
    scrollTrigger: {
        trigger: ".speakers-section",
        start: "top top",
        end: "+=" + (cards.length / 2) * 100 + "%",
        scrub: true,
        pin: true,
        markers: true
    }
});