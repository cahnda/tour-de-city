#! /bin/bash

sudo apt-get install python-pip
sudo apt-get install gunicorn
sudo apt-get install mongo

pip install geopy pymongo
pip install virtualenv
virtualenv env

source env/bin/activate
mongod
gunicorn -w 4 -b 0.0.0.0:6007 -p pid app:app
