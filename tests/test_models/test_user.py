#!/usr/bin/python3
""" Module tester to check if everything is working with User class """
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class Test_user(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(User.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_user = User()
        my_user.name = "Kamarov"
        self.assertEqual(type(my_user.name), str)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_user = User()
        self.assertTrue(issubclass(my_user.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(User.__doc__)
