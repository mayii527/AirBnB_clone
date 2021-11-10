#!/usr/bin/python3
"""this module create the class User"""
from model.base_model import BaseModel


class User(BaseModel):
    """ user class with public attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
