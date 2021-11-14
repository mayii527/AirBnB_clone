#!/usr/bin/python3
"""this module create the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class with public attributes"""
    state_id = ""
    name = ""
