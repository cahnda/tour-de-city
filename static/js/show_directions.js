$(document).ready(function(){
	$("#rate-up, #rate-down").click(function(){
		var rate_json = {
			"rate_value" : this.value
		};
		$.ajax({
			type : "POST",
			url : "/tour=" + document.URL.split("tour=")[1],
			data : JSON.stringify(rate_json, null, '\t'),
			contentType : "application/json;charset=UTF-8",
		});
		$("#rate-up, #rate-down").fadeOut()
	})
})
