import json
from urllib2 import urlopen

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE). 
# POST  Generate an ordered list of places to visit based on their locations. 

def findPlaces (latitude, longitude, responses):
    #make request
    AUTH_KEY = 'AIzaSyBCHXuWpnzODuPRa4-CLTtC9JPyZWEFxPo'
    LOCATION = str (latitude) + "," + str (longitude)
    RADIUS = '3500' #in meters, approx. 2 miles
    RANKBY = 'prominence'
    KEYWORDS = 'tourism+monument'
    SENSOR = false
    TYPES = ''

    # ADD USER INPUT FOR WHAT TYPE OF LOCATION THEY ARE LOOKING FOR
    try: 
        for word in responses:
            TYPES = TYPES + str (word) + '|'
        TYPES = TYPES [:-1]
    except:         
        TYPES = 'amusement_park+aquarium+art_gallery+bowling_alley+cafe+city_hall+establishment+library+museum+night_club+park+restaurant+shopping_mall+store+stadium+store'
            
    url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
           '?keyword=%s?types=%s&radius=%s&sensor=false&key=%s') % (LOCATION, KEYWORDS, TYPES, RADIUS, AUTH_KEY)
    
    print url

    # Send the GET request to the Place details service (using url from above)
    response = urllib2.urlopen(url)
    
    # Get the response and use the JSON library to decode the JSON
    json_raw = response.read()
    json_data = json.loads(json_raw)

    # Iterate through the results and print them to the console
   # if json_data[‘status’] == ‘OK’:
    #    for place in json_data['results']:
     #       print ‘%s: %s\n’ % (place['name'], place['reference'])'
            
