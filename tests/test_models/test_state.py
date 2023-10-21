#!/usr/bin/python3
""" State class test module """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_init(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        attrs = vars(self.state)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.state, k))
            self.assertIsInstance(getattr(self.state, k, None), type(v))

    def test_name(self):
        self.state.name = "state"
        self.assertEqual(self.state.name, "state")
