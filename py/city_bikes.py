import utils

def get_newyork_bikes():
	CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

	citi_stations = get_json(CITI_BIKE_JSON_URL)["stationBeanList"]
	return [{\
		"address": station["stationName"],\
		"longitude": station["longitude"],\
		"latitude": station["latitude"]\
	} for station in citi_stations]

city_bike_functions = {
	"newyork" : get_newyork_bikes
}
