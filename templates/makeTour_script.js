
window.onload = function () {
    alert ("loaded");
    document.getElementById("dialog").innerHTML = "";

    for (var i=1;i<={{locLen}};i++) {
	strIt = i.toString();
	divName = "myDiv" + strIt
        var loc = JSON.parse('{{locs | tojson | safe}}');
	imgTxt = loc[i-1][5];
	phyImg = loc[i-1][3];

	var imgSc = document.getElementById(divName);
	imgSc.onclick = function () {
	    var source = this.getElementsByTagName('img')[0];
	    var phyImg = source.src;

	    console.log (source);
	    document.getElementById("dialog").innerHTML = "";
	    var iDiv = document.getElementById("dialog");
	    var txtNd=document.createTextNode(imgTxt);
	    iDiv.appendChild(txtNd);

	    var imgpop = document.createElement("img");
	    imgpop.setAttribute("src", phyImg );
	    imgpop.setAttribute("height", "500");
	    imgpop.setAttribute("width", "500");

	    iDiv.appendChild(imgpop);

	    $("#dialog").dialog({
		modal:true, 
		title: 
		height: "auto",
		width: "auto",
		buttons: {
		    Ok: function() {
			$( this ).dialog( "close" );
		    }}});
	};
    };
};
