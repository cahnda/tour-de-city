from flask import Flask, render_template
from py import *

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5007)
