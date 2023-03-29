#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):

    """This is the class for State
    Attributes:
        name: input name
    """

    if models.storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
