#!/usr/bin/python3
""" City class tests module """
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_init(self):
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        attrs = vars(self.city)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.city, k))
            self.assertIsInstance(getattr(self.city, k, None), type(v))

    def test_state_id(self):
        self.city.state_id = "state.id"
        self.assertEqual(self.city.state_id, "state.id")

    def test_name(self):
        self.city.name = "city"
        self.assertEqual(self.city.name, "city")
