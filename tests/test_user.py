#!/usr/bin/python3

from unittest import TestCase
from models.user import User


class UserTest(TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_type(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_attr(self):
        self.assertTrue(self.user, 'email')
        self.assertTrue(self.user, 'password')
        self.assertTrue(self.user, 'first_name')
        self.assertTrue(self.user, 'last_name')

if __name__ == '__main__':
    unittest.User()
