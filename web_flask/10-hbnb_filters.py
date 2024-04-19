#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page like 6-index.html with HBNB filters."""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template(
        '10-hbnb_filters.html',
        states=sorted(states.values(), key=lambda x: x.name),
        cities=sorted(cities.values(), key=lambda x: x.name),
        amenities=sorted(amenities.values(), key=lambda x: x.name)
    )


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
