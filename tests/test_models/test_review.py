#!/usr/bin/python3
""" Review class tests module """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        attrs = vars(self.review)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.review, k))
            self.assertIsInstance(getattr(self.review, k, None), type(v))

    def test_place_id(self):
        self.review.place_id = "place.id"
        self.assertEqual(self.review.place_id, "place.id")

    def test_user_id(self):
        self.review.user_id = "user.id"
        self.assertEqual(self.review.user_id, "user.id")

    def test_text(self):
        self.review.text = "text"
        self.assertEqual(self.review.text, "text")

    def test_attribute_none(self):
        """Test if user attributes can handle None"""
        self.review.place_id = None
        self.review.user_id = None
        self.review.text = None
        self.assertIsNone(self.review.place_id)
        self.assertIsNone(self.review.user_id)
        self.assertIsNone(self.review.text)
