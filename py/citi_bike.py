import json, utils
from urllib2 import urlopen

from geopy.distance import vincenty    # geodesic distance
from geopy.geocoders import GoogleV3

CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

def nearest_station_address(street):
	stations = utils.get_citi_bike_stations()
	street_coor = GoogleV3().geocode(street)[1]

	nearest_station = stations[0]
	station_coor = (nearest_station["latitude"], nearest_station["longitude"])
	shortest_dist = distance(street_coor, station_coor)

	for station in stations[1:]:
		station_coor = (station["latitude"], station["longitude"])
		dist = distance(street_coor, station_coor)
		if dist < shortest_dist:
			nearest_station = station
			shortest_dist = dist

	return nearest_station["address"]

def nearest_station_address_lon(lat, lon):
    stations = utils.get_citi_bike_stations()

    nearest_station = stations[0]
    shortest_dist = distance((nearest_station["latitude"], nearest_station["longitude"]), (lat, lon))

    for station in stations[1:]:
        dist = distance((station["latitude"], station["longitude"]), (lat, lon))
        if dist < shortest_dist:
            nearest_station = station
            shortest_dist = dist

    return nearest_station["address"]

def distance(coor1, coor2):
	return vincenty(coor1, coor2).miles

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


def make_location_array(startlat, startlon, endlat, endlon, waypoints):
	startbike = nearest_station_address_lon(startlat, startlon)
	endbike = nearest_station_address_lon(endlat, endlon)
	finalwaypoints = []
	finalwaypoints.append(startbike)
	for waypoint in waypoints:
		bikeloc = nearest_station_address(waypoint)
		finalwaypoints.append(bikeloc)
		finalwaypoints.append(waypoint)
		finalwaypoints.append(bikeloc)
	finalwaypoints.append(endbike)
	return finalwaypoints
