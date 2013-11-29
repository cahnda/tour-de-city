from urllib2 import urlopen
from json import loads

API_URL = ("http://maps.googleapis.com/maps/api/directions/json?" 
          "origin=%s"
          "&waypoints=optimize:true|%s"
          "&destination=%s"
          "&sensor=false")

def get_waypoint_order(origin, waypoints, destination):
	query_url = API_URL % (origin, "|".join(waypoints), destination)
	directions_json = loads(urlopen(query_url).read())
	return directions_json["routes"][0]["waypoint_order"]
