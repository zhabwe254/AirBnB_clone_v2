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

    email = ""
    password = ""
    first_name = ""
    last_name = ""
