#!/usr/bin/python3
"""this module tests the cases of City"""
from models.city import City
from datetime import datetime
import unittest


class TestCity(unittest.TestCase):
    """"test city"""

    def setUp(self):
        """creating object of City"""
        self.Citys = City()

    def exist_City(self):
        """test of exist the class City"""
        self.assertEqual('[City]' in str(self.Citys), True)

    def test_type(self):
        """test type of Citys"""
        self.assertEqual(type(self.Citys), City)

    def test_Citys_id(self):
        """test id for City"""
        self.assertEqual(type(self.Citys.id), str)
        self.assertTrue(hasattr(self.Citys, "id"))

    def test_Citys_created(self):
        """test created_ad for City"""
        self.assertEqual(type(self.Citys.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.Citys, "created_at"))

    def test_Citys_update(self):
        """test update_at for City"""
        self.assertEqual(type(self.Citys.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.Citys, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.Citys)), str)

    def test_City_name(self):
        """test name in City"""
        self.assertEqual(type(self.Citys.name), str)
        self.assertTrue(hasattr(self.Citys, "name"))

    def test_City_stateid(self):
        """test state_id in City"""
        self.assertEqual(type(self.Citys.state_id), str)
        self.assertTrue(hasattr(self.Citys, "state_id"))

    def test_strmethod_id(self):
        '''Tests if id is type str'''
        self.assertEqual('id' in str(self.Citys), True)

    def test_strmethod_created(self):
        """test if created_at type str"""
        self.assertEqual('created_at' in str(self.Citys), True)

    def test_srtmethod_update(self):
        """test if update_at type str"""
        self.assertEqual('update_at' in str(self.Citys), False)

    def test_str_output(self):
        '''Tests for output expected'''
        output = "[{}] ({}) {}".format(
            self.Citys.__class__.__name__,
            self.Citys.id,
            self.Citys.__dict__
        )
        self.assertEqual(output, str(self.Citys))

if __name__ == "__main__":
    unittest.main()
