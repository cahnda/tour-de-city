$(document).ready(function(){
	$("#gUserPanel #profile_image").click(function(){
		$("#gUserPanel").toggleClass("profile_clicked");
		$("#profile_panel").removeClass("visible");
	});

	$("#menu_button").click(function(){
		$("#profile_panel").toggleClass("visible");
	})
})
