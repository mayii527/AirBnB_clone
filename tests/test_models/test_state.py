#!/usr/bin/python3
"""this module tests the cases of state class"""

from models.state import State
from datetime import datetime
import unittest


class TestState(unittest.TestCase):
    """"test state"""

    def setUp(self):
        """creating object of State"""
        self.State = State()

    def exist_State(self):
        """test of exist the class State"""
        self.assertEqual('[State]' in str(self.State), True)

    def test_type(self):
        """test type of State"""
        self.assertEqual(type(self.State), State)

    def test_State_id(self):
        """test id for State"""
        self.assertEqual(type(self.State.id), str)
        self.assertTrue(hasattr(self.State, "id"))

    def test_State_created(self):
        """test created_ad for State"""
        self.assertEqual(type(self.State.created_at), type(datetime.now()))
        self.assertTrue(hasattr(self.State, "created_at"))

    def test_State_update(self):
        """test update_at for State"""
        self.assertEqual(type(self.State.updated_at), type(datetime.now()))
        self.assertFalse(hasattr(self.State, "update_at"))

    def test_method_str(self):
        """test str"""
        self.assertEqual(type(str(self.State)), str)

    def test_State_name(self):
        """test name in State"""
        self.assertEqual(type(self.State.name), str)
        self.assertTrue(hasattr(self.State, "name"))

    def test_strmethod_id(self):
        '''Tests if id is type str'''
        self.assertEqual('id' in str(self.State), True)

    def test_strmethod_created(self):
        """test if created_at type str"""
        self.assertEqual('created_at' in str(self.State), True)

    def test_srtmethod_update(self):
        """test if update_at type str"""
        self.assertEqual('update_at' in str(self.State), False)

    def test_str_output(self):
        '''Tests for output expected'''
        output = "[{}] ({}) {}".format(
            self.State._class.name_,
            self.State.id,
            self.State._dict_
        )
        self.assertEqual(output, str(self.State))

if __name__ == "__main__":
    unittest.main()
