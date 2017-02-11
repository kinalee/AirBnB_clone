#!/usr/bin/python3

from unittest import TestCase
from models.city import City

class CityTest(TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_type(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_attr(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
if __name__ == '__main__':
    unittest.City()
