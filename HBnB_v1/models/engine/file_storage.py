#!/usr/bin/python3
'''Storage Module'''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes instances to JSON and deserializes to instances'''

    __file_path = "file.json"
    __objects = {}
    classname = {'BaseModel': BaseModel, 'User': User, 'State': State,
                 'City': City, 'Amenity': Amenity, 'Place': Place,
                 'Review': Review}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''returns sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        final_dict = {}
        for key, value in self.__objects.items():
            final_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+") as myFile:
            json.dump(final_dict, myFile)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as myFile:
                json_dicts = json.load(myFile)
                for key, value in json_dicts.items():
                    holder = value['__class__']
                    self.__objects[key] = self.classname[holder](**value)
        else:
            pass
