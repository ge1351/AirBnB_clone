#!/usr/bin/python3
""" Module tester to check if everything is working with Review class """
import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class Test_city(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_review = Review()
        my_review.place_id = "the id of the place"
        my_review.user_id = "why are we like this?"
        my_review.text = "this place stinks, please end me rightly"
        self.assertEqual(type(my_review.place_id), str)
        self.assertEqual(type(my_review.user_id), str)
        self.assertEqual(type(my_review.text), str)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_review = Review()
        self.assertTrue(issubclass(my_review.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(Review.__doc__)
