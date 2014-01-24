window.onload = function () {
    alert ("loaded");
    imgList = document.getElementById ("locationNum");
    console.log (imgList.length);
    console.log (imgList);
    imgList.onclick = function () {
	$.modal("this is a modal");
    };
};
