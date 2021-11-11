#!/usr/bin/python3
"""this module create the class call BaseModel"""
from datetime import date, datetime
from uuid import uuid4
import models

class BaseModel:
    """A class BaseModel
    Attributes"""

    def __init__(self, *args, **kwargs):

        ISOformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    self.__dict__[key] = datetime.strptime(value, ISOformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):

        """Return a string of the class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""

        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        new = self.__dict__.copy()
        new['__class__'] = self.__class__.__name__
        new['created_at'] = datetime.isoformat(new['created_at'])
        new['updated_at'] = datetime.isoformat(new['updated_at'])
        return new
