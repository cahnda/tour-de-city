var locationPicker;
(function($) {
	// frame = dom object
	locationPicker = function(frame) {
		var $wrapper = $(frame).parent(),
			$search = $wrapper.find('.search-form'),
			$text = $wrapper.find('.search-text'),
			$submit = $wrapper.find('.search-button'),
			$latitude = $wrapper.find('input[name=latitude]'),
			$longitude = $wrapper.find('input[name=longitude]');

		var frameWindow = frame.contentWindow,
			GMaps = frameWindow.GMaps,
			map = frameWindow.map,
			marker = map.addMarker({
			title: 'Current Location',
			lat: $latitude.val(),
			lng: $longitude.val(),
			draggable: true
		});

		function updateLocation(loc) {
			marker.setPosition(loc);
			$latitude.val(loc.lat());
			$longitude.val(loc.lng());
		}

		function performSearch(loc) {
			GMaps.geocode({
				address: loc,
				callback: function(results, status) {
					if (status == 'OK') {
						updateLocation(results[0].geometry.location);
						map.panTo(results[0].geometry.location);
					}
				}
			});
		}

		map.addListener('dblclick', function(event) {
			updateLocation(event.latLng);
		});
		marker.addListener('dragend', function(event) {
			updateLocation(event.latLng);
		});


		function submitSearch() {
			var loc = $text.val();
			performSearch(loc);
		}

		$submit.click(submitSearch);
		$text.keypress(function(e) {
			if(e.which == 13) {
				submitSearch();
				return false;
			}
			return true;
		});
	}
}(jQuery));
