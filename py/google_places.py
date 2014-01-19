import json
from urllib2 import urlopen

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE).
# POST  Generate an ordered list of places to visit based on their locations.

def findPlaces (latitude, longitude, responses):
    #make request
    AUTH_KEY = 'AIzaSyDnin5Fiq0aAjYFSEf7D1ae5V4O2yP-d_c'
    # LIST OF API KEYS:
    # cahnda@gmail.com : 'AIzaSyC-Rd4Mhjt7PPqMHGDjZdBJp3W835STm5w'
    # dcahn@guerrillajoe.com : 'AIzaSyDnin5Fiq0aAjYFSEf7D1ae5V4O2yP-d_c'
    # sweyn3@gmail.com : 'AIzaSyA6YYBVEWXWJHsynCDK78bhlhNCm1iQPDk'
    # st.zhu1@gmail.com: 'AIzaSyD2EsKFEM-O1SS9PUg6b91_08i4gBvOuRE'
    # dcahn@jsa.org: 'AIzaSyAu_MPXCDjBxDSfoqP0HG7W3e33keYx0Ww'
    LOCATION = str (latitude) + "," + str (longitude)
    RADIUS = 1000 #in meters, approx. .5 miles
    RANKBY = 'prominence'
    TYPES = ''

    # ADD USER INPUT FOR WHAT TYPE OF LOCATION THEY ARE LOOKING FOR
    if responses == []:
        TYPES = "amusement_park|aquarium|art_gallery|bowling_alley|cafe|"
        "city_hall|establishment|library|museum|night_club|park|restaurant|"
        "shopping_mall|store|stadium|store"
    else:
    	TYPES = '|'.join(responses)

    url = ("https://maps.googleapis.com/maps/api/place/search/json?types=%s"
           "&location=%s&radius=%s&sensor=false&rankby=%s&key=%s") % \
           (TYPES, LOCATION, RADIUS, RANKBY, AUTH_KEY)

    # Send the GET request to the Place details service (using url from above)
    response = urlopen(url)

    json_raw = response.read()
    json_data = json.loads(json_raw)

    results = []
    placeNum = 0
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            placeNum = placeNum + 1
            ans = []
            ans.append (place['name'].encode ('ascii', 'ignore'))
            ans.append (place['vicinity'].encode ('ascii', 'ignore'))
            try:
                ans.append (str(place['rating']))
            except:
                ans.append ('N/A')
            try:
                photo_info =  place ['photos'][0]
                photo_height = photo_info['height']
                photo_ref = photo_info['photo_reference']
                photo_width = photo_info['width']

                photo_url = ("https://maps.googleapis.com/maps/api/place/photo?"
                    "maxwidth=%s&photoreference=%s&sensor=true&key=%s") \
                    % (photo_width, photo_ref, AUTH_KEY)
                ans.append (photo_url)
            except:
                ans.append ('http://www.profyling.com/wp-content/uploads/2012/08/no-image-available.jpg')
            divStr = "myDiv" + str (placeNum)
            ans.append (divStr)
            descriptionText = "placeholder"
            ans.append (descriptionText)
            chkStr = "myChk" + str (placeNum)
            ans.append (chkStr)
            locStr = "myLoc" + str (placeNum)
            ans.append (locStr)

            results.append (ans)
           # s= '%s: %s Rating: %s' % (, place ['vicinity'], place['rating'])
           # s = s.encode ('ascii',"ignore")
           # results.append (s)

            #topic_id = place ['id']
            topic_id = "/m/0d6lp"
            url = "https://www.googleapis.com/freebase/v1/topic" + topic_id + '?' + 'filter=suggest&key=%s' %(AUTH_KEY)
            print url
           # topic = json.loads(urlopen(url).read())
        return results

if __name__ == '__main__':
    findPlaces (40.7472569628042, -73.99085998535156, [])
