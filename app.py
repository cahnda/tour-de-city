from flask import Flask, render_template, request, redirect, session, url_for
from py import *
from py import tours
from py.tours import Tour
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

@app.route("/clear")
def clear():
	session.clear()
	return redirect(url_for("index"))

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        print session
        if "google_user_dict" in session.keys():
            google_user_dict = session['google_user_dict']
        session.clear();
        try:
            session['google_user_dict'] = google_user_dict
        except:
            pass
        return render_template("index.html")
    else:
        button = request.form['button'] if 'button' in request.form else None
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
        return redirect('/premadetours')


@app.route ("/makeTour",  methods = ["GET","POST"])
def makeTour():
    if 'page' in session.keys() and session['page'] == 'makeTour':
        if "tour_dictionary" in session.keys():
            session.pop("tour_dictionary")
        res_types  = session['var']
        longitude = session['longitude']
        latitude = session['latitude']
        transportation = session['transportation']
        print latitude, longitude
        locs = google_places.findPlaces(latitude, longitude, res_types)
        locLen = len (locs)
        if request.method =="GET":
            return render_template("make_tour.html",locs=locs, locLen=locLen)
        else:
            button = request.form['button']
            if button == "Submit":
                unicodeobj = request.values.getlist("place")
                if len (unicodeobj) == 0:
                    return redirect('/makeTour')
                else:
                    print "THIS IS MY LENGTH"
                    print len (unicodeobj)
                    counter = 0
                    waypoints = []
                    place_names = []
                    for iterating_var in unicodeobj:
                        iterating_var = iterating_var.encode ('ascii', 'ignore')
                        waypoints.append(iterating_var)
                        counter = counter + 1
                    session['place_names'] = [l[0] for l in locs if l[1] in unicodeobj]
                    session['place_pics'] = [l[3] for l in locs if l[1] in waypoints]
                    waypoints = google_directions.get_waypoint_order(
                    latitude+","+longitude,waypoints,latitude+','+longitude)
                    session['waypoints'] = waypoints
                    session['page'] = 'showDirections'

                    waylist = session['waypoints']
                    endpoint = waylist.pop()
                    if transportation == "BIKING":
                        waylist = utils.make_location_array(\
                        session['latitude'], session['longitude'],session['latitude'], \
                        session['longitude'], waylist)
                    else:
                        waylist = session['waypoints']
                    waypoints = []
                    baseLoc = session['latitude'] + "," + session['longitude']
                    for waypoint in waylist:
                        waypoints.append({"location":waypoint.encode('ascii', 'ignore')})
                    result = dict()
                    result['start'] = baseLoc
                    result['end'] = endpoint
                    result['waypoints'] = json.dumps(waypoints)
                    result['transportation'] = session['transportation']
                    session["tour_dictionary"] = result
                    print result

                    user_id = None
                    if "google_user_dict" in session.keys():
                        user_id = session["google_user_dict"]["id"]
                    return redirect("/tour=%s" % utils.add_mongo_tour(result,
                        session["place_pics"], session['place_names'], user_id))

    else:
        return redirect('/')

@app.route("/tour=<tour_obj_id>", methods=["GET", "POST"])
def showDirections(tour_obj_id):
    if request.method == "GET":
        if "tour_dictionary" in session.keys():
            tour = session["tour_dictionary"]
        else:
            tour = utils.get_mongo_tour(tour_obj_id)["tour_dict"]

        return render_template("show_directions.html", result = tour)

    else:
        utils.rate_tour(tour_obj_id, int(request.json["rate_value"]))
        return ""

@app.route("/profile")
def profile():
	if "google_user_dict" in session:
		return render_template("profile.html",
			user_tours = utils.get_user_tours(session["google_user_dict"]["id"]))
	else:
		return redirect(url_for("index"))

@app.route("/logout")
def logout():
	if "google_user_dict" in session.keys():
		session.pop("google_user_dict")
	return redirect(url_for("index"))

@app.route("/rate", methods = ["GET", "POST"])
def rate():
    names = session['place_names']
    pics = session['place_pics']
    waypoints = []
    for i in range(len(names)):
        waypoints.append((names[i], pics[i]))
    return render_template('rate.html', waypoints=waypoints)

@app.route("/rate/<int:rating>", methods = ["GET", "POST"])
def rating(rating):
    names = session['place_names']
    addresses = session['waypoints']
    pics = session['place_pics']
    newTour = Tour(names,addresses,pics,rating)
    tours.addTour(newTour)
    print(newTour.addresses)
    return redirect('/toptours')


@app.route("/premadetours")
def premadetours():
	tours = sorted(utils.get_mongo_tours(), key=lambda tour: tour["rating"])[:5]
	return render_template("premade_tours.html", highest_ranked_tours = tours)


@app.route("/contact", methods = ["GET", "POST"])
def contact():
	if request.method == "GET":
		return render_template("contact.html")
	else:
		utils.send_email(
			request.form["email_address"],
			request.form["subject"],
			request.form["body"])
		return redirect(url_for("index"))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/updatedata")
def updateData():
    utils.update_bike_stations("newyork") # placeholder argument
    return redirect("/")

@app.route("/googleoauth", methods = ["POST"])
def googleoauth():
	session["google_user_dict"] = request.json
	return ""

@app.errorhandler(404)
def error400(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
    return render_template("errors/500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
