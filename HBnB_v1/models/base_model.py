#!/usr/bin/python3
'''Base Class Module'''

from datetime import datetime
import models
import uuid


class BaseModel:
    '''model that all other classes inherit from'''

    def __init__(self, *args, **kwargs):
        '''intialize base class instances'''
        td = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) > 0:
            for key in kwargs:
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs[key], td)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs[key], td)
                elif key == '__class__':
                    self.__class__ = type(self)
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def save(self):
        '''updates datetime and assigns upon creation'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns dictionary containing all keys/values'''
        new_dict = {}
        for key in self.__dict__:
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = self.__dict__[key].isoformat()
            else:
                new_dict[key] = self.__dict__[key]
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        '''string representation'''
        cls_name = str(self.__class__.__name__)
        s_dict = str(self.__dict__)
        return '[{}] ({}) {}'.format(cls_name, self.id, s_dict)

    def __repr__(self):
        '''internal representation'''
        cls_name = str(self.__class__.__name__)
        s_dict = str(self.__dict__)
        return '[{}] ({}) {}'.format(cls_name, self.id, s_dict)
