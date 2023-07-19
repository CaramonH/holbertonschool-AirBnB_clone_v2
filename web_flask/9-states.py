#!/usr/bin/python3
"""
Write a script that starts a Flask web application
to load all cities of a state
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """tears down session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """displays list of states"""
    states = storage.all("State")
    return render_template('9-states.html', not_found=True)


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """displays state with id"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
