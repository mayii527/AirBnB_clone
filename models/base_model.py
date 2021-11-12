#!/usr/bin/python3
""" this module create the class call BaseModel
This function creates the superclass from which the 
subclasses that we will be using throughout the 
project will later inherit"""

import models
from datetime import datetime
""" this module generate general current date and time"""
from uuid import uuid4
""" this module generate a id unique random"""

class BaseModel:
   """A class BaseModel
    Attributes
    Parameters
    ----------
    parametro_1 : type: dictionary
    each attribute is a dictionary key"""

    def __init__(self, *args, **kwargs):

        ISOformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, ISOformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):

        """Return a string of the class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """save update_at with current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        new = self.__dict__.copy()
      """ Copy function returns a copy of the dictionary 
        without modifying the original """
        new['__class__'] = self.__class__.__name__
        new['created_at'] = datetime.isoformat(new['created_at'])
        new['updated_at'] = datetime.isoformat(new['updated_at'])
        """ return: type: dictionary"""
        return new
