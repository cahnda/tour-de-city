var locationPicker;
(function($) {
	// frame = dom object
	locationPicker = function(frame) {
		var frameWindow = frame.contentWindow,
			GMaps = frameWindow.GMaps,
			map = frameWindow.map;
		var marker = map.addMarker({
			title: 'Current Location',
			lat: 40.7143528,
			lng: -74.0059731,
			draggable: true
		});

		function performSearch(loc) {
			GMaps.geocode({
				address: loc,
				callback: function(results, status) {
					if (status == 'OK') {
						marker.setPosition(results[0].geometry.location);
						map.panTo(results[0].geometry.location);
					}
				}
			});
		}

		map.addListener('dblclick', function(event) {
			marker.setPosition(event.latLng);
		});
		marker.addListener('dragend', function(event) {
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
