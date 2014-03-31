from flask import Flask, session, render_template, request, redirect, url_for
from py import *

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True;
    app.run()
