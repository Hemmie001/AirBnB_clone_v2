#!/usr/bin/python3
"""
this script starts a Flask web application:
That listens on 0.0.0.0, port 5000
and routes:
1 /: display “Hello HBNB!”
2 /hbnb: display “HBNB”
3 /c/<text>: display “C ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
4 /python/(<text>): display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
5 /number/<n>: display “n is a number” only if n is an integer
6 /number/<n>: display “n is a number” only if n is an integer
7 /number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
8   /number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition
The default value of text is “is cool”
H1 tag: “Number: n” inside the tag BODY
My route defination uses strict_slashes=False in your route definition
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays 'C' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """displays 'Python' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays "n is a number" only if <n> is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays an HTML page only if <n> is an integer
       'H1' tag: "Number: <n>" inside the 'BODY' tag"""
    return render_template("5-number.html", var=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """displays an HTML page only if <n> is an integer
       'H1' tag: "Number: <n> is <even|odd>" inside the 'BODY' tag"""
    if (n % 2 == 0):
        return render_template("6-number_odd_or_even.html",
                               var="{} is even".format(n))
    return render_template("6-number_odd_or_even.html",
                           var="{} is odd".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
