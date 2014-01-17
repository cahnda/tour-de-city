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

	//$("textarea").focus(function(){
		//$(this)
	//})

	$("button").click(function(){
		$("button").toggleClass("clicked");
	})
})
