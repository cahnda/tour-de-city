from urllib2 import urlopen
from json import loads

API_URL = ("http://maps.googleapis.com/maps/api/directions/json?" 
          "origin=%s"
          "&waypoints=optimize:true|%s"
          "&destination=%s"
          "&sensor=false")

def get_waypoint_order(origin, waypoints, destination):
    query_url = API_URL % (origin, "|".join(waypoints), destination)
    print query_url
    response = urlopen(query_url)
    print "working so far"
    json_raw = response.read()
    json_data = loads(json_raw)
    return json_data
    # return json_data["routes"][0]["waypoint_order"]
