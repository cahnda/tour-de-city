import json, utils
from urllib2 import urlopen

CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

def nearest_station_address(lat, lon):
	stations = utils.citi_bike_stations()

	nearest_station = stations[0]
	shortest_dist = distance(nearest_station["lat"], nearest_station["lon"], lat, lon)

	for station in stations[1:]:
		dist = distance(station["lat"], station["lon"], lat, lon)
		if dist < shortest_dist:
			nearest_station = station
			shortest_dist = dist

	return nearest_station["address"]

def station_addresses():
	citi_stations = get_json()["stationBeanList"]
	return [{\
		"address": station["stationName"],\
		"longitude": station["longitude"],\
		"latitude": station["latitude"]\
	} for station in citi_stations]

def get_json():
	citi_url = urlopen(CITI_BIKE_JSON_URL)
	return json.loads(citi_url.read())
