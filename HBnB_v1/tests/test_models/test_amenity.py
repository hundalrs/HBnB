#!/usr/bin/python3
'''test suite for model/amenity.py'''
import unittest
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class TestAmenityClass(unittest.TestCase):
    '''test suite class'''
    def test_inheritance(self):
        '''test that user inherits from basemodel'''
        new = Amenity()
        self.assertIsInstance(new, BaseModel)

    def test_attributes(self):
        '''checks if attributes exist'''
        test1 = Amenity()
        test2 = Amenity()
        self.assertTrue(hasattr(test1, "name"))
        self.assertTrue(test1.id != test2.id)

    def test_created_at(self):
        '''tests created at'''
        test1 = Amenity()
        test2 = Amenity()
        created1 = test1.created_at
        created2 = test2.created_at
        self.assertTrue(created1 != created2)
        self.assertTrue(type(created1) is datetime)

    def test_save_method(self):
        '''tests save method'''
        new = Amenity()
        test_updated = new.updated_at
        new.save()
        new_save = new.updated_at
        self.assertTrue(test_updated != new_save)

if __name__ == '__main__':
    unittest.main()
