#!/usr/bin/python3
"""Module for Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a Place.

    Attributes:
        city_id (str): The city id of the Place.
        user_id (str): The user id of the Place.
        name (str): The name of the Place.
        description (str): The description of the Place.
        number_rooms (int): The number of rooms in the Place.
        number_bathrooms (int): The number of bathrooms in the Place.
        max_guest (int): The maximum number of guests in the Place.
        price_by_night (int): The price per night of the Place.
        latitude (float): The latitude of the Place.
        longitude (float): The longitude of the Place.
        amenity_ids (list): List of Amenity ids associated with the Place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
