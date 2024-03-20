""" Module for testing BaseModel class """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel class """

    @classmethod
    def setUpClass(cls):
        """ Set up for tests """
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ Remove test instances """
        del cls.base

    def test_pep8_conformance(self):
        """ Test that the code conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

    def test_documentation(self):
        """ Test to see if documentation is created """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """ Test attributes """
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))

    def test_id(self):
        """ Test id """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_updated(self):
        """ Test created_at and updated_at """
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """ Test __str__ method """
        string = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), string)

    def test_save(self):
        """ Test save method """
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """ Test to_dict method """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertIsInstance(base_dict['id'], str)
