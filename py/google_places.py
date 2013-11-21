<<<<<<< HEAD
import json
from urllib2 import urlopen

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE). 
# POST  Generate an ordered list of places to visit based on their locations. 

def findPlaces (latitude, longitude, responses):
    #make request
    AUTH_KEY = 'AIzaSyC-Rd4Mhjt7PPqMHGDjZdBJp3W835STm5w'
    LOCATION = str (latitude) + "," + str (longitude)
    RADIUS = 3500 #in meters, approx. 2 miles
    RANKBY = 'prominence'
    #KEYWORDS = 'tourism+monument'
    TYPES = ''

    # ADD USER INPUT FOR WHAT TYPE OF LOCATION THEY ARE LOOKING FOR
    if responses == []:
        TYPES = 'amusement_park|aquarium|art_gallery|bowling_alley|cafe|city_hall|establishment|library|museum|night_club|park|restaurant|shopping_mall|store|stadium|store'
    else:
        for word in responses:
            TYPES = TYPES + str (word) + '|'
        TYPES = TYPES [:-1]       
            
    url = ('https://maps.googleapis.com/maps/api/place/search/json'
           '?types=%s&location=%s&radius=%s&sensor=false&rankby=%s&key=%s') %  (TYPES, LOCATION, RADIUS, RANKBY, AUTH_KEY)
   
    print url

    # Send the GET request to the Place details service (using url from above)
    response = urlopen(url)
     
    # Get the response and use the JSON library to decode the JSON
    json_raw = response.read()
    json_data = json.loads(json_raw)

    # Iterate through the results and print them to the console
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            print '\n %s: %s  \n Rating: %s' % (place['name'], place ['vicinity'], place['rating'])           

if __name__ == '__main__':
    findPlaces (40.7472569628042, -73.99085998535156, [])
=======
import json
from urllib2 import urlopen

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE). 
# POST  Generate an ordered list of places to visit based on their locations. 

def findPlaces (latitude, longitude, responses):
    #make request
    AUTH_KEY = 'AIzaSyC-Rd4Mhjt7PPqMHGDjZdBJp3W835STm5w'
    LOCATION = str (latitude) + "," + str (longitude)
    RADIUS = 3500 #in meters, approx. 2 miles
    RANKBY = 'prominence'
    KEYWORDS = 'tourism+monument'
    TYPES = ''

    # ADD USER INPUT FOR WHAT TYPE OF LOCATION THEY ARE LOOKING FOR
    if responses == []:
        TYPES = 'amusement_park|aquarium|art_gallery|bowling_alley|cafe|city_hall|establishment|library|museum|night_club|park|restaurant|shopping_mall|store|stadium|store'
    else:
        for word in responses:
            TYPES = TYPES + str (word) + '|'
        TYPES = TYPES [:-1]       
            
    url = ('https://maps.googleapis.com/maps/api/place/search/json'
           '?keyword=%s?types=%s&location=%s&radius=%s&sensor=false&rankby=%s&key=%s') %  (KEYWORDS, TYPES, LOCATION, RADIUS, RANKBY, AUTH_KEY)
   
    print url

    # Send the GET request to the Place details service (using url from above)
    response = urlopen(url)
     
    # Get the response and use the JSON library to decode the JSON
    json_raw = response.read()
    json_data = json.loads(json_raw)

    # Iterate through the results and print them to the console
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            print '\n %s: %s  \n Rating: %s' % (place['name'], place ['vicinity'], place['rating'])           

if __name__ == '__main__':
    findPlaces (40.7472569628042, -73.99085998535156, [])
>>>>>>> c19a291a4bd726084e5c1de284b12e01175a202b
