$( document ).ready(function() {

  $("#show-all").click(function() {
    $(".container #gallery-all").removeClass("hidden")
    $(".container #gallery-latest").removeClass("hidden")
    $("#show-all").addClass("hidden")
    // alert("butts");
  });

  $("#show-latest").click(function() {
    $(".container #gallery-latest").removeClass("hidden")
  });

  $('.progress-pics').click(function() {
    var imgSrc = $(this).attr('src');
    window.open(imgSrc);
  });

  });
