initLoader()

// Animation - Page Loader
function initLoader() {

  var tl = gsap.timeline();
  
  tl.set(".loading-screen .number-1 .number-wrap", {
    yPercent: 100,
    opacity: 1
  });

  tl.set(".loading-screen .number-ten-times .number-wrap", {
    yPercent: 10,
    opacity: 1
  });
  
  tl.set(".loading-screen .number-percentage", {
    yPercent: 200,
    opacity: 1
  }, "<");
 
  var randomNumbers1 = gsap.utils.random([2, 3, 4]);
  var randomNumbers2 = gsap.utils.random([5, 6]);
  var randomNumbers3 = gsap.utils.random([2, 5]);
  var randomNumbers4 = gsap.utils.random([7, 8, 9]);
   
  var loadingSpeedNumbers = 1.2;
  
  tl.to(".loading-screen .number-2 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: (randomNumbers1 - 1) * -10,
  }, "0.25");

  tl.to(".loading-screen .number-3 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: (randomNumbers3 - 1) * -10,
  }, "<");
  
  tl.to(".loading-screen .number-percentage", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: 0,
  }, "<");
   
  tl.to(".loading-screen .number-2 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: (randomNumbers2 - 1) * -10,
  });

  tl.to(".loading-screen .number-3 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: (randomNumbers4 - 1) * -10,
  }, "<");

  tl.to(".loading-screen .number-2 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: -90,
  });

  tl.to(".loading-screen .number-3 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: -90,
  }, "<");

  tl.to(".loading-screen .number-1 .number-wrap", {
    duration: loadingSpeedNumbers,
    ease: "Expo.easeInOut",
    yPercent: 0,
  }, "<");
   
  tl.to($('.loading-screen'), {
    autoAlpha: 0,
    ease: "linear",
    duration: 0.3,
  });
  
  tl.call(function () {
    initBasicFunctions();
  }, null, "< 0.2");
  
  // tl.fromTo($('.side'), {
  //   xPercent: -100,
  //   rotate: 0.001,
  // }, {
  //   xPercent: 0,
  //   rotate: 0.001,
  //   ease: Expo.easeInOut,
  //   duration: 1,
  //   clearProps: "all"
  // }, "<");
  
  tl.fromTo($('.sidebar'), {
    yPercent: -100,
    rotate: 0.001,
  }, {
    yPercent: 0,
    rotate: 0.001,
    ease: Expo.easeInOut,
    duration: 1,
    clearProps: "all"
  }, "<");
}

