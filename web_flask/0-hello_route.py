#!/usr/bin/env bash
"""
This script starts a Flask web application:
That listens on 0.0.0.0, port 5000
Routes:
/: display "Hello HBNB!"
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """This displays 'Hello HBNB!'"""
    return render_template("10-hbnb_filters.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=none)
