function initFlickitySlider() {

   // Source
   // https://flickity.metafizzy.co/

   // Slider type: Cards

   $('[data-flickity-slider-type="catalogue"]').each(function (index) {

      var sliderIndexID = 'flickity-slider-type-cards-id-' + index;
      $(this).attr('id', sliderIndexID);

      var sliderThis = $(this);

      var flickitySliderGroup = document.querySelector('#' + sliderIndexID + ' .flickity-carousel');
      var flickitySlider = sliderThis.find('.flickity-carousel').flickity({
         // options
         watchCSS: true,
         contain: false,
         wrapAround: false,
         dragThreshold: 10,
         prevNextButtons: false,
         pageDots: false,
         selectedAttraction: 0.04,
         friction: 0.25,
         percentPosition: true,
         freeScroll: false,
         on: {
            change: function (index) {
              updatePagination();
              sliderThis.find('[data-flickity-dot-index="' + index + '"]').addClass('is--active').siblings().removeClass('is--active');
              sliderThis.find('[data-flickity-word-index="' + index + '"]').addClass('is--active').siblings().removeClass('is--active');
            }
         }
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
    
      // Generate dots
      var amountSlides = sliderThis.find('.flickity-slide').length;
      
      sliderThis.find('.dot').remove();
      sliderThis.find('[data-flickity-control="prev"]').attr('disabled', 'disabled');

      for (var i = 0; i < amountSlides; i++) {
        var dot = $('<div>', { 
            class: 'dot', 
            'data-flickity-dot-index': i // Set the data-flickity-dot-index attribute
        });
        
        if (i === 0) {
            dot.addClass('is--active'); // Add .is--active class to the first .dot
        }
        
        var dotInner = $('<div>', { class: 'dot-inner' }); // Create a .dot-inner div
        dot.append(dotInner); // Append .dot-inner inside .dot
        sliderThis.find('.flickity-dots').append(dot); // Append the whole structure to the body (or any other container)
      }
      
      // Select active slides with dot
      sliderThis.find('[data-flickity-dot-index]').on('click', function () {
        var dotIndex = $(this).attr('data-flickity-dot-index');
         flickitySlider.flickity('select', dotIndex);
      });
      
      // Search for words and add index
      $('.flickity-words-item').each(function(index) {
        $(this).attr('data-flickity-word-index', index); // Add data-flickity-word-index with the index value
      });
      $('[data-flickity-word-index="0"]').addClass('is--active');
      
   });

}