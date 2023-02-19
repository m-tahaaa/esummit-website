function secondsToDhms(seconds) {
    if (seconds < 0) {
        document.getElementById("counter").style.display = "None";
    }
    seconds = Number(seconds);
    var d = Math.floor(seconds / (3600*24));
    var h = Math.floor(seconds % (3600*24) / 3600);
    var m = Math.floor(seconds % 3600 / 60);
    var s = Math.floor(seconds % 60);
    if (d == 0) {
        document.getElementById("days").parentElement.classList.add("hidden");
        document.getElementById("mins").parentElement.classList.remove("col-span-2");
        document.getElementById("seconds").parentElement.classList.remove("hidden");
    }
    document.getElementById("days").innerText = d ;
    document.getElementById("hours").innerText = h ;
    document.getElementById("mins").innerText = m ;
    document.getElementById("seconds").innerText = s ;
}

function startTimer() {
    setInterval(countdown,1000)
}

function countdown() {
    let seconds = document.getElementById('time_diff').innerText;
    document.getElementById('time_diff').innerText = seconds - 1;
    // console.log(seconds)
    secondsToDhms(seconds)
}

document.addEventListener('DOMContentLoaded', startTimer());

const hiddentElements = document.querySelectorAll('.stagger-card');
console.log(hiddentElements);
const observer2 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        // console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
        else {
            entry.target.classList.remove("show");
        }
    });
})

hiddentElements.forEach((el) => observer2.observe(el));

const videos = document.querySelectorAll("video.lazy");

const lazyLoad = video => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const src = video.getAttribute("data-src");
        video.src = src;
        video.load();
        observer.disconnect();
      }
    });
  });
  observer.observe(video);
};

videos.forEach(lazyLoad);