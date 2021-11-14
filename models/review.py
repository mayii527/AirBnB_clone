#!/usr/bin/python3
"""this module create the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class with public attributes"""
    place_id = ""
    user_id = ""
    text = ""
