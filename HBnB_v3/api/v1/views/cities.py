#!/usr/bin/python3
'''view for State'''

from api.v1.views import app_views
from flask import Blueprint, jsonify, abort, request
from models import storage
import json
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def city_states(state_id):
    ''' list all states in json format '''
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    stored_cities = storage.all('City').values()
    city_list = []
    for city in stored_cities:
        city_dict = city.to_dict()
        if city.state_id == state_id:
            city_list.append(city_dict)
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'])
def find_city(city_id):
    ''' match city_id to city '''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404)
    return jsonify(city_obj.to_dict())


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def post_city(state_id):
    '''POST City'''
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'name' in data:
        new_city = City(**data)
        setattr(new_city, 'state_id', state_id)
        new_city.save()
        return jsonify(new_city.to_dict()), 201
    else:
        return jsonify("Missing name"), 400


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    ''' deletes city '''
    value = storage.get('City', city_id)
    if value is None:
        abort(404)
    city_storage = storage.all('City')
    for city in city_storage.values():
        if city.id == city_id:
            storage.delete(city)
    return jsonify({}), 200


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    '''updates state object'''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'state_id' or key != 'created_at' or key != 'updated_at':
            setattr(city_obj, key, value)
    city_obj.save()
    updated_city = city_obj.to_dict()
    return (jsonify(updated_city)), 200
