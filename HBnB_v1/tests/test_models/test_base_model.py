#!/usr/bin/python3
'''Unittest for BaseModel class'''

import io
import pep8 as pycodestyle
from models.base_model import BaseModel
import sys
import unittest


class TestBaseModel(unittest.TestCase):
    '''unittests for BaseModel'''

    def test_string(self):
        '''tests that str method has correct output'''
        instance = BaseModel()
        string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_model_created(self):
        '''testing if instance is created'''
        instance_1 = BaseModel()
        self.assertTrue(instance_1)

    def test_id_exists(self):
        '''testing if id exits'''
        instance_2 = BaseModel()
        self.assertEqual(len(instance_2.id), 36)

    def test_class(self):
        '''testing if class works'''
        instance_3 = BaseModel()
        self.assertEqual((instance_3.__class__), BaseModel)

    def test_dict(self):
        '''testing if to_dict returns dictionary'''
        instance_4 = BaseModel()
        self.assertEqual(dict, type(instance_4.to_dict()))

    def test_created_at(self):
        '''testing if created_at is assigned'''
        instance_4 = BaseModel()
        self.assertTrue(instance_4.created_at)

    def test_updated_at(self):
        '''testing if updated_at is assigned'''
        instance_4 = BaseModel()
        self.assertTrue(instance_4.updated_at)

    def test_save_created(self):
        '''Save changing updated_at to current datetime test but leaves
        created_at not changed'''
        model = BaseModel()
        prev = model.created_at
        model.save()
        self.assertEqual(prev, model.created_at)

    def test_save_updated(self):
        '''save method changing updated_at to current datetime test'''
        model = BaseModel()
        prev = model.updated_at
        model.save()
        self.assertNotEqual(prev, model.updated_at)

    def test_to_dict_type(self):
        '''test if to_dict returns dictionary'''
        m = BaseModel()
        model_dict = m.to_dict()
        self.assertEqual(dict, type(model_dict))

    def test_to_dictclass(self):
        '''tests if to_dict adds '__class__' to dictionary'''
        m = BaseModel()
        model_dict = m.to_dict()
        self.assertIn('__class__', model_dict)

    def test_to_dictid(self):
        '''test if 'id' is in dictionary'''
        m = BaseModel()
        model_dict = m.to_dict()
        self.assertIn('id', model_dict)

    def test_to_dict_id_string(self):
        '''tests if 'id' value is string'''
        m = BaseModel()
        model_dict = m.to_dict()
        self.assertEqual(str, type(model_dict['id']))

if __name__ == '__main__':
    unittest.main()
