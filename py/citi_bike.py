import json
from urllib2 import urlopen

CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

def station_addresses():
	citi_stations = get_json()["stationBeanList"]
	return [{"address": station["stationName"]} for station in citi_stations]

def get_json():
	citi_url = urlopen(CITI_BIKE_JSON_URL)
	return json.loads(citi_url.read())
