from flask import render_template
import json

DEFAULT_OPTIONS = {
	'zoom': 8,
	'center': 'new google.maps.LatLng(-34.397, 150.644)'
}

# options should be a dict
def map(options):
	map_options = DEFAULT_OPTIONS
	map_options.update(options)
	return render_template('map.html',
		map_options=json.dumps(map_options))
