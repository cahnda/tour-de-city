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
def map(type, options={}):
	map_options = DEFAULT_OPTIONS
	map_options.update(options)
	return render_template('map.html', map_type=type, map_options=map_options)
