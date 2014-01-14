<script>

window.onload = function () {
    alert ("loaded");
    for (var i=1;i<={{locLen}};i++) {
	strIt = i.toString();
	divName = "myDiv" + strIt
	img = document.getElementById(divName);
	var iDiv = document.createElement('div');
	iDiv.setAttribute("id", divName + "pop");
	descriptionText = {{locs[i][4]}}
	var txtNd=document.createTextNode(descriptionText);
	var imgpop = document.createElement("img");
	imgpop.setAttribute("src", "images/hydrangeas.jpg");
	imgpop.setAttribute("height", "768");
	imgpop.setAttribute("width", "1024");

	img.onclick = function () {
	    $("#dialog").dialog({
		modal:true, 
		buttons: {
		    Ok: function() {
			$(  this ).dialog( "close" );
		    }}});
	};
    };
};

</script>
