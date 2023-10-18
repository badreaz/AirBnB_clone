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
        self.assertEqual(self.user.email, "")
        self.user.email = "myemail@email.com"
        self.assertEqual(self.user.email, "myemail@email.com")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "email", 888)"""

    def test_password(self):
        self.assertEqual(self.user.password, "")
        self.user.password = "66382"
        self.assertEqual(self.user.password, "66382")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "password", 888)"""

    def test_first_name(self):
        self.assertEqual(self.user.first_name, "")
        self.user.first_name = "Betty"
        self.assertEqual(self.user.first_name, "Betty")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "first_name", 888)"""

    def test_last_name(self):
        self.assertEqual(self.user.last_name, "")
        self.user.last_name = "Bar"
        self.assertEqual(self.user.last_name, "Bar")
        """with self.assertRaises(AttributeError):
            setattr(self.user, "last_name", 888) """

    def test_attribute_none(self):
        self.user.email = None
        self.user.password = None
        self.user.first_name = None
        self.user.last_name = None
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.password)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)
