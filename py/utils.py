import pymongo
import citi_bike, google_maps, google_places

client = pymongo.MongoClient()
db = client.SSSD

citi_bike_stations = db.citi_bike_stations

def update_citi_bike_stations():
	citi_bike_stations.remove()
	citi_bike_stations.insert(citi_bike.station_addresses())

def get_citi_bike_stations():
	return citi_bike_stations.find()
