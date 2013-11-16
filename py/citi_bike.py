import json
from urllib2 import urlopen

CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

def get_json():
	citi_url = urlopen(CITI_BIKE_JSON_URL)
	citi_js = json.loads(citi_url.read())
