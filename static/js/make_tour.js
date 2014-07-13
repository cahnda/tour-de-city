$(document).ready(function(){
    $(".dialog").hide();
    totalChecked = 0;

  var dialogDisappear = function(dialogSelector){
      $(dialogSelector).fadeOut(260);
      $(".location-container").animate({"opacity" : "1.0"}, 300);
  }

  var dialogAppear = function(dialogSelector){
    $(".dialog").hide();
    $(dialogSelector).fadeIn(260);
    $(".location-container").animate({"opacity" : "0.3"}, 300);
  }

    // click events for .location-container and .dialog buttons
  $(".location-container").each(function(){

  	var locationSelector = ".location-container#" + this.id + " label";
  	var dialogSelector = ".dialog#" + this.id;
  	var hasBeenSelected = 0;

  	$(this).click(function(){
  	    $(".location-container").animate({"opacity" : "0.3"}, 300);
  	    $(this).addClass("active");
  	    dialogAppear(dialogSelector);  
  	});

  	$(dialogSelector + " .footer #cancel").click(function(){
  	    dialogDisappear(dialogSelector)
  	    $(locationSelector).removeClass("active");
  	    $(locationSelector + " input[type='checkbox']").prop("checked",
  								 false);
  	    if (hasBeenSelected == 1) {
  		totalChecked = totalChecked - 1; 
  		hasBeenSelected = 0;
  	    }
  	})

  	$(dialogSelector + " .footer #select").click(function(){
  		dialogDisappear(dialogSelector)

  		$(locationSelector + " input[type='checkbox']").prop("checked",
  								     true);

  		$(locationSelector).addClass("active");
  		if (hasBeenSelected == 0) {
  		    totalChecked = totalChecked + 1;
  		    hasBeenSelected = 1;
  		}
    })
  })
})