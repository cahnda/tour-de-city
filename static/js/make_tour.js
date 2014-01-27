totalChecked = 0;

$(document).ready(function(){
	$('.location input[type=checkbox]').change(function() {
		$(this).parent().toggleClass('active', this.checked);
	});
	var max = 3;
	var $checkboxes = $('.locations-form input[type=checkbox]');

	$checkboxes.change(function(){
		var current = $checkboxes.filter(':checked').length;
		$checkboxes.filter(':not(:checked)').prop('disabled', current >= max);
	});

	$(".dialog").hide();
});

window.onload = function () {

	var locContainers = $(".location-container");
	for(var locNum = 0; locNum < numLocs; locNum++){
		currLoc = locContainers[locNum];
		currLoc.onclick = function(){
			dialogContent = [];
			dialogAppear();
		}
	}

	var dialogAppear = function(){
		$("#dialog").fadeIn(260);
		$(".location-container").animate({"opacity" : "0.3"}, 260);
	}
};
