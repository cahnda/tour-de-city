#proj3-6-VSSD: CUSTOM BIKE TOURS IN NYC

## Group Members
Visit our trello [board](https://trello.com/b/aiLwI3nm/vssd) (*note: you must have been invited by a current member to view its contents*)!

  * Victoria Greene
  * David Cahn
  * Severyn Kozak
  * Sweyn Venderbush

## Our Project
Our project will generate tours of NYC and Boston. 

Tours will come in three forms:

  * Walking
  * Biking
  * Public transportation

We'll over overlay the *Google Maps*, *Google Places*, and *Citi Bike* APIs to highlight possible destinations, find the nearest bike depots, and plot an optimal route between desired locations. We will use the *FourSqaure* and *Yelp* APIs to prioritize locations based on user interest.

In addition to user-generated tours, we will allow users to select from pre-made tours of two-kinds:

  * Highest-rated by users (stored in mongo database)
  * Pre-designed by creators based on themes

##Hosted Version

Running at [softdev-server.stuycs.org:6007](http://softdev-server.stuycs.org:6007).

##Installing

``` sh
sudo chmod +x install.sh && ./install.sh
```

##Running

``` sh
python app.py
```


When running locally for the first time, visit
[/updatedata](http://localhost:6007/updatedata) to pull necessary information into your mongo server.

## Dependencies

  * mongodb
  * gunicorn
  * pip
  * virtualenv
  * geopy
  * pymongo

## Limitation

Purchasing Google Maps API would allow us to create a tour of greater length.
With the free version, we can only connect a limited number of waypoints. For
this version of the app, users can only select a maximum of three stops for
their tour.
