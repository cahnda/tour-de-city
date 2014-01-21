$(document).ready(function(){

	var fadeTime = 650;

	$("#phone-contact").click(function(){
		$("#email-info").hide();
		$("#phone-info").fadeIn(fadeTime);
	})

	$("#email-contact").click(function(){
		$("#phone-info").hide();
		$("#email-info").fadeIn(fadeTime);
	})

	$("textarea").focus(function(){
		$(this).animate({height : "200px"});
		$("#contact").animate({height : "450px"})
	}).focusout(function(){
		$(this).animate({height : "50"});
		$("#contact").animate({height : "300px"});
	})

	$("button").click(function(){
		$("button").toggleClass("clicked");
	})
})
