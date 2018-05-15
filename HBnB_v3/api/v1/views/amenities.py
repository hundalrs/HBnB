#!/usr/bin/python3
'''view for State'''

from api.v1.views import app_views
from flask import Blueprint, jsonify, abort, request
from models import storage
import json
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'])
def all_amenities():
    ''' list all amenities in json format '''
    stored_amenities = storage.all('Amenity').values()
    amenity_list = []
    for amenity in stored_amenities:
        amenity_dict = amenity.to_dict()
        amenity_list.append(amenity_dict)
    return jsonify(amenity_list)


@app_views.route('/amenities', methods=['POST'])
def post_amenity():
    '''transforms http body request to a dictionary'''
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'name' in data:
        new_amenity = Amenity(**data)
        new_amenity.save()
        return jsonify(new_amenity.to_dict()), 201
    else:
        return jsonify("Missing name"), 400


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE'])
def retrieve_amenity(amenity_id):
    ''' retrieves state if not linked to object'''
    value = storage.get('Amenity', amenity_id)
    if request.method == 'DELETE':
        if value is None:
            abort(404)
        amenity_storage = storage.all('Amenity')
        for amenity in amenity_storage.values():
            if amenity.id == amenity_id:
                storage.delete(amenity)
        return jsonify({}), 200
    if value is None:
        abort(404)
    return jsonify(value.to_dict()), 200


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    '''updates amenity object'''
    amenity_obj = storage.get('Amenity', amenity_id)
    if amenity_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'id' or key != 'created_at' or key != 'updated_at':
            setattr(amenity_obj, key, value)
    amenity_obj.save()
    updated_amenity = amenity_obj.to_dict()
    return (jsonify(updated_amenity)), 200
