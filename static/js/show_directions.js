var map, directionsDisplay, google, directionsService;

function calcRoute() {
    var start = "{{result['start']}}";
    var end = "{{result['end']}}";
    var waypts = JSON.parse({{result['waypoints']|tojson|safe}});
    console.log(start);
    console.log(end);
    console.log(waypts);
    var request = {
        origin: start,
        destination: end,
        travelMode: google.maps.TravelMode.{{result['transportation']}},
        waypoints: waypts
    };
    directionsService.route(request, function(response, status) {
        console.log(status)
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}

$(window).load(function() {
    //Other
    $("#final_map").hide();

    //Google Maps
    var fwindow = $('iframe')[0].contentWindow;
    var fdocument = fwindow.document
    google = fwindow.google;
    map = fwindow.map.map;

    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(fdocument.getElementById('directions-panel'));
    calcRoute();
});
