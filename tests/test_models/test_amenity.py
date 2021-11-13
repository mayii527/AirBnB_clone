#!/usr/bin/python3
"""this module tests the cases of BaseModel"""

from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """"test Amenity"""


    def setUp(self):
        """creating object of Amenity"""
        self.Amenity = Amenity()


    def exist_Amenity(self):
        """test of exist the class Amenity"""
        self.assertEqual('[Amenity]' in str(self.Amenity), True)


    def test_type(self):
        """test type of Amenity"""
        self.assertEqual(type(self.Amenity), Amenity)


    def test_Amenity_id(self):
        """test id for Amenity"""
        self.assertEqual(type(self.Amenity.id), str)
        self.assertTrue(hasattr(self.Amenity, "id"))

    def test_Amenity_created(self):
        """test created_ad for Amenity"""
        self.assertEqual(type(self.Amenity.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.Amenity, "created_at"))

    def test_Amenity_update(self):
        """test update_at for Amenity"""
        self.assertEqual(type(self.Amenity.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.Amenity, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.Amenity)), str)

    def test_Amenity_name(self):
        """test name in Amenity"""
        self.assertEqual(type(self.Amenity.name), str)
        self.assertTrue(hasattr(self.Amenity, "name"))

if __name__ == "__main__":
    unittest.main()