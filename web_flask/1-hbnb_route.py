#!/usr/bin/python3
"""
This script starts a Flask web application
that listens on 0.0.0.0, port 5000
the routes should  display “Hello HBNB!”
it should use strict_slashes=False in your route definition
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
