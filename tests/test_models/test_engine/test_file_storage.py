#!/usr/bin/python3
"""
unit test for file storage class
"""
from unittest import TestCase
from models.engine import file_storage


class FileStorageTest(TestCase):
    """ test case class for FileStorage """

    def setUp(self):
        self.storage = file_storage.FileStorage()

    def tearDown(self):
        del self.storage

    def test_all(self):
        self.assertTrue(type(self.storage.all()) is dict)


if __name__ == '__main__':
    unittst.main()
