<<<<<<< HEAD
""" Module for User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines attributes for User class """
=======
#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
"""Represent a User.

     Attributes:
         email (str) : The email of the user.
    password (str) : The password of the user.
    first_name (str) : The first name of the user.
    last_name (str) : The last name of the user.
"""
>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87

    email = ""
    password = ""
    first_name = ""
    last_name = ""
