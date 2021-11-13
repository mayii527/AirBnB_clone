#!/usr/bin/python3
""" Definition of the parent class : BaseModel."""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """init a instance of BaseModel"""
        ISOformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, ISOformat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string of the class BaseModel"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save update_at with current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        new = self.__dict__.copy()
        new['__class__'] = self.__class__.__name__
        new['created_at'] = datetime.isoformat(new['created_at'])
        new['updated_at'] = datetime.isoformat(new['updated_at'])
        return new
