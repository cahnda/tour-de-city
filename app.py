from flask import Flask, render_template, request, redirect, session, url_for
from py import *
import json

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)
env.globals.update(helpers=helpers)

@app.route('/map')
def map():
	return google_maps.map({
		'zoom': 8,
		'center': 'new google.maps.LatLng(-34.397, 150.644)'
	})

@app.route("/", methods = ["GET","POST"])
def index():
    print 'on index page'
    if request.method == "GET":
        print 'get'
        return render_template("index.html")
    else:
        print 'post'
        button = request.form['button']
        print 'after button'
        if button == "Submit":
            print 'right before'
            session['latitude'] = request.form.get('latitude', None)
            session['longitude'] = request.form.get('longitude', None)
            print session['latitude']
            print session['longitude']
            unicodeobj = request.values.getlist("tour")
            var = []
            for iterating_var in unicodeobj:
                print ' hello'
                iterating_var = iterating_var.encode ('ascii', 'ignore')
                var.append(iterating_var)
            print var
            session ['var'] = var
            return redirect(url_for('makeTour'))

@app.route ("/makeTour",  methods = ["GET","POST"])
def makeTour ():
        var  = session ['var']
        longitude = session['longitude']
        latitude = session['latitude']
        #Sweyn needs to add the get long + lat capability so that these can be inputed into google places. I'm using placeholders for now
        locs =  google_places.findPlaces (latitude, longitude, var)
        if request.method =="GET":
            return render_template("makeTour.html", locs = json.dumps(locs))
        else:
            button = request.form['button']
            if button == "Submit":
                print "hello"
                unicodeobj = request.values.getlist("place")
                var = []
                for iterating_var in unicodeobj:
                        iterating_var = iterating_var.encode ('ascii', 'ignore')
                        var.append(iterating_var)
                var = google_directions.get_waypoint_order(latitude+","+longitude,var,latitude+','+longitude)
                session['waypoints'] = var
                return redirect(url_for("showDirections"))

@app.route("/showDirections")
def showDirections():
    waylist = session['waypoints']
    waypoints = []
    for waypoint in waylist:
        waypoints.append({"location":waypoint.encode('ascii', 'ignore')})
    print "OUTPUT:" + str(waypoints)
    result = dict()
    result['start'] = 'New York'
    result['end'] = 'Boston'
    result['waypoints'] = json.dumps(waypoints)
    return render_template("showDirections.html", dict = result)


@app.errorhandler(404)
def error404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
	return render_template("errors/500.html"), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
