from flask import Flask
import utils

app = Flask(__name__)
app.secret_key = ''

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5007)
