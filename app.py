from flask import Flask, render_template, request
from py import *
import json


app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)
env.globals.update(helpers=helpers)

def get_form_value(key):
    return request.form[key].encode('ascii', 'ignore')

@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        latitude = get_form_value('gllpLatitude')
        longitude = get_form_value('gllpLongitude')
        return redirect(url_for('maptest'))


@app.route("/maptest")
def maptest():
    result = {
    	'start': 'New York',
    	'end': 'Chicago',
    	'waypoints': json.dumps([{"location":"Los Angeles"}])
    }
    print result['waypoints']
    return render_template("test.html", dict = result)

@app.errorhandler(404)
def error404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
	return render_template("errors/500.html"), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
