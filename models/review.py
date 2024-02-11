#!/usr/bin/python3
"""
This module defines the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.
    Public class attributes:
    - place_id: string - empty string: it will be the Place.id
    - user_id: string - empty string: it will be the User.id
    - text: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes Review object."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
