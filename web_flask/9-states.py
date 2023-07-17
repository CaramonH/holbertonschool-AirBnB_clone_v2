#!/usr/bin/python3
"""Script that starts a Flask web app"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """tears down session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays list of states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states.values())


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """displays state with id"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)