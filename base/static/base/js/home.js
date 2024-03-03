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

window.addEventListener('load',()=>{
    gsap.to(cardsWrapper, {
        x: () => window.innerWidth*(.9) - cardsWrapper.scrollWidth,
        ease: "none",
        scrollTrigger: {
            trigger: ".speakers-section",
            start: "top top",
            end: "+=" + (cards.length / 2) * 100 + "%",
            scrub: 1,
            pin: true,
            markers: false
        }
    });
})

// gsap.utils.toArray(".speaker").forEach( (speaker, i) => {
//     gsap.from(speaker, {
//         scrollTrigger: {
//             trigger: speaker,
//             start: i* cardsWrapper.offsetWidth /11 + "px 40%",
//             end: "+="+ window.offsetWidth *.4 + "px",
//             scrub: 1,
//             markers: true
//         },
//         scale: .5,
//         opacity: .5
//     })
// })

// cards.forEach((card, index) => {
//     gsap.from(card, {
//         opacity: 0,
//         x: () => index * 100, // Adjust the animation position based on the index of the card
//         ease: "power1.inOut", // Choose the easing function
//         duration: 1, // Set the duration of the animation
//         scrollTrigger: {
//             trigger: card,
//             start: "top bottom", // Change the start position of the animation as needed
//             end: "bottom top", // Change the end position of the animation as needed
//             scrub: true, // Allow the animation to scrub along with the scroll
//             markers: true // Show markers for debugging
//         }
//     });
// });
