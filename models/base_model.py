#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class for base model of object hierarchy.

    Attributes:
        id (str): The unique identifier of the object.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
