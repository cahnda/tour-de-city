window.onload = function () {
    alert ("loaded");
    imgList = document.getElementsByClassName  ("location-content");
    console.log (imgList.length);
    for img in imgList {
	console.log (imgList);
	imgList.onclick = function () {
	    $.modal("this is a modal");
	};
    };
};
