import city_bikes, google_maps, google_places, google_directions

from geopy.distance import vincenty    # geodesic distance
from geopy.geocoders import GoogleV3
from urllib2 import urlopen
import pymongo, json

client = pymongo.MongoClient()
db = client.SSSD

bike_stations = db.newyork_bikes

def update_bike_stations(city_name):
	city_bike_stations = getBikeDatabase(city_name)
	city_bike_stations.remove()
	city_bike_stations.insert(city_bikes.city_bike_functions[city_name])

def setBikeDatabase(lat_str, lon_str):
	global bike_stations

	address = GoogleV3().reverse("%s, %s" % (lat_str, lon_str))[0][0].split(",")
	city_name = address[len(address) - 3].lower().replace(" ", "")
	bike_stations = getBikeDatabase(city_name)

def getBikeDatabase(city_name):
	if city_name == "newyork":
		return db.newyork_bikes

def get_bike_stations():
	return bike_stations.find()

def nearest_station_address(street):
    stations = get_bike_stations()
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
    stations = get_bike_stations()

    nearest_station = stations[0]
    shortest_dist = distance((nearest_station["latitude"], \
            nearest_station["longitude"]), (lat, lon))

    for station in stations[1:]:
        dist = distance((station["latitude"], station["longitude"]), (lat, lon))
        if dist < shortest_dist:
            nearest_station = station
            shortest_dist = dist

    return nearest_station["address"]

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

def distance(coor1, coor2):
    return vincenty(coor1, coor2).miles

def get_json(url):
    return json.loads(urlopen(url).read())
