#!/usr/bin/python3

from unittest import TestCase
from models.place import Place

class PlaceTest(TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_type(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenities, list)

    def test_attr(self):
        self.assertTrue(self.place, 'city_id')
        self.assertTrue(self.place, 'user_id')
        self.assertTrue(self.place, 'name')
        self.assertTrue(self.place, 'description')
        self.assertTrue(self.place, 'number_rooms')
        self.assertTrue(self.place, 'number_bathrooms')
        self.assertTrue(self.place, 'max_guest')
        self.assertTrue(self.place, 'price_by_night')
        self.assertTrue(self.place, 'latitude')
        self.assertTrue(self.place, 'longitude')
        self.assertTrue(self.place, 'amenities')

if __name__ == '__main__':
    unittest.Place()
