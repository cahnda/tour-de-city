proj3-6-SSSD
=================

# CUSTOM BIKE TOURS IN NYC

## Group Members
  * Victoria Greene
  * David Cahn
  * Severyn Kozak
  * Sweyn Venderbush

## Our Project
Our project will generate tours of NYC and Boston. 

Tours will come in three forms:
1. Walking
2. Biking
3. Public transportation

We'll over overlay the *Google Maps*, *Google Places*, and *Citi Bike* APIs to highlight possible destinations, find the nearest bike depots, and plot an optimal route between desired locations. We will use the *FourSqaure* and *Yelp* APIs to prioritize locations based on user interest.

In addition to user-generated tours, we will allow users to select from pre-made tours of two-kinds:
1. Highest-rated by users (stored in mongo database)
2. Pre-designed by creators based on themes

##Hosted Version

[http://softdev-server.stuycs.org:6007](http://softdev-server.stuycs.org:6007)

##Installing

	sudo chmod +x install.sh

##Running

	./install.sh

On first run go to
[http://localhost:6007/updatedata](http://localhost:6007/updatedata) to pull the
necessary data.

## Dependencies

  * mongodb
  * gunicorn
  * pip
  * virtualenv
  * geopy
  * pymongo

## Limitation

Purchasing Google Maps API would allow us to create a tour of unlimited length.
With the free version, we can only connect a limited number of waypoints. For
this version of the app, users can only select a maximum of three stops for
their tour.
