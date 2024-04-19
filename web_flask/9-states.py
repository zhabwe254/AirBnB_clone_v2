#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a HTML page listing all states."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Displays a HTML page showing details of a specific state."""
    state = storage.get(State, id)
    if state:
        return render_template('10-states.html', state=state)
    else:
        return render_template('10-not_found.html')


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
