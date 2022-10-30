#!/usr/bin/python3
""" Module tester to check if everything is working with amenity class """
import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_amenity(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_amenity = Amenity()
        my_amenity.name = "I dont know what is that"
        self.assertEqual(type(my_amenity.name), str)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_amenity = Amenity()
        self.assertTrue(issubclass(my_amenity.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(Amenity.__doc__)
