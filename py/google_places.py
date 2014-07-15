import requests
import json
from urllib2 import urlopen

import datetime

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE).
# POST  Generate an ordered list of places to visit based on their locations.

def findPlaces (latitude, longitude, responses):
    
    auth_key = 'AIzaSyChW4Dkv_Ua8CXq6zy1sRRha2tRW7FYzlM'
    # LIST OF API KEYS:
    # cahnda@gmail.com : 'AIzaSyC-Rd4Mhjt7PPqMHGDjZdBJp3W835STm5w'
    # dcahn@guerrillajoe.com : 'AIzaSyDnin5Fiq0aAjYFSEf7D1ae5V4O2yP-d_c'
    # sweyn3@gmail.com : 'AIzaSyA6YYBVEWXWJHsynCDK78bhlhNCm1iQPDk'
    # st.zhu1@gmail.com: 'AIzaSyD2EsKFEM-O1SS9PUg6b91_08i4gBvOuRE'
    # dcahn@jsa.org: 'AIzaSyAu_MPXCDjBxDSfoqP0HG7W3e33keYx0Ww'
    # stuyvesantspectator@gmail.com: 'AIzaSyBtT5oFCm_LRdN1IvkROlLeoFRGdyNcfpU'
    # dcahn@northeastjsa.org: 'AIzaSyAOz86LAqTs5HwgH6Ib2e3AIkNLaoVelSo'
    # spectatoredits@gmail.com: 'AIzaSyBJ2GpKgNV-tufVV__SC5x6vV3L74ZCTCg'
    # futureofisraelconference@gmail.com:'AIzaSyChW4Dkv_Ua8CXq6zy1sRRha2tRW7FYzlM'

    # Construct request for Google Places API
    url = constructGooglePlacesURL(latitude, longitude, responses, auth_key)

    # Send the GET request to the places service (using url from above)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)

    
    # Initialize results
    ans_array = []
    placeCounter = 0

    photoTime = 0
    yelpTime = 0

    if json_data['status'] != 'OK':
        # Log error
        return []

    try:
        results = json_data['results']
    except:
        # Log error
        return []

    for place in results:
        if "reference" not in place:
            continue

        placeCounter += 1

        # Initialize individual result
        ans = {}
        ans["counter"] = str(placeCounter)

        placeName = place['name'].encode ('ascii', 'ignore')
        ans["name"] = placeName

        try:
            ans['rating'] = float(place['rating'])
        except:
            ans['rating'] = 0.0
        try:
            openNow = place["opening_hours"]["open_now"];
            if openNow:
                ans["open_now"] = "This venue is currently open"
            else:
                ans["open_now"] = "This venue is currently closed"
        except:
                ans["open_now"] = "No data available on opening hours"

        # Construct request for Google Details API
        ref = place["reference"]
        url = "https://maps.googleapis.com/maps/api/place/details/json?reference=%s&sensor=false&&key=%s" % (ref, auth_key)

        # Send the GET request to the details service (using url from above)
        response = urlopen(url)
        json_raw = response.read()
        json_data = json.loads(json_raw)

        # Photos info is critical
        if json_data['status'] == 'OK':
            place_details = json_data ['result']

            # Get Photo URL
            try:
                photo_info =  place_details['photos'][0]
                photo_height = photo_info['height']
                photo_ref = photo_info['photo_reference']
                photo_width = photo_info['width']

                photo_url = ("https://maps.googleapis.com/maps/api/place/photo?"
                    "maxwidth=%s&photoreference=%s&sensor=true&key=%s") \
                    % (photo_width, photo_ref, auth_key)

                ans["photo_url"] = photo_url
            except:
                # Log error
                ans["photo_url"] = "/static/images/no_photo_available.jpg"

            # Get Phone Number
            try:
                phoneNum = place_details['formatted_phone_number']
                ans["phone_number"] = phoneNum
            except:
                ans["phone_number"] = "No phone number listed"

            # Get Website
            try:
                ans["website"] = place_details["website"]
            except:
                ans["website"] = 'No website listed'

            # Get Reviews
            try:
                ans["reviews"] = place_details["reviews"]
            except:
                ans["reviews"] = "No reviews available"

            # Get Address
            try:
                address = place_details['vicinity'].encode ('ascii', 'ignore')
                ans["address"] = address
            except:
                ans["address"] = "No Address Listed"
        else:
            # Log error
            ans["photo_url"]    = "/static/images/no_photo_available.jpg"
            ans["phone_number"] = "No phone number listed"
            ans["website"]      = 'No website listed'
            ans["reviews"]      = "No reviews available"


        lat = place ["geometry"]["location"]["lat"]
        lng = place ["geometry"]["location"]["lng"]

        lat = str (lat)
        lng = str (lng)

        FOURSQUARE_CLIENT_ID = "PROKVIKPGQ3VZ1S2LMVI0QIKPEUXYRT14XLHTOHF2XS4RQYK"
        FOURSQUARE_CLIENT_SECRET = "B1GJXBPPLOGTT53OK4RNC3UZ3XK0A11GUPA3EECEUVSFDJRJ"
        DATEVERIFIED = "20140301"

        url = "https://api.foursquare.com/v2/venues/search?query=%s&ll=%s,%s&intent=match&client_id=%s&client_secret=%s&v=%s" % (placeName, lat, lng, FOURSQUARE_CLIENT_ID, FOURSQUARE_CLIENT_SECRET, DATEVERIFIED)

        response = requests.get(url)
        try:
            json_data = response.json()["response"]["venues"]
        except:
            json_data = []

        myCheckIns = 0
        myHere     = 0

        if len(json_data) > 0:
            myVenue =  json_data [0]
            for venue in json_data:
                if venue["name"] == placeName:
                    myVenue = venue
            myHere = myVenue ["hereNow"]["count"]
            myStats =  myVenue ['stats']
            myCheckIns =  myStats ["checkinsCount"]

        ans["checkins"] = myCheckIns
        ans["here"] = myHere

        ans_array.append (ans)

    print json.dumps(results)
    ans_array = sorted(ans_array, key=lambda ans: ans["rating"], reverse = True)
    for ans in ans_array:
        if ans["rating"] == 0:
            ans["rating"] = "N/A"

    return ans_array

def constructGooglePlacesURL(latitude, longitude, responses, auth_key):
    location = str (latitude) + "," + str (longitude)
    radius = 1000 #in meters, approx. .5 miles
    rankby = 'prominence'
    types = ''

    if responses == []:
        types = "amusement_park|aquarium|art_gallery|bowling_alley|cafe|"
        "city_hall|establishment|library|museum|night_club|park|restaurant|"
        "shopping_mall|store|stadium|store"
    else:
        types = '|'.join(responses)

    url = ("https://maps.googleapis.com/maps/api/place/search/json?types=%s"
           "&location=%s&radius=%s&sensor=false&rankby=%s&key=%s") % \
           (types, location, radius, rankby, auth_key)
    return url

if __name__ == '__main__':
    print findPlaces (40.720842536130434, -73.99730066093753, [])
