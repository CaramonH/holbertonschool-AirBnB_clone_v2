#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Display 'HBNB'"""
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        return 'C ' + text.replace('_', ' ')

    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        return 'Python ' + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        return str(n) + ' is a number'

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        states = storage.all(State).values()
        cities = list()

        for state in states:
            for city in state.cities:
                cities.append(city)

        return render_template('8-cities_by_states.html',
                               states=states, state_cities=cities)

    @app.route('/states', strict_slashes=False)
    def states():
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.route('/states/<id>', strict_slashes=False)
    def get_state_by_uuid(id):
        states = storage.all(State).values()

        for state in states:
            if id == state.id:
                return render_template('9-states.html',
                                       state=state, state_cities=state.cities)

        return render_template('9-states.html', not_found=True)

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
