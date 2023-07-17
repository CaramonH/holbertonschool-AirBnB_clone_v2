#!/usr/bin/python3
"""Script that starts a Flask web app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """tears down session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """displays list of states"""
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)