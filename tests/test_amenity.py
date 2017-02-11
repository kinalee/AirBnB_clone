#!/usr/bin/python3

from unittest import TestCase
from models.amenity import Amenity

class AmenityTest(TestCase):
    def setUp(self):
        self.am = Amenity()

    def tearDown(self):
        del self.am

    def test_type(self):
        self.assertIsInstance(self.am.name, str)

    def test_attr(self):
        self.assertTrue(hasattr(self.am, 'name'))

if __name__ == '__main__':
    unittest.Amenity()
