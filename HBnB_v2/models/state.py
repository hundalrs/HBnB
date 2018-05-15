#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
import models
import os
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:

        name = ""

        @property
        def cities(self):
            '''
                Getter for cities when using FileStorage system
            '''
            cls_dict = models.storage.all(models.classes["City"])
            cities_in_state = []
            current_state = self.id
            for key, value in cls_dict.items():
                if value.state_id == current_state:
                    cities_in_state.append(value)
            return cities_in_state