function initBasicFunctions() {
  $('[data-modal-toggler="toggle"]').click(function () {
    if ($('[data-modal-status]').attr('data-modal-status') == 'not-active') {
      $('[data-modal-status]').attr('data-modal-status', 'active');
        scroll.stop();
    } else {
      $('[data-modal-status]').attr('data-modal-status', 'not-active');
      scroll.start();
    }
  });

  // Close Modal
  $('[data-modal-toggler="close"]').click(function () {
    $('[data-modal-status]').attr('data-modal-status', 'not-active');
      scroll.start();
  });

  // Toggle Navigation
  $('[data-navigation-toggle="toggle"]').click(function () {
    if ($('[data-navigation-status]').attr('data-navigation-status') == 'not-active') {
      $('[data-navigation-status]').attr('data-navigation-status', 'active');
      scroll.stop();
    } else {
      $('[data-navigation-status]').attr('data-navigation-status', 'not-active');
      scroll.start();
    }
  });

  // Close Navigation
  $('[data-navigation-toggle="close"]').click(function () {
    $('[data-navigation-status]').attr('data-navigation-status', 'not-active');
    scroll.start();
  });

  // Countdown
  $('[data-countdown]').each(function() {
    let countDown = $(this);
    let countDownAmount = '035';

    // Function to calculate the days difference
    function calculateDaysFromToday(targetDate) {
        const today = new Date();
        const target = new Date(targetDate);

        // Calculate the difference in time
        const timeDifference = target - today;

        // Convert time difference from milliseconds to days
        const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));

        return daysDifference;
    }

    // Function to update the countdown element
    function updateCountdown() {
        const targetDate = countDown.attr('data-countdown');

        const daysLeft = calculateDaysFromToday(targetDate);
        

        function formatNumber(number) {
            return number.toString().padStart(3, '0');
        }

        if (daysLeft > 0) {
          countDownAmount = formatNumber(25);
        } else {
          countDownAmount = formatNumber(25);
        }
    }

    // Initialize the count
    updateCountdown();

    // Mapping of digits to their respective position
    const positionMap = {
        'X': 0, // 0% for "X" at the top
        '9': -9.09090909091, // -9.09%
        '8': -18.18181818182, // -18.18%
        '7': -27.27272727273, // -27.27%
        '6': -36.36363636364, // -36.36%
        '5': -45.45454545455, // -45.45%
        '4': -54.54545454546, // -54.54%
        '3': -63.63636363637, // -63.63%
        '2': -72.72727272728, // -72.72%
        '1': -81.81818181819, // -81.81%
        '0': -90.90909090910 // -90.90% for "0"
    };

    // Split the number into individual digits
    const digits = countDownAmount.split("");

    // Set dummy: hidden
    countDown.find('.count-down__number-dummy').css('opacity', '0').css('visibility', 'hidden');

    // Iterate through the numbers 9 to 0 and append them as span elements
    // for (let i = 9; i >= 0; i--) {
    //     countDown.find('[data-countdown-transform]').append(`<span class="count-down__number-span" data-countdown-number="${i}">${i}</span>`);
    // }
    if (!countDown.find('.count-down__number-span').length) {
        for (let i = 9; i >= 0; i--) {
            countDown.find('[data-countdown-transform]').append(`<span class="count-down__number-span" data-countdown-number="${i}">${i}</span>`);
        }
    }
    // Function to trigger GSAP animation (this can now be called externally)
    function startGsapAnimation() {
        // Find the elements that should have the transform applied
        const countdownTransformElements = countDown.find('[data-countdown-transform]');

        // Loop through each digit and apply the corresponding GSAP animation
        digits.forEach(function(digit, index) {
            const position = positionMap[digit]; // Get the position (as percentage value) from the map

            // Animate the countdown transform elements with GSAP
            gsap.to($(countdownTransformElements[index]), {
                yPercent: position,
                rotate: 0.001,
                ease: "smooth",
                duration: 2,
                delay: index * 0.25
            });
        });
    }

    // Expose the GSAP animation function for external use
    window.startCountdownAnimation = startGsapAnimation;
  });
  
  // Loop text
  $('[data-text-loop-init]').each(function(){
  
    const $wordList = $(this);
    const $words = $wordList.find('[data-text-loop-item]');
    const totalWords = $words.length;
    
    let currentIndex = 0;
    let intervalID = null;

    // Function to calculate Y position in percentage
    function getYPositionPercent() {
      const wordHeightPercent = 100 / totalWords; // Each word represents a percentage of the total height
      return -wordHeightPercent * currentIndex;
    }

    function moveWords() {
      currentIndex++;
      
      gsap.to($wordList, {
        yPercent: getYPositionPercent(),  // Move using percentages
        duration: 1.25,
        ease: "elastic.out(1, 0.4)",
        onComplete: function() {
          // Once the first word moves out of view, append it to the end
          if (currentIndex >= totalWords - 3) {
            $wordList.append($wordList.children().first());
            currentIndex--;
            
            // Reset position to make the movement seamless
            gsap.set($wordList, {yPercent: getYPositionPercent()});
          }
        }
      });
    }

    // Function to start the loop
    function startLoop() {
      if (!intervalID) {
        intervalID = setInterval(moveWords, 1500);
      }
    }

    // Function to stop the loop
    function stopLoop() {
      if (intervalID) {
        clearInterval(intervalID);
        intervalID = null;
      }
    }

    // ScrollTrigger to manage the pausing and resuming of the text loop
    ScrollTrigger.create({
      trigger: $wordList,
      start: "top bottom",  // When the top of the element enters the bottom of the viewport
      end: "bottom top",    // When the bottom of the element exits the top of the viewport
      onEnter: startLoop,   // Start the loop when entering the viewport
      onLeave: stopLoop,    // Pause the loop when leaving the viewport
      onEnterBack: startLoop, // Resume the loop when coming back
      onLeaveBack: stopLoop   // Pause the loop when scrolling up and the element leaves again
    });

    // Initial start of the loop
    startLoop();
  });
  
  // Loop text
  $('[data-loop-steps]').each(function(){
    let elements = $(this).children();
    let currentIndex = 0;
    let intervalDuration = 2000; // 2 seconds

    function activateNextElement() {
      // Remove 'active' class from all elements
      elements.removeClass('active');
      
      // Add 'active' class to the current element
      elements.eq(currentIndex).addClass('active');

      // Update the current index
      currentIndex = (currentIndex + 1) % elements.length; // Loop back to 0 when reaching the last element
    }

    // Call the function every 2 seconds
    activateNextElement(); // Activate first element immediately
    setInterval(activateNextElement, intervalDuration);
  });

  // Accordion
  $('[data-accordion-toggle]').click(function(){
    if ($(this).closest('[data-accordion-status]').attr('data-accordion-status') == 'active') {
      $(this).closest('[data-accordion-status]').attr('data-accordion-status', 'not-active');
    }
    else {
      $(this).closest('[data-accordion-status]').attr('data-accordion-status', 'active');
    }
    setTimeout(function() {
      ScrollTrigger.refresh();
    }, 735);
  });


  // Animation - Page Enter
  const staggerDefault = 0.2;  // Default stagger time

  function pageTransitionOut() {
      var tl = gsap.timeline();
      
      tl.fromTo($('[data-animation="bounce"]'), {
          scale: 0.5,
          rotate: () => gsap.utils.random([-5, 5]),
      }, {
          rotate: 0.001,
          scale: 1,
          ease: "elastic.out(1,0.75)",
          duration: 0.8,
          stagger: staggerDefault * 0.75,
      }, 0.3);
      
      tl.fromTo($('[data-animation="bounce"]'), {
          autoAlpha: 0,
      }, {
          autoAlpha: 1,
          ease: "Expo.easeOut",
          duration: 0.8,
          stagger: staggerDefault * 0.75
      }, "<");
      
      tl.call(function () {
        console.log('Starting countdown animation...');
        window.startCountdownAnimation();  // Make sure this function exists
      }, null, "< 1.5");
      
      // tl.call(function () {
      //     console.log('Starting scroll...');
      //     scroll.start();  // Make sure this function exists
      // }, null, 0);
  }

  pageTransitionOut();
  if (document.querySelector("[data-count-up-group]")) {
    // Scrolltrigger Animation: Count Up
    $("[data-count-up-group]").each(function (index) {
        let triggerElement = $(this);
        let targetElements = $(this).find("[data-count-up]");

        targetElements.each(function() {
            let targetElement = $(this);

            // Normalize the innerText by removing periods and converting it to a number
            let currentText = targetElement.text().trim();
            let normalizedValue;

            if (currentText.includes(".")) {
                normalizedValue = parseInt(currentText.replace(/\./g, ""), 10);
            } else {
                normalizedValue = parseInt(currentText, 10);
            }

            targetElement.text(normalizedValue); // Set the text to the normalized value

            // Create a separate timeline for each target element
            let tl = gsap.timeline({
                scrollTrigger: {
                    trigger: triggerElement,
                    start: "0% 100%",
                    end: "100% 0%",
                    onEnter: () => tl.play(),
                }
            });

            // Animate from 0 (or any custom value) to the original normalized value
            tl.fromTo(targetElement, 
                {
                    innerText: 0 // Starting value (you can customize this if needed)
                }, 
                {
                    duration: 2,
                    ease: Expo.easeOut,
                    innerText: normalizedValue, // Target value
                    delay: 0.25,
                    roundProps: "innerText",
                    onUpdate: function() {
                        this.targets().forEach(target => {
                            const val = gsap.getProperty(target, "innerText");
                            target.innerText = numberWithCommas(Math.round(val)); // Ensure the number is rounded and formatted correctly
                        });
                    },
                }, 
                "<"
            );
        });

        function numberWithCommas(n) {
            var parts = n.toString().split(".");
            parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, "."); // Add the period as thousands separator
            return parts.join(".");
        }
    });
  }
}

