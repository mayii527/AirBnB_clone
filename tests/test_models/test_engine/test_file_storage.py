#!/usr/bin/python3
"""Test case engine"""
import models
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Test steps"""

    def test_is_an_instance(self):
        """Test if test_object is from the class FileStorage"""
        test_object = FileStorage()
        self.assertIsInstance(test_object, FileStorage)

    def test_path_atribute(self):
        """Test if is a valid path"""
        self.assertTrue(FileStorage._FileStorage_file_path, "file.json")
        self.assertEqual(FileStorage._FileStorage_file_path != 0)
        self.assertTrue(type(FileStorage._FileStorage_file_path) is str)

    def test_class_obj(self):
        """Test if objects is dict"""
        self.assertTrue(type(FileStorage._FileStorage_objects) is dict)

    def test_all(self):
        """test if all returns dict"""
        test_object = models.storage.all()
        self.assertIsInstance(test_object, dict)


if __name__ == "__main__":
    unittest.main()
