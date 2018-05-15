#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, Table
from sqlalchemy.orm import relationship

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    association_table = Table("place_amenity", Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''

    __tablename__ = 'places'


    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place", cascade="delete")

        amenities = relationship("Amenity", secondary=association_table, viewonly=False)

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''
                Getter for getting all the reviews for the place
            '''
            cls_dict = models.storage.all(models.classes["Review"])
            reviews_of_place = []
            current_place = self.id
            for key, value in cls_dict.items():
                if value.place_id == current_place:
                    reviews_of_place.append(value)
            return reviews_of_place

        @property
        def amenities(self):
            '''
                Getter for all the amenities
            '''
            all_amenities = models.storage.all(models.classes["Amenity"])
            for each_amen in all_amenities:
                if each_amen.place_id == self.id:
                    amenity_list.append(each_amen)
            return amenity_list

        @amenities.setter
        def amenities(self, obj=None):
            '''
                Setter for adding an object into the list of amenities
            '''
            if type(obj) == models.classes["Amenity"]:
#                amenity_list = self.amenities
                amenity_list.append(obj)
