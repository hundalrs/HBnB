#!/usr/bin/python3
'''view for State'''

from api.v1.views import app_views
from flask import Blueprint, jsonify, abort, request
from models import storage
import json
from models.state import State


@app_views.route('/states', methods=['GET'])
def all_states():
    ''' list all states in json format '''
    stored_states = storage.all('State').values()
    states_list = []
    for state in stored_states:
        state_dict = state.to_dict()
        states_list.append(state_dict)
    return jsonify(states_list)


@app_views.route('/states', methods=['POST'])
def post_state():
    '''transforms http body request to a dictionary'''
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'name' in data:
        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201
    else:
        return jsonify("Missing name"), 400


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    ''' retrieves state if not linked to object'''
    value = storage.get('State', state_id)
    if request.method == 'DELETE':
        if value is None:
            abort(404)
        state_storage = storage.all('State')
        for state in state_storage.values():
            if state.id == state_id:
                storage.delete(state)
        return jsonify({}), 200
    if value is None:
        abort(404)


@app_views.route('/states/<state_id>', methods=['GET'])
def retrieve_state(state_id):
    '''retrieves state if not linked to object'''
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    else:
        return jsonify(state_obj.to_dict())


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    '''updates state object'''
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'id' or key != 'created_at' or key != 'updated_at':
            setattr(state_obj, key, value)
    state_obj.save()
    updated_state = state_obj.to_dict()
    return (jsonify(updated_state)), 200
