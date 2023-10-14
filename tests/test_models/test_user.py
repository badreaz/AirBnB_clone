#!/usr/bin/python3
""" User class tests module """
import unittest
from models import storage
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertIsInstance(self.user, User)

    def test_attribute(self):
        attrs = vars(self.user)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.user, k))
            self.assertIsInstance(getattr(self.user, k, None), type(v))

    def test_email(self):
        self.user.email = "myemail@email.com"
        self.assertEqual(self.user.email, "myemail@email.com")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "email", 888)"""

    def test_password(self):
        self.user.password = "66382"
        self.assertEqual(self.user.password, "66382")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "password", 888)"""

    def test_first_name(self):
        self.user.first_name = "Betty"
        self.assertEqual(self.user.first_name, "Betty")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "first_name", 888)"""

    def test_last_name(self):
        self.user.last_name = "Bar"
        self.assertEqual(self.user.last_name, "Bar")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "last_name", 888) """
