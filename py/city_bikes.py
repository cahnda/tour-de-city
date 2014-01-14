import utils
from urllib2 import urlopen
import json, xml.etree.ElementTree as ElementTree

def get_newyork_bikes():
	CITI_BIKE_JSON_URL = "http://citibikenyc.com/stations/json"

	citi_stations = get_json(CITI_BIKE_JSON_URL)["stationBeanList"]
	return [bike_station_dict(
		station["stationName"],
		station["longitude"],
		station["latitude"])
		for station in citi_stations]


def get_boston_bikes():
	BOSTON_BIKE_XML_URL = "http://www.thehubway.com/data/stations/bikeStations.xml"

	bike_stations_xml = get_xml(BOSTON_BIKE_XML_URL)
	return [bike_station_dict(
		station.find("name").text[0],
		station.find("long").text,
		station.find("lat").text)
		for station in bike_stations_xml.iter("station")]

def bike_station_dict(address, longitude, latitude):
	return {\
		"address": address,\
		"longitude": longitude,\
		"latitude": latitude\
	}

city_bike_functions = {
	"newyork" : get_newyork_bikes,
	"boston" : get_boston_bikes
}

def get_json(url):
	return json.loads(urlopen(url).read())

def get_xml(url):
	return ElementTree.fromstring(urlopen(url).read())
