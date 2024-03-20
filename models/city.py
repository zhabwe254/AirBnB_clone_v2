#!/usr/bin/python3
"""City Module for HBNB project."""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel,Base):
    """Class representing a City.

    Attributes:
>>City inherits from BaseModel and Base
>>state_id - representing a string column of maximum 60 characters
>> name -representing a string column of maximum 128 characters. nullable=False ensures that the value can't be null.
>>__tablename__ -represents the table name, cities
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
