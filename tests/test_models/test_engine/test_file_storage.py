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
