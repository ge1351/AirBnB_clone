#!/usr/bin/python3
""" Module tester to check if everything is working with User class """
import unittest
import pep8
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import json


class Test_file_storage(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8_pycodestyle(self):
        """ See if pep8 worked """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "found errors pep8")

    def test_ifdocumented(self):
        """ This checks if the file is correctly documented """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_instance_of_self(self):
        """ checks if test_attributes are the same """
        self.assertTrue(isinstance(storage, FileStorage))

    def test_all(self):
        """ check if all works and the objects are there works """
        my_object = BaseModel()
        my_object.name = "Illusive"
        my_object.email = "illusiveman@hotmail.com"
        my_object.save()
        storager = storage.all()
        regi_obj = storager["BaseModel.{}".format(my_object.id)]
        self.assertEqual(my_object.id, regi_obj.id)
        self.assertEqual(my_object.name, regi_obj.name)
        self.assertEqual(my_object.email, regi_obj.email)

    def test_new(self):
        """ test if new works """
        my_obj = BaseModel()
        storage.new(my_obj)
        storager = storage.all()
        self.assertIn(my_obj, storager.values())

    def test_save(self):
        """ tests if saves works """
        my_obj = BaseModel()
        my_obj.name = "IllusiveMan"
        my_obj.save()
        with open("file.json", "r", encoding="utf-8") as file_r:
            loader = json.load(file_r)
            name_getter = loader.get("BaseModel.{}".format(my_obj.id))
            self.assertEqual(name_getter['name'], my_obj.name)

    def test_reload(self):
        """ test the reload functions """
        my_us = User()
        my_us.name = "mama aiuda"
        my_us.save()
        storage.save()
        storage.reload()
        storager = storage.all()
        self.assertIsNot(my_us, storager.values())

    def test__objects_exists(self):
        """ test that objects exist """
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))

    def test__file_path_exists(self):
        """ test that path file exist """
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))
