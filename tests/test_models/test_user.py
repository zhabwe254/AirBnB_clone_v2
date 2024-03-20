""" Module for testing User class """
import unittest
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """ Tests for the User class """

    @classmethod
    def setUpClass(cls):
        """ Set up for tests """
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        """ Remove test instances """
        del cls.user

    def test_pep8_conformance(self):
        """ Test that the code conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

    def test_documentation(self):
        """ Test to see if documentation is created """
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """ Test attributes """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_inheritance(self):
        """ Test inheritance """
        self.assertIsInstance(self.user, BaseModel)

    def test_types(self):
        """ Test types """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
       