initFlickitySlider();

function initFlickitySlider() {
  $(document).ready(function () {

    $('[data-flickity-slider-type="catalogue"]').each(function (index) {
      var sliderIndexID = 'flickity-slider-card-id-' + index;
      $(this).attr('id', sliderIndexID);

      var sliderThis = $(this);
      var flickitySlider = sliderThis.find('.flickity-carousel').flickity({
        // Flickity options
        // watchCSS: true,
        contain: false,
        wrapAround: false,
        dragThreshold: 10,
        prevNextButtons: false,
        pageDots: false,
        selectedAttraction: 0.04,
        friction: 0.25,
        percentPosition: true,
        freeScroll: false,
      });

      
      // Flickity instance
      var flkty = flickitySlider.data('flickity');

      // previous
      var prevButton = sliderThis.find('[data-flickity-control="prev"]').on('click', function () {
        flickitySlider.flickity('previous');
      });
      // next
      var nextButton = sliderThis.find('[data-flickity-control="next"]').on('click', function () {
        flickitySlider.flickity('next');
      });

      var inviewColumns = 1;

      function updatePagination() {
        // enable/disable previous/next buttons
        if (!flkty.cells[flkty.selectedIndex - 1]) {
            prevButton.attr('disabled', 'disabled').addClass('is--disabled');
            nextButton.removeAttr('disabled').removeClass('is--disabled'); // <-- remove disabled from the next
        } else if (!flkty.cells[flkty.selectedIndex + parseInt(inviewColumns)]) {
            nextButton.attr('disabled', 'disabled').addClass('is--disabled');
            prevButton.removeAttr('disabled').removeClass('is--disabled'); //<-- remove disabled from the prev
        } else {
            prevButton.removeAttr('disabled').removeClass('is--disabled');
            nextButton.removeAttr('disabled').removeClass('is--disabled');
        }
      }
      

      // Generate and append dots for navigation
      var amountSlides = sliderThis.find('.flickity-slide').length;
      sliderThis.find('.dot').remove();  // Remove existing dots if any
      sliderThis.find('[data-flickity-control="prev"]').attr('disabled', 'disabled');

      // Generate dots
      for (var i = 0; i < amountSlides; i++) {
        var dot = $('<div>', {
          class: 'dot',
          'data-flickity-dot-index': i
        });

        if (i === 0) {
          dot.addClass('is--active'); // Mark first dot as active
        }

        var dotInner = $('<div>', { class: 'dot-inner' }); // Create inner element for the dot
        dot.append(dotInner); // Append the inner element inside the dot
        sliderThis.find('.flickity-dots').append(dot); // Append the dot structure
      }
      sliderThis.find('[data-flickity-dot-index]').on('click', function () {
        var dotIndex = $(this).attr('data-flickity-dot-index');
         flickitySlider.flickity('select', dotIndex);
      });
      $('.flickity-words-item').each(function(index) {
        $(this).attr('data-flickity-word-index', index); // Add data-flickity-word-index with the index value
      });
      $('[data-flickity-word-index="0"]').addClass('is--active');

      flickitySlider.on('change.flickity', function (event, index) {
        updatePagination();
        sliderThis.find('[data-flickity-dot-index="' + index + '"]').addClass('is--active').siblings().removeClass('is--active');
        sliderThis.find('[data-flickity-word-index="' + index + '"]').addClass('is--active').siblings().removeClass('is--active');
      });

    });

  });
}



