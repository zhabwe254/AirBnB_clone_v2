<<<<<<< HEAD
""" Module for State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Defines attributes for State class """

    name = ""
=======
#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orpha')
>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87
