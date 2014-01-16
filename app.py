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
@app.route('/map/<type>')
def map(type=''):
    return google_maps.map(type)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        button = request.form['button']
        if button == "Submit":
            session['latitude'] = request.form.get('latitude', None)
            session['longitude'] = request.form.get('longitude', None)
            session['transportation'] = request.form.get('tour-transportation', None)
            unicodeobj = request.values.getlist("tour")
            var = []
            for iterating_var in unicodeobj:
                iterating_var = iterating_var.encode ('ascii', 'ignore')
                var.append(iterating_var)
            session ['var'] = var
            session['page'] = 'makeTour'
            return redirect(url_for('makeTour'))

@app.route ("/makeTour",  methods = ["GET","POST"])
def makeTour():
    if 'page' in session.keys() and session['page'] == 'makeTour':
        var  = session['var']
        longitude = session['longitude']
        latitude = session['latitude']
        locs = google_places.findPlaces(latitude, longitude, var)
        if request.method =="GET":
            return render_template("make_tour.html",locs=locs)
        else:
            button = request.form['button']
            if button == "Submit":
                unicodeobj = request.values.getlist("place")
                counter = 0
                var = []
                for iterating_var in unicodeobj:
                    iterating_var = iterating_var.encode ('ascii', 'ignore')
                    var.append(iterating_var)
                    counter = counter + 1
                #because we don't have full access to google places
                if counter > 3:
                        return "You have chosen more than the maximum of three"
                        " (3) stops for your tour. Please go back and"
                        " refresh the page before selecting again"
                var = google_directions.get_waypoint_order(
                    latitude+","+longitude,var,latitude+','+longitude)
                session['waypoints'] = var
                session['page'] = 'showDirections'
                return redirect(url_for("showDirections"))
    else:
        return redirect('/')

@app.route("/showDirections")
def showDirections():
    if 'page' in session.keys() and session['page'] == 'showDirections':
        waylist = session['waypoints']
        endpoint = waylist.pop()
        utils.setBikeDatabase(session["latitude"], session["longitude"])
        waylist = utils.make_location_array(\
            session['latitude'], session['longitude'],session['latitude'], \
            session['longitude'], waylist)
        waypoints = []
        baseLoc = session['latitude'] + "," + session['longitude']
        for waypoint in waylist:
            waypoints.append({"location":waypoint.encode('ascii', 'ignore')})
        result = dict()
        result['start'] = baseLoc
        result['end'] = endpoint
        result['waypoints'] = json.dumps(waypoints)
        result['transportation'] = session['transportation']
        session['page'] = ''
        return render_template("show_directions.html", result = result)
    else:
        return redirect("/")


@app.route("/updatedata")
def updateData():
    utils.update_bike_stations("newyork") # placeholder argument
    return redirect("/")

@app.errorhandler(404)
def error400(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
    return render_template("errors/500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
