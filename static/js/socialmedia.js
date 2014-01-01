function facebookClick(){
	var url = "http://www.facebook.com/sharer.php?" +
		"u=https://softdev-server.stuycs.org:6007&t=Bike%20tours!";
	popUpUrl(url);
}

function twitterClick(){
	var url = "https://twitter.com/intent/tweet?" +
		"url=http://softdev-server.stuycs.org:6007&text=Check%20out%20tours!&" +
		"hashtags=Tours!,";
	popUpUrl(url);
}

function googlePlusClick(){
	var url = "https://plus.google.com/share?url=http://softdev-server.stuycs.org:6007";
	popUpUrl(url);
}

function tumblrClick(){
	var url = "http://www.tumblr.com/share?v=3&u=softdev-server.stuycs.org:6007&t=Bike%20tours!";
	popUpUrl(url);
}

function popUpUrl(url){
	window.open(url,'sharer','toolbar=0,status=0,width=626,height=436');
}