function updateFontSize() {
  const minFontSize = 5;       // Minimum font size in px
  const maxFontSize = 14.2;     // Maximum font size in px
  if (window.innerWidth >= 992) {
    const vwFontSize = window.innerWidth / 100 * 0.85;
    const clampedSize = Math.max(minFontSize, Math.min(vwFontSize, maxFontSize));
    document.documentElement.style.setProperty('--size-font', `${clampedSize}px`);
  } else if (window.innerWidth >= 768 && window.innerWidth <= 991){
    const vwFontSize = window.innerWidth / 100 * 1.12;
    const clampedSize = Math.max(minFontSize, Math.min(vwFontSize, maxFontSize));
    document.documentElement.style.setProperty('--size-font', `${clampedSize}px`);
  } else {
    const vwFontSize = window.innerWidth / 100 * 2;
    const clampedSize = Math.max(minFontSize, Math.min(vwFontSize, maxFontSize));
    document.documentElement.style.setProperty('--size-font', `${clampedSize}px`);
  }
}

// Initialize the font size on load and on window resize
window.addEventListener('resize', updateFontSize);
updateFontSize(); // Initial call when the page loads


document.addEventListener('scroll', () => {
  const element = document.querySelector('[data-scrolling-started]');
  if (element) {
    if (window.scrollY > 0) {
      element.setAttribute('data-scrolling-started', 'true');
    } else {
      element.setAttribute('data-scrolling-started', 'false');
    }
  }
});
