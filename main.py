from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
	msg = "Welcome to the home page"
	return render_template("index.html", msg=msg)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	app.run(debug = True)