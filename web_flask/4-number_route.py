#!/usr/bin/python3
"""Starts a Flask web app with 5 routes"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def textC(text):
    new_text = text.replace("_", " ")
    return ('C ' + new_text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def textPython(text='is cool'):
    return ('Python ' + text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
