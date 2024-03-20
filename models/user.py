""" Module for User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines attributes for User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
