from flask import render_template

DEFAULT_OPTIONS = {
	'div': '#map-canvas',
	'zoom': 11,
	'lat': 40.7143528,
	'lng': -74.0059731,
	'streetViewControl': False,
	'disableDoubleClickZoom': True,
}

# type = default or directions
# options should be a dict
def map():
	map_options = DEFAULT_OPTIONS
	return render_template('map.html', map_options=map_options)
