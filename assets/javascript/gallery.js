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
    var imgSrc = $('.progress-pics').attr('src');
    console.log(imgSrc)
    window.location.replace(imgSrc)
  });

  });
