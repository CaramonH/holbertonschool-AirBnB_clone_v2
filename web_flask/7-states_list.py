#!/usr/bin/python3
"""Script that starts a Flask web app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """tears down new session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
