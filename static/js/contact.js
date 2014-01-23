$(document).ready(function(){

	var fadeTime = 650;

	$("textarea").focus(function(){
		$(this).stop().animate({height : "200px"});
		$("#contact").stop().animate({height : "450px"})
	}).focusout(function(){
		$(this).stop().animate({height : "50"});
		$("#contact").stop().animate({height : "300px"});
	})

	$("button").click(function(){
		//if(!$(this).hasClass("clicked"))
			//$("button").toggleClass("clicked");
		var emailConButton = $("#email-contact")
		if(emailConButton.hasClass("clicked")){
			$("#email-info").hide();
			$("#phone-info").fadeIn(fadeTime);
		}
		else {
			$("#phone-info").hide();
			$("#email-info").fadeIn(fadeTime);
		}
		$("button").toggleClass("clicked")
	})
})
