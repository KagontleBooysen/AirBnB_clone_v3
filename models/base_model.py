#!/usr/bin/python3
"""This module contains the BaseModel class"""

from datetime import datetime
import models
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


# print format of create_engine
# 'mysql+mysqldb://<username>:<password>@<host>:<port>/<db_name>'
# connect with the mysql database

# Base = declarative_base()
if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Base class for all common attributes and methods"""
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True, nullable=False,
                    default=str(uuid.uuid4()))
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""

        # if keyword argument is provided initialize class with the specified
        # values
        if kwargs != {}:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if (key == 'created_at' and type(val) == str):
                    # val = datetime.fromisoformat(val)
                    # the above .fromisoformat() method does
                    # not work in python 3.4
                    # print(type(val))
                    # print("val: ", val)
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                if (key == 'updated_at' and type(val) == str):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                self.__setattr__(key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of BaseModel"""

        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Return a dict representation of the BaseModel"""

        formated_dict = self.__dict__.copy()
        formated_dict['created_at'] = formated_dict['created_at'].isoformat()
        formated_dict['updated_at'] = formated_dict['updated_at'].isoformat()
        formated_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in formated_dict:
            del formated_dict['_sa_instance_state']
        return formated_dict
