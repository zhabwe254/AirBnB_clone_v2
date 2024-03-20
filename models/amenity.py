#!/usr/bin/python3
""" State Module for HBNB project """

#BaseModel is a superclass that the Amenity class will inherit from models.base_model
from models.base_model import BaseModel

#Amenity class is used to represent different amenities available at properties, such as pool, building and parking
class Amenity(BaseModel):
    name = ""
