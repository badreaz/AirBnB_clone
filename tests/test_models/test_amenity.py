#!/usr/bin/python3
""" Amenity class tests module """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        attrs = vars(self.amenity)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.amenity, k))
            self.assertIsInstance(getattr(self.amenity, k, None), type(v))

    def test_name(self):
        self.amenity.name = "amenity name"
        self.assertEqual(self.amenity.name, "amenity name")
        self.assertIsInstance(self.amenity.name, str)
