#!/usr/bin/python3
"""this module tests the cases of test cases review"""

from models.review import Review
from datetime import datetime
import unittest


class TestReview(unittest.TestCase):
    """"test Review"""

    def setUp(self):
        """creating object of Review"""
        self.reviews = Review()

    def exist_Review(self):
        """test of exist the class Review"""
        self.assertEqual('[Review]' in str(self.reviews), True)

    def test_type(self):
        """test type of reviews"""
        self.assertEqual(type(self.reviews), Review)

    def test_reviews_id(self):
        """test id for Review"""
        self.assertEqual(type(self.reviews.id), str)
        self.assertTrue(hasattr(self.reviews, "id"))

    def test_reviews_created(self):
        """test created_ad for Review"""
        self.assertEqual(type(self.reviews.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.reviews, "created_at"))

    def test_reviews_update(self):
        """test update_at for Review"""
        self.assertEqual(type(self.reviews.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.reviews, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.reviews)), str)

    def test_Review_placeid(self):
        """test place_id in Review"""
        self.assertEqual(type(self.reviews.place_id), str)
        self.assertTrue(hasattr(self.reviews, "place_id"))

    def test_Review_userid(self):
        """test user_id in Review"""
        self.assertEqual(type(self.reviews.user_id), str)
        self.assertTrue(hasattr(self.reviews, "user_id"))

    def test_Review_text(self):
        """test text in Review"""
        self.assertEqual(type(self.reviews.text), str)
        self.assertTrue(hasattr(self.reviews, "text"))

if __name__ == "__main__":
    unittest.main()
