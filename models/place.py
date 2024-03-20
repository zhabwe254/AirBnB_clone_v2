<<<<<<< HEAD
""" Module for Place class """
=======
#!/usr/bin/python3
""" Place Module for HBNB project """

>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ Defines attributes for Place class """
=======
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87

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

