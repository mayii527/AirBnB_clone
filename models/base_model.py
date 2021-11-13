#!/usr/bin/python3
"""BaseModel module"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class, define common
    attribute for the other"""

    def __init__(self, *args, **kwargs):
        """init a instance of BaseModel,
        *args dont be use"""

        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Return a string of the class BaseModel"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save update_at with current time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        new = self.__dict__.copy()
        new['__class__'] = self.__class__.__name__
        new['created_at'] = self.created_at.isoformat()
        new['updated_at'] = self.updated_at.isoformat()
        return new
