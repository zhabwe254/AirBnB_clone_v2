#!/usr/bin/python3
"""Module for City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City.

    Attributes:
        state_id (str): The state id of the City.
        name (str): The name of the City.
    """

    state_id = ""
    name = ""
