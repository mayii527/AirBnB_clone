#!/usr/bin/python3
"""this module tests the cases of Amenity class"""

from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """"test Amenity"""

    def setUp(self):
        """creating object of Amenity"""
        self.Amenitys = Amenity()

    def exist_Amenity(self):
        """test of exist the class Amenity"""
        self.assertEqual('[Amenity]' in str(self.Amenitys), True)

    def test_type(self):
        """test type of Amenity"""
        self.assertEqual(type(self.Amenitys), Amenity)

    def test_Amenity_id(self):
        """test id for Amenity"""
        self.assertEqual(type(self.Amenitys.id), str)
        self.assertTrue(hasattr(self.Amenitys, "id"))

    def test_Amenity_created(self):
        """test created_ad for Amenity"""
        self.assertEqual(type(self.Amenitys.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.Amenitys, "created_at"))

    def test_Amenity_update(self):
        """test update_at for Amenity"""
        self.assertEqual(type(self.Amenitys.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.Amenitys, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.Amenitys)), str)

    def test_Amenity_name(self):
        """test name in Amenity"""
        self.assertEqual(type(self.Amenitys.name), str)
        self.assertTrue(hasattr(self.Amenitys, "name"))

    def test_strmethod_id(self):
        '''Tests if id is type str'''
        self.assertEqual('id' in str(self.Amenitys), True)

    def test_strmethod_created(self):
        """test if created_at type str"""
        self.assertEqual('created_at' in str(self.Amenitys), True)

    def test_srtmethod_update(self):
        """test if update_at type str"""
        self.assertEqual('update_at' in str(self.Amenitys), False)

    def test_strmethod_classname(self):
        '''Tests if class name in str'''
        self.assertEqual('[Amenity]' in str(self.Amenitys), True)

    def test_str_output(self):
        '''Tests for output expected'''
        output = "[{}] ({}) {}".format(
            self.Amenitys.__class__.__name__,
            self.Amenitys.id,
            self.Amenitys.__dict__
        )
        self.assertEqual(output, str(self.Amenitys))

if __name__ == "__main__":
    unittest.main()
