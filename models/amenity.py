#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an Amenity.

    Attributes:
        name (str): The name of the Amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of an Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Returns a string representation of the Amenity object."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of the Amenity object."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

