#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
import os


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

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
        """Tests instantiation of City class."""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class."""
        city = City()
        attributes = storage.attributes()["City"]
        for attr, value in attributes.items():
            self.assertTrue(hasattr(city, attr))
            self.assertEqual(type(getattr(city, attr, None)), value)

    def test_save_method(self):
        """Tests the save method of City class."""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of City class."""
        city = City()
        city.name = "New City"
        city.state_id = "ABC123"
        city_dict = city.to_dict()
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())
        self.assertEqual(city_dict["name"], "New City")
        self.assertEqual(city_dict["state_id"], "ABC123")

    def test_str_method(self):
        """Tests the __str__ method of City class."""
        city = City()
        city.name = "New City"
        city.state_id = "ABC123"
        city_str = str(city)
        self.assertTrue("[City]" in city_str)
        self.assertTrue("name" in city_str)
        self.assertTrue("state_id" in city_str)


if __name__ == "__main__":
    unittest.main()
