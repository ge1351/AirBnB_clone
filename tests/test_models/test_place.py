#!/usr/bin/python3
""" Module tester to check if everything is working with Place class """
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class Test_city(unittest.TestCase):
    """ Tester to check if place is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_place = Place()
        my_place.city_id = "placeholder"
        my_place.user_id = "placeholdertwo"
        my_place.name = "elmatadero"
        my_place.description = "alo mama"
        my_place.number_rooms = 1
        my_place.number_bathrooms = 1
        my_place.max_guest = 2
        my_place.price_by_night = 300
        my_place.latitude = 1.222
        my_place.longitude = 1.555
        my_place.amenity_ids = []
        self.assertEqual(type(my_place.city_id), str)
        self.assertEqual(type(my_place.user_id), str)
        self.assertEqual(type(my_place.name), str)
        self.assertEqual(type(my_place.description), str)
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertEqual(type(my_place.number_bathrooms), int)
        self.assertEqual(type(my_place.max_guest), int)
        self.assertEqual(type(my_place.price_by_night), int)
        self.assertEqual(type(my_place.latitude), float)
        self.assertEqual(type(my_place.longitude), float)
        self.assertEqual(type(my_place.amenity_ids), list)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_place = Place()
        self.assertTrue(issubclass(my_place.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(Place.__doc__)
