#!/usr/bin/python3
"""
Test suite for city model
"""

import unittest
from models.base_model import BaseModel
from models.city import City
from io import StringIO
from datetime import datetime


class TestUser(unittest.TestCase):
    '''City Class tests'''

    def test_inheritance(self):
        '''tests that City inherits from BaseModel'''
        new = City()
        self.assertIsInstance(new, BaseModel)

    def test_name_type(self):
        '''tests type of name'''
        new = City()
        name = getattr(new, "name")
        self.assertIsInstance(name, str)

    def test_name_type2(self):
        '''tests type of name'''
        new = City()
        name = getattr(new, "state_id")
        self.assertIsInstance(name, str)

    def updated_at_after_save(self):
        '''tests if updated_at is set to current datetime'''
        new = City()
        prev = new.updated_at
        new.save()
        self.assertNotEqual(prev, new.updated_at)

    def test_class_name(self):
        '''test __class__ key in dict'''
        new = City()
        new_dict = new.to_dict()
        self.assertIn('__class__', new_dict)

    def test_to_dict_id_is_str(self):
        '''checks if type of id val is a string'''
        new = City()
        new_dict = new.to_dict()
        self.assertEqual(str, type(new_dict['id']))

    def test_updated_at_in_dict(self):
        '''test if updated_at is in dictionary'''
        new = City()
        new_dict = new.to_dict()
        self.assertIn('updated_at', new_dict)

    def test_updated_at_is_str(self):
        '''test type of updated_at is string'''
        new = City()
        new_dict = new.to_dict()
        self.assertEqual(str, type(new_dict['updated_at']))

    def test_created_at_in_dict(self):
        '''test to see if created_at is in dictionary'''
        new = City()
        new_dict = new.to_dict()
        self.assertIn('created_at', new_dict)

    def test_created_at_is_str(self):
        '''test created at is string'''
        new = City()
        new_dict = new.to_dict()
        self.assertEqual(str, type(new_dict['created_at']))

    def test_setup(self):
        '''test init class attributes'''
        test1 = City()
        test2 = City()
        self.assertTrue(hasattr(test1, "state_id"))
        self.assertTrue(hasattr(test1, "name"))
        self.assertTrue(test1.id != test2.id)

if __name__ == '__main__':
    unittest.main()
