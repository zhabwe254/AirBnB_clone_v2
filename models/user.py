#!/usr/bin/python3
"""Module for User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User.

    Attributes:
        email (str): The email of the User.
        password (str): The password of the User.
        first_name (str): The first name of the User.
        last_name (str): The last name of the User.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
