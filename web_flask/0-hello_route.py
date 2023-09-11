#!/usr/bin/python3
"""
This script starts a Flask web application:
That listens on 0.0.0.0, port 5000
Routes:
/: display "Hello HBNB!"
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """This displays 'Hello HBNB!'"""
    return "Hello_hbnb!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
