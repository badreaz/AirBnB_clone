#!/usr/bin/python3
""" unittests for the BaseModel class """
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_with_args(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(len(my_model.id), 36)
        storage.save()

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
        self.assertEqual(json_model["my_number"], my_model.my_number)
        self.assertEqual(json_model["name"], my_model.name)

    def test_kwargs(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        dic = my_model.to_dict()
        new_model = BaseModel(**dic)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertNotEqual(my_model, new_model)
