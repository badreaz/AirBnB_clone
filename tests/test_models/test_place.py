#!/usr/bin/python3
""" Place class tests module """
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_init(self):
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        attrs = vars(self.place)
        for k, v in attrs.items():
            self.assertTrue(hasattr(self.place, k))
            self.assertIsInstance(getattr(self.place, k, None), type(v))

    def test_city_id(self):
        self.place.city_id = "city.id"
        self.assertEqual(self.place.city_id, "city.id")

    def test_user_id(self):
        self.place.user_id = "user.id"
        self.assertEqual(self.place.user_id, "user.id")

    def test_name(self):
        self.place.name = "name"
        self.assertEqual(self.place.name, "name")

    def test_description(self):
        self.place.description = "description"
        self.assertEqual(self.place.description, "description")

    def test_number_rooms(self):
        self.place.number_rooms = 3
        self.assertEqual(self.place.number_rooms, 3)

    def test_nummber_bathrooms(self):
        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_max_guest(self):
        self.place.max_guest = 6
        self.assertEqual(self.place.max_guest, 6)

    def test_price_by_night(self):
        self.place.price_by_night = 500
        self.assertEqual(self.place.price_by_night, 500)

    def test_latitude(self):
        self.place.latitude = 23.98
        self.assertEqual(self.place.latitude, 23.98)

    def test_longitude(self):
        self.place.longitude = 63.86
        self.assertEqual(self.place.longitude, 63.86)

    def test_amenity_ids(self):
        self.place.amenity_ids = ["amenity.id", "amenity.id"]
        self.assertEqual(self.place.amenity_ids, ["amenity.id", "amenity.id"])
