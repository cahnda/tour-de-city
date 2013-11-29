from flask import Flask, render_template, request, redirect
from py import *

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route("/", methods = ["GET","POST"])
def index():
        print 'on index page'
        if request.method =="GET":
                print 'get'
                return render_template("index.html")
        else: 
                print 'post'
                button = request.form['button']
                if button == "Submit":
                        first = request.form['tour'].encode ('ascii',"ignore")
                        unicodeobj = request.values.getlist("tour")
                        var = []
                        for iterating_var in unicodeobj:
                                print ' hello'
                                iterating_var = iterating_var.encode ('ascii', 'ignore')
                                var.append(iterating_var)
                        print var
                return redirect ('/makeTour', var)

@app.route ("/makeTour",  methods = ["GET","POST"])
def makeTour (places):
        print 'at page 2'
        #Sweyn needs to add the get long + lat capability so that these can be inputed into google places. I'm using placeholders for now
        locs =  google_places.findPlaces (40.7472569628042, -73.99085998535156, places)
        if request.method =="GET":
                return render_template("makeTour.html", locs)
        else:
                button = request.form['button']
                if button == "Submit":
                        first = request.form['place'].encode ('ascii',"ignore")
                        unicodeobj = request.values.getlist("place")
                        var = []
                        for iterating_var in unicodeobj:
                                iterating_var = iterating_var.encode ('ascii', 'ignore')
                                var.append(iterating_var)
                        print var
               # return showTour (var) this should direct to the last page. Var contains all of the addresses.
                
@app.errorhandler(404)
def error404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
	return render_template("errors/500.html"), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
