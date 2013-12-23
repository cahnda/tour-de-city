proj3-6-SSSD
=================

# CUSTOM BIKE TOURS IN NYC

## Group Members
  * Victoria Greene
  * David Cahn
  * Severyn Kozak
  * Sweyn Venderbush

## Our Project
Our project will generate citi-bike tours to various landmarks and
points of interest in NYC. We'll over overlay the *Google Maps*, *Google
Places*, and *Citi Bike* APIs to highlight possible destinations, find the
nearest bike depots, and plot an optimal route between desired locations.

## Backend
Google Maps: Connect a set of given points using the shortest path. Display map.
Google Places: Find nearest landmarks, using user input for type (museum,
nightclub, etc). Order them by distance. Citibike: Given a location, find the
nearest citibike hub.

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
