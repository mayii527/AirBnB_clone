#!/usr/bin/python3
"""this module tests the cases of BaseModel"""

from models.user import User
from datetime import datetime
import unittest


class TestUser(unittest.TestCase):
    """"test for clas User"""

    def setUp(self):
        """creating object of User"""
        self.users = User()

    def exist_User(self):
        """test of exist the class User"""
        self.assertEqual('[User]' in str(self.users), True)

    def test_type(self):
        """test type of users"""
        self.assertEqual(type(self.users), User)

    def test_users_id(self):
        """test id for User"""
        self.assertEqual(type(self.users.id), str)
        self.assertTrue(hasattr(self.users, "id"))

    def test_users_created(self):
        """test created_ad for User"""
        self.assertEqual(type(self.users.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.users, "created_at"))

    def test_users_update(self):
        """test update_at for User"""
        self.assertEqual(type(self.users.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.users, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.users)), str)

    def test_User_email(self):
        """test email in User"""
        self.assertEqual(type(self.users.email), str)
        self.assertTrue(hasattr(self.users, "email"))

    def test_User_password(self):
        """test password in User"""
        self.assertEqual(type(self.users.password), str)
        self.assertTrue(hasattr(self.users, "password"))

    def test_User_firstname(self):
        """test of first_name in User"""
        pass

    def test_User_lastname(self):
        """test of first_name in User"""
        pass


if __name__ == "__main__":
    unittest.main()
