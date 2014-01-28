$(document).ready(function(){
	$(".dialog").hide();
	totalChecked = 0;

	// click events for .location-container and .dialog buttons
	$(".location-container").each(function(){

	var locationSelector = ".location-container#" + this.id + " label";
	var dialogSelector = ".dialog#" + this.id;

	$(this).click(function(){
		$(".location-container").animate({"opacity" : "0.3"}, 300);
		$(this).addClass("active");
		dialogAppear(dialogSelector);
	});

	$(dialogSelector + " .footer #cancel").click(function(){
		dialogDisappear(dialogSelector)
		$(locationSelector).removeClass("active");
		$(locationSelector + " input[type='checkbox']").prop("checked", false);
	})

	$(dialogSelector + " .footer #select").click(function(){
		if (totalChecked < 3) {
		dialogDisappear(dialogSelector)
		$(locationSelector).addClass("active");
		totalChecked = totalChecked + 1;}
		else {
			alert ("You have already selected 3 locations");
		}

	})

	})

	var dialogDisappear = function(dialogSelector){
		$(dialogSelector).fadeOut(260);
		$(".location-container").animate({"opacity" : "1.0"}, 300);
	}

	var dialogAppear = function(dialogSelector){
		$(".dialog").hide();
		$(dialogSelector).fadeIn(260);
		$(".location-container").animate({"opacity" : "0.3"}, 300);
	}

})
