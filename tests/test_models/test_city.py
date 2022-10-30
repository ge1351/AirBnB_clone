#!/usr/bin/python3
""" Module tester to check if everything is working with City class """
import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class Test_city(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(City.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_city = City()
        my_city.name = "I dont know what is that"
        self.assertEqual(type(my_city.name), str)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_city = City()
        self.assertTrue(issubclass(my_city.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(City.__doc__)
