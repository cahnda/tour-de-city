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

## The Plan

Deadlines:
Functioning website: January 17th-19th
More Styling + Fixing Stuff: 19-24th

Special features:
Themed/Random tour
Rate your tours [Victoria]
Login system (if we have time), Save historic tours [Severyn/Anyone]
Use javascript to keep everything on the same page (if we have time)
 
Page 1: Organization! [Severyn]
   * Select City → Set internal variable for user session. 
   * Working to create an organized way of integrating multiple cities.
   * Discuss with DC and VG about integrating with the rest of the website
   * "Select Premade Tour → Directs to Page 4
   * “Make Your Own Tour” → Directs to Page 2
   * MTA and Walking tours [Integration]
   * Geolocation (if we learn how to do this)

Page 2: [David] = API work
     * Theme? Random?
     * Pop-out box, with full description, check a box to select the location
     * Yelp + 4Square API to prioritize
     * Upcoming events/art show. Temporary cool stuff that might be worthwhile.
     * 20 locations max
     * Avoid clutter on the pages
 Page 3: [Sweyn] = Google maps
     * Simple end-page with full description of page
     * User-friendly organization of the tour data/locations = better way of presenting the final result. Really really important.
     * Finished with tour → Page 5
Page 4: [Victoria] = Database work + Javascript [Mongo]
     * Rate your tours [Victoria], the rated tours can have themes
     * Themed tour, pre-designed (manually) [Victoria]
Page 5: Rating Your Tour [Victoria]
    
Styling: Wait and see [Severyn]

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
