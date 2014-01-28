$(window).load(function() {

      $("#map-button").click(function(){
            if($(this).hasClass("click")){
                  $(this).removeClass("click").text("Show Map");
                  $("#final_map").fadeOut();
                  $("#final_summary").fadeIn();
            }
            else {
                  $(this).addClass("click").text("Show Summary");
                  $("#final_summary").fadeOut();
                  $("#final_map").fadeIn();       
            }
      });

      //Other
      $("#final_map").hide();

      //Google Maps
      var fwindow = $('iframe')[0].contentWindow;
      var fdocument = fwindow.document
      google = fwindow.google;
      map = fwindow.map.map;

      directionsService = new google.maps.DirectionsService();
      directionsDisplay = new google.maps.DirectionsRenderer();
      directionsDisplay.setMap(map);
      directionsDisplay.setPanel(fdocument.getElementById('directions-panel'));
      calcRoute();
});
