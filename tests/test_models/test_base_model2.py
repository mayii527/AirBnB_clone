#!/usr/bin/python3
"""this module tests the cases of BaseModel"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest


class TestBaseModel(unittest.TestCase):
    """"dsfsfsdf"""
    def setUp(self):
        """creating object of BaseModel"""
        self.Model = BaseModel()

    def exist_BaseModel(self):
        """test of exist the class BaseModel"""
        self.assertEqual('[BaseModel]' in str(self.Model), True)

    def test_type(self):
        """test type of Model"""
        self.assertEqual(type(self.Model), BaseModel)

    def test_Model_id(self):
        """test id for BaseModel"""
        self.assertEqual(type(self.Model.id), str)
        self.assertTrue(hasattr(self.Model, "id"))

    def test_Model_created(self):
        """test created_ad for BaseModel"""
        self.assertEqual(type(self.Model.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.Model, "created_at"))

    def test_Model_update(self):
        """test update_at for BaseModel"""
        self.assertEqual(type(self.Model.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.Model, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.Model)), str)


if __name__ == "__main__":
    unittest.main()
