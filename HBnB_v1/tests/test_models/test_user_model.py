#!/usr/bin/python3
'''test suite for model/user.py'''
import unittest
import json
import os
import sys
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class TestUserClass(unittest.TestCase):
    '''test suite class'''
    def test_inheritance(self):
        '''test that user inherits from basemodel'''
        new = User()
        self.assertIsInstance(new, BaseModel)

    def test_attributes(self):
        '''checks if attributes exist'''
        test1 = User()
        test2 = User()
        self.assertTrue(hasattr(test1, "email"))
        self.assertTrue(hasattr(test1, "password"))
        self.assertTrue(hasattr(test1, "first_name"))
        self.assertTrue(hasattr(test1, "last_name"))
        self.assertTrue(type(test1.email) is str)
        self.assertTrue(type(test1.first_name) is str)
        self.assertTrue(type(test1.password) is str)
        self.assertTrue(type(test1. last_name) is str)
        self.assertTrue(type(test1.id) is str)
        self.assertTrue(test1.id != test2.id)

    def test_created_at(self):
        '''tests created at'''
        test1 = User()
        test2 = User()
        created1 = test1.created_at
        created2 = test2.created_at
        self.assertIsNot(created1, created2)
        self.assertTrue(type(created1) is datetime)

    def test_save_method(self):
        '''tests save method'''
        usr = User()
        test_updated = usr.updated_at
        usr.save()
        new_save = usr.updated_at
        self.assertTrue(test_updated != new_save)
        
    def test_string(self):
        '''tests string method output'''
        usr = User()
        usr_id = usr.id
        usr_dict = usr.__dict__
        st = "[User] ({}) {}".format(usr_id, usr_dict)
        self.assertEqual(st, str(usr))

if __name__ == '__main__':
    unittest.main()
