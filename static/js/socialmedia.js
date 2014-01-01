function facebookClick(){
	var url = "http://www.facebook.com/sharer.php?" +
		"u=https://cstuy.org&t=trllest";
	popUpUrl(url);
}

function twitterClick(){
	var url = "https://twitter.com/intent/tweet?" +
		"url=http://www.cstuy.org&text=Check%20out%20CSTUY!&" +
		"hashtags=cstuy,";
	popUpUrl(url);
}

function googlePlusClick(){
	var url = "https://plus.google.com/share?url=http://cstuy.org";
	popUpUrl(url);
}

function tumblrClick(){
	var url = "http://www.tumblr.com/share?v=3&u=cstuy.org&t=CSTUY";
	popUpUrl(url);
}

function popUpUrl(url){
	window.open(url,'sharer','toolbar=0,status=0,width=626,height=436');
}
