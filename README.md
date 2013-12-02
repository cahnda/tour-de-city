proj2-pd6-07-SSSD
=================

### PROJECT SUMMARY: BUILD CUSTOM BIKE TOURS IN NYC

	 ______     ______     ______     _____
	/\  ___\   /\  ___\   /\  ___\   /\  __-.
	\ \___  \  \ \___  \  \ \___  \  \ \ \/\ \
	 \/\_____\  \/\_____\  \/\_____\  \ \____-
	  \/_____/   \/_____/   \/_____/   \/____/

# Group Members
  * Steve Zhu
  * David Cahn
  * Severyn Kozak
  * Sweyn Venderbush

# Our Project
Our project will generate citi-bike tours to various landmarks and
points of interest. We'll over overlay the *Google Maps*, *Google Places*, and
*Citi Bike* APIs to highlight possible destinations, find the nearest bike
depots, and plot an optimal route between desired locations.

# Backend
Google Maps: Connect a set of given points using the shortest path. Display map.
Google Places: Find nearest landmarks, using user input for type (museum, nightclub, etc). Order them by distance.
Citibike: Given a location, find the nearest citibike hub.

#Installing

    pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install geopy pymongo

#Running

    source env/bin/activate
    mongod
    gunicorn -w 4 -b 0.0.0.0:5007 -p pid app:app

On first run go to [http://localhost:5007/updatedata](http://localhost:5007/updatedata) to pull the necessary data.    

# Dependencies
geopy
pymongo

#Limitation

Purchasing Google Maps API would allow us to create a tour of unlimited length. With the free version, we can only connect a limited number of waypoints. For this version of the app, users can only select a maximum of three stops for their tour. 