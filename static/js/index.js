$(window).load(function() {
	locationPicker($('iframe')[0]);

	$("#venue-info").hide();
	$("#venue-form").css('position', 'static');
})

$(document).ready(function(){
	if (navigator.geolocation){
		navigator.geolocation.getCurrentPosition(function(position){
			$("input[name='latitude']").val(position.coords.latitude);
			$("input[name='longitude']").val(position.coords.longitude);
		});
	}

	$("#start-button").click(function(){
		if($(this).hasClass("clicked")){
			$(this).removeClass("clicked").text("Start");
			$(".row, #venue-info").fadeOut();
			$("input[type=radio], input[type=checkbox]").prop("checked", false);
		}
		else {
			$(this).addClass("clicked").text("Cancel");
			$("#row1").fadeIn();
			$('html, body').animate({
        		scrollTop: $("#row1").offset().top
    		}, 500);
		}
	});

	$("#row1 input[type=radio]").click(function(){
		$(this).parent().parent().next(".row").fadeIn();
		$('html, body').animate({
        	scrollTop: $("#row2").offset().top
    	}, 500);
	})

	$("#row2 input[type=radio]").click(function(){
	    if ($("#row1 input:radio:checked").val() == "premade") {
		document.getElementById("venue-form").submit()
		return
	    }
		$("#venue-info").fadeIn();
		$('html, body').animate({
        		scrollTop: $("#venue-container").offset().top
    		}, 500);
		var $mapContainer = $('.map-container'),
			$venueContainer = $('#venue-container');

		function resizeMap() {
			var mapHeight = $mapContainer.outerHeight()
				venueHeight = $venueContainer.outerHeight();
			if (mapHeight != venueHeight) {
				$mapContainer.css('height', venueHeight);
			}
		}

		$(window).resize(resizeMap);
		resizeMap();
	})

	$('#venue-info input[type=checkbox]').change(function() {
		$(this).parent().toggleClass('active', this.checked);
	});

})
