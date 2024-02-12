#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inheriting from BaseModel"""
    place_id: str = ""
    user_id: str = ""  # Empty string: it will be the User.id
    text: str = ""
