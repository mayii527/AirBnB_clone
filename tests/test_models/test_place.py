#!/usr/bin/python3
"""this module tests the cases of BaseModel"""

from models.place import Place
from datetime import datetime
import unittest


class TestPlace(unittest.TestCase):
    """"test Place"""

    def setUp(self):
        """creating object of Place"""
        self.places = Place()

    def exist_Place(self):
        """test of exist the class Place"""
        self.assertEqual('[Place]' in str(self.places), True)

    def test_type(self):
        """test type of places"""
        self.assertEqual(type(self.places), Place)

    def test_places_id(self):
        """test id for Place"""
        self.assertEqual(type(self.places.id), str)
        self.assertTrue(hasattr(self.places, "id"))

    def test_places_created(self):
        """test created_ad for Place"""
        self.assertEqual(type(self.places.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.places, "created_at"))

    def test_places_update(self):
        """test update_at for Place"""
        self.assertEqual(type(self.places.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.places, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.places)), str)

    def test_Place_cityid(self):
        """test city_id in Place"""
        self.assertEqual(type(self.places.city_id), str)
        self.assertTrue(hasattr(self.places, "city_id"))

    def test_Place_userid(self):
        """test user_id in Place"""
        self.assertEqual(type(self.places.user_id), str)
        self.assertTrue(hasattr(self.places, "user_id"))

    def test_Place_name(self):
        """test name in Place"""
        self.assertEqual(type(self.places.name), str)
        self.assertTrue(hasattr(self.places, "name"))

    def test_Place_description(self):
        """test description in Place"""
        self.assertEqual(type(self.places.description), str)
        self.assertTrue(hasattr(self.places, "description"))

    def test_Place_numberrooms(self):
        """test number_rooms in Place"""
        self.assertEqual(type(self.places.number_rooms), int)
        self.assertTrue(hasattr(self.places, "number_rooms"))

    def test_Place_numberbathrooms(self):
        """test number_bathrooms in Place"""
        self.assertEqual(type(self.places.number_bathrooms), int)
        self.assertTrue(hasattr(self.places, "number_bathrooms"))

    def test_Place_maxguest(self):
        """test max_guest in Place"""
        self.assertEqual(type(self.places.max_guest), int)
        self.assertTrue(hasattr(self.places, "max_guest"))

    def test_Place_pricebynight(self):
        """test price_by_night in Place"""
        self.assertEqual(type(self.places.price_by_night), int)
        self.assertTrue(hasattr(self.places, "price_by_night"))

    def test_Place_latitude(self):
        """test latitude in Place"""
        self.assertEqual(type(self.places.latitude), float)
        self.assertTrue(hasattr(self.places, "latitude"))

    def test_Place_longitude(self):
        """test longitude in Place"""
        self.assertEqual(type(self.places.longitude), float)
        self.assertTrue(hasattr(self.places, "longitude"))

    def test_Place_amenityids(self):
        """test amenity_ids in Place"""
        self.assertEqual(type(self.places.amenity_ids), list)
        self.assertTrue(hasattr(self.places, "amenity_ids"))
    
if __name__ == "__main__":
    unittest.main()
