window.onload = function () {
    alert ("loaded");
    imgList = document.getElementsByClassName ("location-content");
    console.log (imgList.length);
for (var img in imgList)
	console.log (imgList);
	imgList.onclick = function () {
	    $.modal("this is a modal");
	};
    };
};
