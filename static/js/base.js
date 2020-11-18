    // Get the current year for the footer
    $('#year').this(new Date().getFullYear());
    // Modify slider responsiveness
    $('.carousel').carousel({
      interval: 6000,
      pause: 'hover'
    });
    $('.slider').slick({
      infinite: true,
      slideToShow: 1,
      slideToScroll: 1
    });
    // console.log("test")
    // Lightbox Init
    $(document).on('click', '[data-toggle="lightbox"]', function (event) {
      event.preventDefault();
      $(this).ekkoLightbox();
    });
    // Video Play
    $(function () {
      // Auto play modal video from stackoverflow
      $(".video").click(function () {
        var theModal = $(this).data("target"),
          videoSRC = $(this).attr("data-video"),
          videoSRCauto = videoSRC + "?modestbranding=1&rel=0&controls=0&showinfo=0&html5=1&autoplay=1";
        $(theModal + ' iframe').attr('src', videoSRCauto);
        $(theModal + ' button.close').click(function () {
          $(theModal + ' iframe').attr('src', videoSRC);
        });
      });
    });
    //Get the go to top button
    var mybutton = document.getElementById("#myBtn");
    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        display = "block";
    } else {
        display = "none";
    }
    }
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    }
