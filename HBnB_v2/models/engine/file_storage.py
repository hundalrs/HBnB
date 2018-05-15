#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return a dictionary of all the objects that match the passed class
            or return all if no class was passed
        '''
        if cls is None:
            return self.__objects
        else:
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = self.__objects[key]
            return cls_dict

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        self.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                self.__objects = json.load(fd)
            for key, val in self.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
            Delete an object if it's stored in the dictionary
        '''
        if obj is None:
            return
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        del self.__objects[key]
        self.save()

    def close(self):
        '''calls reload for deserialization of JSON file to objects'''
        self.reload()
