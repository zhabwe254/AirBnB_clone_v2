""" Module for Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines attributes for Review class """

    place_id = ""
    user_id = ""
    text = ""
