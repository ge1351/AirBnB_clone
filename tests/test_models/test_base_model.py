#!/usr/bin/python3
"""
    Unittester for the AirBnB project
"""
import unittest
import pep8
from models.base_model import BaseModel
from models import storage
import os
import datetime


class Test_base_model(unittest.TestCase):
    """ Tester that checks whetever everything is working as intended """

    def test_pep8_pycodestyle(self):
        """ Tester for pep8/pycodestyle """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors, please fix them")

    def test_instanceof_itself(self):
        """ Tester to see if he is an instance of BaseModel """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_checkif_docstring(self):
        """ Tester to see if the function is correctly documented """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_dict(self):
        """ this checks every value of the normal dict """
        my_base = BaseModel()
        my_base_dict = my_base.__dict__
        self.assertEqual(type(my_base).__name__, "BaseModel")
        self.assertTrue(hasattr(my_base_dict, "__class__"))

    """def test_to_dict(self):"""
        """ Tester to see if the function is correctly documented """
        """my_instance = BaseModel()
        my_instance.name = "Betty"
        my_instance.email = "holberton@email.com"
        instance_dict = my_instance.to_dict()
        self.assertTrue(type(instance_dict) is dict)
        self.assertIn("name", instance_dict.keys())
        self.assertIn("email", instance_dict.keys())"""

    def test_save(self):
        """ Tester to see if the function is correctly documented """
        my_instance = BaseModel()
        my_instance.name = "Betty"
        my_instance.email = "holberton@email.com"
        my_instance.save()
        objects = storage.all()
        instance = objects["BaseModel.{}".format(my_instance.id)]
        self.assertEqual(my_instance.id, instance.id)
        self.assertEqual(my_instance.name, instance.name)
        self.assertEqual(my_instance.email, instance.email)
        self.assertTrue(os.path.isfile("file.json"))

    def test_hasattrib(self):
        """ test if every attribute has been correctly made """
        my_base = BaseModel()
        self.assertTrue(hasattr(my_base, "id"))
        self.assertTrue(hasattr(my_base, "created_at"))
        self.assertTrue(hasattr(my_base, "updated_at"))
        self.assertTrue(hasattr(my_base, "__init__"))

    def test_typeofvalues(self):
        """ test to see if every values is of the correct type """
        my_base = BaseModel()
        self.assertEqual(type(my_base.id), str)
        self.assertEqual(type(my_base.updated_at), datetime.datetime)
        self.assertEqual(type(my_base.created_at), datetime.datetime)
