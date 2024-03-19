#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
import os


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        user = User()
        attributes = storage.attributes()["User"]
        for attr, value in attributes.items():
            self.assertTrue(hasattr(user, attr))
            self.assertEqual(type(getattr(user, attr, None)), value)

    def test_save_method(self):
        """Tests the save method of User class."""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of User class."""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_str_method(self):
        """Tests the __str__ method of User class."""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_str = str(user)
        self.assertTrue("[User]" in user_str)
        self.assertTrue("email" in user_str)
        self.assertTrue("password" in user_str)
        self.assertTrue("first_name" in user_str)
        self.assertTrue("last_name" in user_str)


if __name__ == "__main__":
    unittest.main()
