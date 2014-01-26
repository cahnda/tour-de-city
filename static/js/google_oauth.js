/*
 *	Handles Google oauth login, and stores user information in Flask client.
*/

$("#gSignInContainer").click(function() {
	var opts = {
		lines: 15, // The number of lines to draw
		length: 9, // The length of each line
		width: 2, // The line thickness
		radius: 10, // The radius of the inner circle
		corners: 1, // Corner roundness (0..1)
		rotate: 0, // The rotation offset
		direction: 1, // 1: clockwise, -1: counterclockwise
		color: '#fff', // #rgb or #rrggbb or array of colors
		speed: 1.0, // Rounds per second
		trail: 60, // Afterglow percentage
		shadow: false, // Whether to render a shadow
		hwaccel: false, // Whether to use hardware acceleration
		className: 'spinner', // The CSS class to assign to the spinner
		zIndex: 2e9, // The z-index (defaults to 2000000000)
		top: 'auto', // Top position relative to parent in px
		left: 'auto' // Left position relative to parent in px
	};
	window.spinner = new Spinner(opts).spin();
	$(this).find("#gSignInWrapper").hide();
	$(this).append(spinner.el);

	var po = document.createElement('script');
	po.type = 'text/javascript'; po.async = true;
	po.src = 'https://apis.google.com/js/client:plusone.js?onload=render';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(po, s);
});

function render() {
	gapi.signin.render('customBtn', {
		'callback': 'signinCallback',
		'clientid': '611512958800-p6uidtj1frllpcvv8jo6gnc9f2lmn431.apps.googleusercontent.com',
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
				googleUserPanel.appendChild(userImage);

				googleUserPanel.innerHTML += "\
					<div id='profile'>\
						<a href='/profile'>profile</a>\
					</div>\
					<div id='logout'>\
						<a href='/logout'><img src='static/images/logout.png'></a>"

				googleUserPanel.style.top = "-50px";
				$("body").prepend(googleUserPanel);

				window.spinner.stop();
				// add gUserPanel
				$("#gSignInContainer").animate({"top" : "-50px"}, 270, function(){
					$("#gUserPanel").animate({"top" : "0px"}, 270);
				});

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
