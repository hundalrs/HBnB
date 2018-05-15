#!/usr/bin/python3
'''test suite for model/review.py'''
import unittest
from models import storage
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class TestReviewClass(unittest.TestCase):
    '''test suite class'''
    def test_inheritance(self):
        '''test that user inherits from basemodel'''
        new = Review()
        self.assertIsInstance(new, BaseModel)

    def test_attributes(self):
        '''checks if attributes exist'''
        test1 = Review()
        test2 = Review()
        self.assertTrue(hasattr(test1, "place_id"))
        self.assertTrue(hasattr(test1, "text"))
        self.assertTrue(hasattr(test1, "user_id"))
        self.assertTrue(type(test1.user_id) is str)
        self.assertTrue(type(test1.place_id) is str)
        self.assertTrue(type(test1.text) is str)
        self.assertTrue(test1.id != test2.id)

    def test_created_at(self):
        '''tests created at'''
        test1 = Review()
        test2 = Review()
        created1 = test1.place_id
        created2 = test2.place_id
        self.assertTrue(created1 == created2)
        self.assertTrue(type(created2) is str)

    def test_save_method(self):
        '''tests save method'''
        new = Review()
        test_updated = new.updated_at
        new.save()
        new_save = new.updated_at
        self.assertTrue(test_updated != new_save)

if __name__ == '__main__':
    unittest.main()
