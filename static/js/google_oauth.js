/*
 *  Handles Google oauth login, and stores user information in Flask client.
*/

(function(){
	var po = document.createElement('script');
	po.type = 'text/javascript'; po.async = true;
	po.src = 'https://apis.google.com/js/client:plusone.js?onload=render';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(po, s);
})();

$("#gSignInContainer").click(function() {
	var opts = {
		lines: 15, length: 9, width: 2, radius: 10, corners: 1, rotate: 0,
		direction: 1, color: '#fff', speed: 2.2, trail: 70, shadow: false,
		hwaccel: false, className: 'spinner', zIndex: 2e9, top: 'auto',
		left: 'auto'
	};
	window.spinner = new Spinner(opts).spin();
	$(this).find("#gSignInWrapper").hide();
	$(this).append(spinner.el);

});

function render() {
	gapi.signin.render('customBtn', {
		'callback': 'signinCallback',
		"clientid" : "611512958800-d09hbf07sibk69it40fhd12ogup6sfk7.apps.googleusercontent.com",
		'cookiepolicy': 'single_host_origin',
		'scope': 'profile'
	});
}

function signinCallback(authResult) {
	if (authResult['status']['signed_in']) {
		gapi.client.load('plus','v1', function(){
			var request = gapi.client.plus.people.get({'userId': 'me'});
			request.execute(function(resp) {
				console.log(resp);

				// store person object in Flask session
				$.ajax({
					type : "POST",
					url : "/googleoauth",
					data : JSON.stringify(resp, null, '\t'),
					contentType : "application/json;charset=UTF-8",
				})

				// prepare gUserPanel, as per templates/layout.html
				var googleUserPanel = document.createElement("div");
				googleUserPanel.id = "gUserPanel";

				var userImage = document.createElement("img");
				userImage.src = resp["image"]["url"];

				googleUserPanel.innerHTML += ("\
					<img id='profile_image' src='" + resp["image"]["url"] +
					"'><div id='menu_button'>\
						<span>menu</span>\
					</div>\
					\
					<div id='profile_panel'>\
						<p>\
							\/\/" + resp["displayName"] + "\
						</p>\
						\
						<ul>\
							<li>\
								<a href='/profile'>@profile</a>\
							</li><br>\
							<li>\
								<a href='/logout'>@logout</a>\
							</li><br>\
						</ul>\
					</div>")

				googleUserPanel.style.top = "-50px";
				$("body").prepend(googleUserPanel);

				window.spinner.stop();
				// add gUserPanel
				$("#gSignInContainer").animate({"top" : "-50px"}, 270, function(){
					$("#gUserPanel").animate({"top" : "0px"}, 270);
				});

				$("#gUserPanel #profile_image").click(function(){
					$("#gUserPanel").toggleClass("profile_clicked");
					$("#profile_panel").removeClass("visible");
				});

				$("#menu_button").click(function(){
					$("#profile_panel").toggleClass("visible");
				})

			});
		});
	}
	else {
		// Update the app to reflect a signed out user
		// Possible error values:
		//	 "user_signed_out" - User is signed-out
		//	 "access_denied" - User denied access to your app
		//	 "immediate_failed" - Could not automatically log in the user

		console.log('Sign-in state: ' + authResult['error']);
	}
}
