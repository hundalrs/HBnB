#!/usr/bin/python3
'''File Storage test module'''

import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class MyTest(unittest.TestCase):
    '''unittests for file storage'''

    def setUp(self):
        self.basemodel = BaseModel()

    def tearDown(self):
        del self.basemodel

    def setUp(self):
        self.filestorage = FileStorage()

    def tearDown(self):
        del self.filestorage

    def test_all(self):
        '''check if the all method works'''
        new_dict = self.filestorage.all()
        self.assertEqual(type(new_dict), dict)

    def test_filestorage(self):
        '''check if filestorage is working correctly'''
        self.assertEqual(type(self.filestorage), type(FileStorage()))

    def test_reload(self):
        '''check if reload works after saving'''
        instance_1 = BaseModel()
        instance_1_id = instance_1.id
        self.filestorage.new(instance_1)
        self.filestorage.save()
        self.filestorage.reload()
        instance_1_dict = self.filestorage.all()
        self.assertEqual(type(instance_1_dict), dict)

    def save(self):
        '''check if the save method works'''
        instance_2 = self.basemodel
        self.filestorage.new(instance_2)
        self.filestorage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_str_new(self):
        '''check if str and new work'''
        instance = self.filestorage
        model = BaseModel()
        instance.new(model)
        test_string = "{}.{}".format(model.__class__.__name__, model.id)
        new_dict = instance.all()
        self.assertIn(test_string, new_dict)
