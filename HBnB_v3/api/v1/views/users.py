#!/usr/bin/python3
'''view for State'''

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
import json
from models.user import User


@app_views.route('/users', methods=['GET'])
def all_users():
    ''' list all amenities in json format '''
    stored_users = storage.all('User').values()
    user_list = []
    for user in stored_users:
        users_dict = user.to_dict()
        user_list.append(users_dict)
    return jsonify(user_list)


@app_views.route('/users', methods=['POST'])
def post_user():
    '''transforms http body request to a dictionary'''
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'email' in data and 'password' in data:
        new_user = User(**data)
        new_user.save()
        return jsonify(new_user.to_dict()), 201
    else:
        if 'email' not in data:
            return jsonify("Missing email"), 400
        elif 'password' not in data:
            return jsonify('Missing password'), 400


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE'])
def delete_user(user_id):
    ''' delete user and match to user_id'''
    value = storage.get('User', user_id)
    if request.method == 'DELETE':
        if value is None:
            abort(404)
        user_storage = storage.all('User')
        for user in user_storage.values():
            if user.id == user_id:
                storage.delete(user)
        return jsonify({}), 200
    if value is None:
        abort(404)
    return jsonify(value.to_dict()), 200


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    '''updates user object'''
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'id' or key != 'email'\
                or key != 'created_at' or key != 'updated_at':
            setattr(user_obj, key, value)
    user_obj.save()
    updated_user = user_obj.to_dict()
    return (jsonify(updated_user)), 200
