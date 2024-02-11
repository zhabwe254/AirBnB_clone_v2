#!/usr/bin/python3
"""
This module defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    Public class attributes:
    - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes Amenity object."""
        super().__init__(*args, **kwargs)
        self.name = ""
