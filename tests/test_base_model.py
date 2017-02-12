#!/usr/bin/python3

from unittest import TestCase
from datetime import datetime
from models.base_model import BaseModel
import uuid


class BaseModelTest(TestCase):
    def setUp(self):
        self.bm1 = BaseModel()

    def tearDown(self):
        del self.bm1

    def test_init(self):
        self.assertTrue(hasattr(self.bm1, 'id'))
        self.assertTrue(hasattr(self.bm1, 'created_at'))
        self.assertFalse(hasattr(self.bm1, 'updated_at'))
        self.bm1.created_at

    def test_save(self):
        self.bm1.save()
        self.assertTrue(hasattr(self.bm1, 'updated_at'))

if __name__ == '__main__':
    unittest.BaseModel()
