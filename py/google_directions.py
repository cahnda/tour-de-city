from urllib2 import urlopen
from json import loads
import copy

API_URL = "http://maps.googleapis.com/maps/api/directions/json?origin=%s&waypoints=optimize:true|%s&destination=%s&sensor=false"

def get_waypoint_order(origin, waypoints, destination):
    if len(waypoints) < 2:
        return waypoints
    else:
        formatWaypoints = waypoints[:]
        formatWaypoints = prepareFormat(formatWaypoints)
        print waypoints
        query_url = API_URL % (origin, "|".join(formatWaypoints), destination)
        print query_url
        response = urlopen(query_url)
        print "working so far"
        json_raw = response.read()
        json_data = loads(json_raw)
        order = json_data["routes"][0]["waypoint_order"]
        orderedWaypoints = []
        for num in order:
            orderedWaypoints.append(waypoints[num])
        return orderedWaypoints

def prepareFormat(waypoints):
    for x in range(0,len(waypoints)):
        waypoint = waypoints[x]
        l = list(waypoint)
        print l
        i = 0
        while i < len(l):
            print len(l)
            print i
            if l[i] == " ":
                if l[i-1] == ",":
                    l.pop(i)
                else:
                    l[i] = "+"
            i = i+1
        waypoints[x] = "".join(l)
    return waypoints
    
