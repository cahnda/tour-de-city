totalChecked = 0;

$(document).ready(function(){
	//$('.location input[type=checkbox]').change(function() {
		//$(this).parent().toggleClass('active', this.checked);
	//});
	//var max = 3;
	//var $checkboxes = $('.locations-form input[type=checkbox]');
	//$checkboxes.change(function(){
		//var current = $checkboxes.filter(':checked').length;
		//$checkboxes.filter(':not(:checked)').prop('disabled', current >= max);
	//});
	$(".location-container").click(function(){
		var widthInfoDiv = document.querySelector("div.main-content.content").offsetWidth;
		$(this).css({"width" : widthInfoDiv + "px"});
	})
});

window.onload = function () {
	//allCBox = document.getElementsByClassName ("chkbox");
	//for (i=0; i < allCBox.length; i++) {
		//allCBox[i].disabled = true;
	//};

	for (var n=1;n<=numLocs;n++) {
		strIt = n.toString();
		divName = "myDiv" + strIt
		var imgSc = document.getElementById(divName);

		imgSc.onclick = function () {

			//var source = this.getElementsByTagName('img')[0];
			//var phyImg = source.src;
			num = this.id.substring (5);
			chkId = "myChk" + num;
			locId = "myLoc" + num;

			loc = locs
			var openingHours = loc[num-1][5];
			var telephoneNum = loc[num-1][8];
			var website = loc[num-1][9];
			var reviews = loc[num-1][10];
			var YelpRating = loc[num-1][11];
			var YelpRatingImg = loc[num-1][12];

			if (reviews === "No reviews available")
				myReview = reviews;
			else {
				myReview = [];
				for (var i = 0; i < 3; i++) {
					if (typeof reviews[i] != "undefined"){
						var txt = reviews[i]["text"];
						var txt = txt.replace("&#39;","'");
						myReview.push(txt);
					}
				}
			}

			var titleImg  = this.getElementsByTagName('h2')[0].innerHTML;
			var addressImg  = this.getElementsByTagName('p')[0].innerHTML;
			var ratingImg  = this.getElementsByTagName('p')[1].innerHTML;
			chk = document.getElementById (chkId);
			loc = document.getElementById (locId);


            console.log ("AM I CHECKED?");
            console.log (chk.checked);

            document.getElementById("dialog").innerHTML = "";
            var iDiv = document.getElementById("dialog");
            column1 = document.createElement("tr")
            column2 = document.createElement("tr")


            var titleName = "Name: ";
            var addressName = "Address: ";
            var ratingName = "Google Places ";
            var ratingNameYELP = "Average Yelp Rating: ";

            var titleNd=document.createTextNode(titleImg);
            var addressNd=document.createTextNode(addressImg);
            var ratingNd=document.createTextNode(ratingImg);
            var ratingNdYelp = document.createTextNode(YelpRating);

            column1.appendChild (titleNd);
            column1.appendChild(document.createElement("br"));
            column1.appendChild (addressNd);
            column1.appendChild(document.createElement("br"));
            var txtNd=document.createTextNode(telephoneNum);
            column1.appendChild(txtNd);

            column1.appendChild(document.createElement("br"));
            var txtNd=document.createTextNode(website);
            console.log (website);
            column1.appendChild(txtNd);

            column1.appendChild(document.createElement("br"));
            var txtNd=document.createTextNode(openingHours);
            column1.appendChild(txtNd);

            column1.appendChild(document.createElement("br"));
            var txtNd=document.createTextNode(ratingName);
            column1.appendChild (txtNd);
            column1.appendChild (ratingNd);

            column1.appendChild(document.createElement("br"));
            var txtNd=document.createTextNode(ratingNameYELP);
            column1.appendChild (txtNd);
            column1.appendChild (ratingNdYelp);

            column1.appendChild(document.createElement("br"));
            var imgpop = document.createElement("img");
            imgpop.setAttribute("src", YelpRatingImg );
            imgpop.setAttribute("height", "40");
            imgpop.setAttribute("width", "150");

            column1.appendChild(imgpop);
            column1.appendChild(document.createElement("br"));
            column1.appendChild(document.createElement("br"));
            column1.appendChild(document.createElement("br"));

            var txtNd=document.createTextNode("REVIEWS:");
            column1.appendChild(txtNd);

            if (myReview === "No reviews available"){

                var txtNd=document.createTextNode(myReview);
                column1.appendChild(txtNd);
                console.log ("no review");
            }

            else {
                for (var i = 1; i <= myReview.length; i++) {
                    column1.appendChild(document.createElement("br"));
                    column1.appendChild(document.createElement("br"));
                    var txtNd=document.createTextNode(i.toString () + ". ");
                    var reviewNd=document.createTextNode(myReview[i-1]);
                    column1.appendChild(txtNd);
                    column1.appendChild(reviewNd);
                }}

            //var imgpop = document.createElement("img");
            //imgpop.setAttribute("src", phyImg );
            //imgpop.setAttribute("height", "350");
            //imgpop.setAttribute("width", "350");

            column2.appendChild(document.createElement("br"));
            //column2.appendChild(imgpop);
            iDiv.appendChild (column1);
            iDiv.appendChild (column2);

        };
    };
};
