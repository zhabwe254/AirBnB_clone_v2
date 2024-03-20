#!/usr/bin/python3
""" State Module for HBNB project """

#BaseModel is a superclass that the Amenity class will inherit from
from models.base_model import BaseModel

#Amenity class is used to represent different amenities available at properties, such as Wi-Fi, pool.
class Amenity(BaseModel):
    name = ""
