#!/usr/bin/python3
""" unittests for the BaseModel class """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_with_args(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(len(my_model.id), 36)

    def test_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
    
    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        json_model = my_model.to_dict()
        self.assertEqual(json_model["__class__"], "BaseModel")
        self.assertEqual(json_model["my_number"], str(my_model.my_number))
        self.assertEqual(jjson_model["name"], my_model.name)
