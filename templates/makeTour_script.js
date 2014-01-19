totalChecked = 0;

window.onload = function () {
    $('.location input[type=checkbox]').change(function() {
	$(this).parent().toggleClass('active', this.checked);
    });

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
	    num = this.id.substring (5);
	    chkId = "myChk" + num;
	    
	    var titleImg  = this.getElementsByTagName('h2')[0].innerHTML;
	    var addressImg  = this.getElementsByTagName('p')[0].innerHTML;
	    var ratingImg  = this.getElementsByTagName('p')[0].innerHTML;
	    var chk = document.getElementById (chkId);
	    
	    document.getElementById("dialog").innerHTML = "";
	    var iDiv = document.getElementById("dialog");
	    var txtNd=document.createTextNode(imgTxt);
	    iDiv.appendChild(txtNd);

	    var imgpop = document.createElement("img");
	    imgpop.setAttribute("src", phyImg );
	    imgpop.setAttribute("height", "350");
	    imgpop.setAttribute("width", "350");

	    iDiv.appendChild(imgpop);

	    $("#dialog").dialog({
		modal:true, 
		title: titleImg,
		height: "auto",
		width: "auto",
		buttons: {
		    Select: function () {
			if (totalChecked < 3) {
			    chk.checked = true;
			    totalChecked = totalChecked + 1;
			    $(this).dialog('close');
			    $(this).parent().toggleClass('active');}
			else {
			    alert ("You Cannot Select this Location. You have already met the maximum of three stops.");}
		    },
			
		    Unselect: function () {
			chk.checked = false;
			totalChecked = totalChecked - 1;
			$(this).dialog('close');},

		    Close: function() {
			$( this ).dialog( "close" );
		    }}});
	};
    };
};
</script>
