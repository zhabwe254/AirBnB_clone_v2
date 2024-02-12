#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.
    Public class attributes:
    - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes State object."""
        super().__init__(*args, **kwargs)
        self.name = ""
