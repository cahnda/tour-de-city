$(window).load(function() {

      $("#map-button").click(function(){
            if($(this).hasClass("click")){
                  $(this).removeClass("click").text("View Tour");
                  $("#final_map").fadeOut();
            }
            else {
                  $(this).addClass("click").text("Hide Tour");
                  $("#final_map").fadeIn();       
            }
      });

      $("#stops-button").click(function(){
            if($(this).hasClass("click")){
                  $(this).removeClass("click").text("View Stops");
                  $("#stops").fadeOut(100);
            }
            else {
                  $(this).addClass("click").text("Hide Stops");
                  $("#stops").fadeIn(100);       
            }
      });

      //Other
      $("#final_map").hide();
      $("#stops").hide();

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

$(document).ready(function(){
	$("#rate-up, #rate-down").click(function(){
		var rate_json = {
			"rate_value" : this.value
		};
		$.ajax({
			type : "POST",
			url : "/tour=" + document.URL.split("tour=")[1],
			data : JSON.stringify(rate_json, null, '\t'),
			contentType : "application/json;charset=UTF-8",
		});
		$("#rate-up, #rate-down").fadeOut()
	})
})
