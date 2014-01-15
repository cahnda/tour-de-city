$(window).load(function() {
	locationPicker($('iframe')[0]);

	$("#venue-form").hide();
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
			$(".row, #venue-form").fadeOut();
			$("input[type=radio], input[type=checkbox]").prop("checked", false);
		}
		else {
			$(this).addClass("clicked").text("Cancel");
			$("#row1").fadeIn();
		}
	});

	$("#row1 input[type=radio]").click(function(){
		$(this).parent().parent().next(".row").fadeIn();
	})

	$("#row2 input[type=radio]").click(function(){
		$("#venue-form").fadeIn();
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

	$('#venue-form input[type=checkbox]').change(function() {
		$(this).parent().toggleClass('active', this.checked);
	});

})
