#!/usr/bin/python3
""" Module tester to check if everything is working with state class """
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel


class Test_state(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(State.__doc__)

    def test_attribute_type(self):
        """ checks if test_attributes are the same """
        my_state = State()
        my_state.name = "TX"
        self.assertEqual(type(my_state.name), str)

    def test_inheritance(self):
        """ checks if he is correctly inheriting from BaseModel """
        my_state = State()
        self.assertTrue(issubclass(my_state.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings """
        self.assertIsNotNone(State.__doc__)
