#!/usr/bin/python3
'''view for Place'''

from api.v1.views import app_views
from flask import Blueprint, jsonify, abort, request
from models import storage
import json
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def all_places(city_id):
    ''' list all places in json format '''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404)
    stored_places = storage.all('Place').values()
    place_list = []
    for place in stored_places:
        place_dict = place.to_dict()
        if place.city_id == city_id:
            place_list.append(place_dict)
    return jsonify(place_list)


@app_views.route('/places/<place_id>', methods=['GET'])
def find_place(place_id):
    ''' match place_id to place '''
    place_obj = storage.get('Place', place_id)
    if place_obj is None:
        abort(404)
    return jsonify(place_obj.to_dict())


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def post_place(city_id):
    '''POST Place'''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'user_id' not in data:
        return jsonify("Missing user_id"), 400
    if 'name' in data:
        value = storage.get('User', data['user_id'])
        if value is None:
            abort(404)
        if value is not None:
            new_place = Place(**data)
            setattr(new_place, 'city_id', city_id)
            new_place.save()
            return jsonify(new_place.to_dict()), 201
    else:
        return jsonify("Missing name"), 400


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    ''' deletes place '''
    value = storage.get('Place', place_id)
    if value is None:
        abort(404)
    place_storage = storage.all('Place')
    for place in place_storage.values():
        if place.id == place_id:
            storage.delete(place)
    return jsonify({}), 200


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    '''updates place object'''
    place_obj = storage.get('Place', place_id)
    if place_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'id' or key != 'created_at' or key != 'updated_at' or\
           key != 'user_id' or key != 'city_id':
            setattr(place_obj, key, value)
    place_obj.save()
    updated_place = place_obj.to_dict()
    return (jsonify(updated_place)), 200
