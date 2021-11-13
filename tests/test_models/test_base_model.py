#!/usr/bin/python3
"""Module for test base model class"""
import models
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Init test case of basemodel"""

    def testInstanceBaseModel(self):
        """Test if a object is from the class BaseModel"""
        test_object = BaseModel()
        self.assertIsInstance(test_object, BaseModel)

    def testObjectId(self):
        """Test if a class generate unique id"""
        test_object = BaseModel()
        test_object1 = BaseModel()
        self.assertNotEqual(test_object.id, test_object1.id)

    def testObjectSave(self):
        """Test to check if the method save is working"""
        test_object = BaseModel()
        first_date = test_object.updated_at
        test_object.save()
        second_date = test_object.updated_at
        self.assertNotEqual(first_date, second_date)
