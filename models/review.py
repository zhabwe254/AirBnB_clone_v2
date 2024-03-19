#!/usr/bin/python3
"""Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review.

    Attributes:
        place_id (str): The place id of the Review.
        user_id (str): The user id of the Review.
        text (str): The text content of the Review.
    """

    place_id = ""
    user_id = ""
    text = ""
