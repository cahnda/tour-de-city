var locationPicker;
(function($) {
	// frame = dom object
	locationPicker = function(frame) {
		var frameWindow = frame.contentWindow;
		var google, map, geocoder, marker;
		google = frameWindow.google;
		map = frameWindow.map;
		geocoder = new google.maps.Geocoder();
		marker = new google.maps.Marker({
			position: new google.maps.LatLng(40.7143528, -74.0059731),
			map: map,
			draggable: true
		});

		function performSearch(loc) {
			geocoder.geocode({"address": loc},
				function(results, status) {
					if (status == google.maps.GeocoderStatus.OK) {
						marker.setPosition(results[0].geometry.location);
						map.panTo(results[0].geometry.location);
					}
				}
			);
		}

		google.maps.event.addListener(map, 'dblclick', function(event) {
			marker.setPosition(event.latLng);
		});
		google.maps.event.addListener(marker, 'dragend', function(event) {
			marker.setPosition(marker.position);
		});

		var $wrapper = $(frame).parent(),
			$search = $wrapper.find('.search-form'),
			$text = $search.find('.search-text');

		$search.submit(function() {
			var loc = $text.val();
			performSearch(loc);
			return false;
		});
	}
}(jQuery));
