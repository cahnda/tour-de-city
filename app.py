from flask import Flask, render_template, request
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

                return first
#@app.selectionPage ("makeTour")
#def makeTour ():
                
@app.errorhandler(404)
def error404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
	return render_template("errors/500.html"), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
