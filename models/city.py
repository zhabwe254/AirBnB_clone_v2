#!/usr/bin/python3
"""
This module defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.
    Public class attributes:
    - state_id: string - empty string: it will be the State.id
    - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes City object."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
