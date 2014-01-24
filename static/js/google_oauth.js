$("#gSignInWrapper").click(function() {
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
				$.ajax({
					type : "POST",
					url : "/googleoauth",
					data : JSON.stringify(resp, null, '\t'),
					contentType : "application/json;charset=UTF-8",
					success : function(result) {
						console.log(result);
					},
					error : function(){
						console.log("Failure");
					}
				})

				var googleUserPanel = document.createElement("div");
				googleUserPanel.id = "gUserPanel";
				var userImage = document.createElement("img");
				userImage.src = resp["image"]["url"];
				googleUserPanel.appendChild(userImage);
				$("#gSignInWrapper").replaceWith(googleUserPanel);

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
