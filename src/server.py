from flask import Flask
from search import checkParking
from flask_headers import headers


app = Flask(__name__)

@app.route("/")
@headers({'ngrok-skip-browser-warning' : True})
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/search')
@headers({'ngrok-skip-browser-warning' : True})
def run():
  obj = checkParking()
  return "<p>" + obj + "</p>"