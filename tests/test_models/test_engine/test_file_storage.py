#!/usr/bin/python3
""" FileStorage class tests module """
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.obj = BaseModel()
        self.key = "BaseModel." + str(self.obj.id)

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_is_instance(self):
        self.assertIsInstance(storage, FileStorage)

    def test_new(self):
        objects = storage.all()
        self.assertEqual(objects[self.key].__dict__, self.obj.__dict__)

    def test_save(self):
        self.obj.name = "name"
        storage.save()
        objects = storage.all()
        self.assertEqual(objects[self.key].__dict__, self.obj.__dict__)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        self.storage = FileStorage()
        self.storage.reload()
        self.assertTrue(True)
