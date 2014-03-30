var page_url = "http://tour-de-city.com";

function facebookClick(){
	var url = "http://www.facebook.com/sharer.php?" +
		"u=" + page_url + "&t=Bike%20tours!";
	popUpUrl(url);
}

function twitterClick(){
	var url = "https://twitter.com/intent/tweet?url=" + page_url +
		"&text=Check%20out%20tours!&hashtags=Tours!,";
	popUpUrl(url);
}

function googlePlusClick(){
	var url = "https://plus.google.com/share?url=" + page_url;
	popUpUrl(url);
}

function tumblrClick(){
	var url = "http://www.tumblr.com/share?v=3&u=" + page_url +
		"&t=Bike%20tours!";
	popUpUrl(url);
}

function popUpUrl(url){
	window.open(url,'sharer','toolbar=0,status=0,width=626,height=436');
}
