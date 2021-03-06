import requests
import json
from urllib2 import urlopen

import datetime

# PRE: Take a list of "types of places"(i.e. musuem, nightclub) and current location (LONGITUDE and LATITUDE).
# POST  Generate an ordered list of places to visit based on their locations.

def findPlaces (latitude, longitude, responses):
    #make request
    AUTH_KEY = 'AIzaSyChW4Dkv_Ua8CXq6zy1sRRha2tRW7FYzlM'
    # LIST OF API KEYS:
    print AUTH_KEY

    # cahnda@gmail.com : 'AIzaSyC-Rd4Mhjt7PPqMHGDjZdBJp3W835STm5w'
    # dcahn@guerrillajoe.com : 'AIzaSyDnin5Fiq0aAjYFSEf7D1ae5V4O2yP-d_c'
    # sweyn3@gmail.com : 'AIzaSyA6YYBVEWXWJHsynCDK78bhlhNCm1iQPDk'
    # st.zhu1@gmail.com: 'AIzaSyD2EsKFEM-O1SS9PUg6b91_08i4gBvOuRE'
    # dcahn@jsa.org: 'AIzaSyAu_MPXCDjBxDSfoqP0HG7W3e33keYx0Ww'
    # stuyvesantspectator@gmail.com: 'AIzaSyBtT5oFCm_LRdN1IvkROlLeoFRGdyNcfpU'
    # dcahn@northeastjsa.org: 'AIzaSyAOz86LAqTs5HwgH6Ib2e3AIkNLaoVelSo'
    # spectatoredits@gmail.com: 'AIzaSyBJ2GpKgNV-tufVV__SC5x6vV3L74ZCTCg'
    # futureofisraelconference@gmail.com:'AIzaSyChW4Dkv_Ua8CXq6zy1sRRha2tRW7FYzlM'

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
    print json_data

    results = []
    placeNum = 0

    photoTime = 0
    yelpTime = 0

    if json_data['status'] == 'OK':
        print "a"
        for place in json_data['results']:
            placeNum = placeNum + 1
            ans = []
            placeName = place['name'].encode ('ascii', 'ignore')
            ref =  place['reference']
            lat = place ["geometry"]["location"]["lat"]
            lng  = place ["geometry"]["location"]["lng"]

            ans.append (placeName)
            ans.append (place['vicinity'].encode ('ascii', 'ignore'))
            try:
                ans.append (str(place['rating']))
            except:
                ans.append (0)
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
                ans.append ("/static/images/no_photo_available.jpg")

            divStr = "myDiv" + str (placeNum)
            ans.append (divStr)
            try:
                openNow = place ["opening_hours"]["open_now"];
                if openNow:
                    ans.append ("This venue is currently open")
                else:
                    ans.append ("This venue is currently closed")
            except:
                    ans.append ("No data available on opening hours")

            chkStr = "myChk" + str (placeNum)
            ans.append (chkStr)
            locStr = "myLoc" + str (placeNum)
            ans.append (locStr)

           # s= '%s: %s Rating: %s' % (, place ['vicinity'], place['rating'])
           # s = s.encode ('ascii',"ignore")
           # results.append (s)
           # topic_id = "/en/" + placeName
            #url = "https://www.googleapis.com/freebase/v1/topic" + topic_id + '?' + 'filter=suggest&key=%s' %(AUTH_KEY)
            #query = placeName
            #service_url = 'https://www.googleapis.com/freebase/v1/search'
            #params = {
               #'query': query,
             #  'key': AUTH_KEY,
             #  'indent':'true',
              # 'type': 'location/geocode/' + latStr,
           #}
            #url = service_url + '?' + urlencode(params)
           # topic = json.loads(urlopen(url).read())

            #start = datetime.datetime.now()
            url = "https://maps.googleapis.com/maps/api/place/details/json?reference=%s&sensor=false&&key=%s" %(ref, AUTH_KEY)
            #print "Google API call: %s" % url
            #print "now"
          #  print url
            response = urlopen(url)
            json_raw = response.read()
            json_data = json.loads(json_raw)
                        
           # print json_data
           # print "hello"

            if json_data['status'] == 'OK':
                result = json_data ['result']
                try:
                    phoneNum = result['formatted_phone_number']
                    ans.append (phoneNum)
                except:
                    ans.append ("No phone number listed")

                try:
                    ans.append (result["website"])
                except:
                    ans.append ('No website listed')
                try:
                    #reviews = result["reviews"]
                    #for review in reviews:
                       # if len(review["text"]) > 100:
                       #     review["text"] = (review["text"][:100], review["text"][100:])
                            ans.append (result ['reviews'])
                except:
                    ans.append ("No reviews available")

            #end = datetime.datetime.now()
            #photoTime += (end - start).microseconds

            #start = datetime.datetime.now()
            #YELP API INTEGRATION
            #url = "http://api.yelp.com/business_review_search?term=%s&lat=%s&long=%s&radius=10&limit=1&ywsid=QpOpEuta4Y2gBa4QcDhx3w" % (placeName,lat, lng)
            #print "Yelp API call: %s" % url

            #try:
                #response = requests.get(url)
                #json_data = response.json()["businesses"][0]
                #ratingYELP = json_data ['avg_rating']
                #ratingImg = json_data ['rating_img_url_small']
                #reviews = json_data ['reviews']
                #ans.append (ratingYELP)
                #ans.append (ratingImg)
               ## if (len (reviews) > 1):
                ##    ArrayReviews = []
                 ##   for review in reviews:
                  ##      ArrayReviews.append(review['text_excerpt'])
                   ## ans[10] = ArrayReviews
            #except:
                #ans.append ("No yelp information")
                #ans.append ("No yelp information")

            #end = datetime.datetime.now()
            #yelpTime += (end - start).microseconds
            lat = str (lat)
            lng = str (lng)
            CLIENT_ID = "PROKVIKPGQ3VZ1S2LMVI0QIKPEUXYRT14XLHTOHF2XS4RQYK"
            CLIENT_SECRET = "B1GJXBPPLOGTT53OK4RNC3UZ3XK0A11GUPA3EECEUVSFDJRJ"
            DATEVERIFIED = "20140301"

            url = "https://api.foursquare.com/v2/venues/search?query=%s&ll=%s,%s&intent=match&client_id=%s&client_secret=%s&v=%s" % (placeName, lat, lng, CLIENT_ID, CLIENT_SECRET,DATEVERIFIED)

            response = requests.get(url)
            json_data = response.json()["response"]["venues"]
            print json_data
            myCheckIns = myHere = 0

            if len(json_data) > 0:
                myVenue =  json_data [0]
                print "UNIQUE"
                for venue in json_data:
                    if venue["name"] == placeName:
                        myVenue = venue
                myHere = myVenue ["hereNow"]["count"]
                myStats =  myVenue ['stats']
                myCheckIns =  myStats ["checkinsCount"]

            ans.append (myCheckIns)
            ans.append (myHere)
            results.append (ans)
        results = sorted(results, key=lambda ans: ans[2], reverse = True)
        for ans in results:
            if ans[2] == 0:
                ans[2] = "N/A"

        #print "yelptime: %d" % yelpTime
        #print "phototime: %d" % photoTime
        return results

if __name__ == '__main__':
    print findPlaces (40.720842536130434, -73.99730066093753, [])
