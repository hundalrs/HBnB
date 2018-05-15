#!/usr/bin/python3
'''test suite for model/state.py'''
import unittest
from models import storage
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class TestStateClass(unittest.TestCase):
    '''test suite class'''
    def test_inheritance(self):
        '''test that user inherits from basemodel'''
        new = Place()
        self.assertIsInstance(new, BaseModel)

    def test_attributes(self):
        '''checks if attributes exist'''
        test1 = Place()
        test2 = Place()
        self.assertTrue(hasattr(test1, "name"))
        self.assertTrue(hasattr(test1, "latitude"))
        self.assertTrue(hasattr(test1, "number_bathrooms"))
        self.assertTrue(hasattr(test1, "number_rooms"))
        self.assertTrue(hasattr(test1, "user_id"))
        self.assertTrue(hasattr(test1, "city_id"))
        self.assertTrue(hasattr(test2, "latitude"))
        self.assertTrue(hasattr(test1, "name"))
        self.assertTrue(test1.id != test2.id)
       
    def test_created_at(self):
        '''tests types '''
        test1 = Place()
        self.assertTrue(type(test1.name) is str)
        self.assertTrue(type(test1.latitude) is float)
        self.assertTrue(type(test1.city_id) is str)
        self.assertTrue(type(test1.user_id) is str)
        self.assertTrue(type(test1.number_rooms) is int)
        self.assertTrue(type(test1.number_bathrooms) is int)
        self.assertTrue(type(test1.longitude) is float)
        
    def test_save_method(self):
        '''tests save method'''
        new = Place()
        test_updated = new.updated_at
        new.save()
        new_save = new.updated_at
        self.assertTrue(test_updated != new_save)
        
if __name__ == '__main__':
    unittest.main()
