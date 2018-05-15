#!/usr/bin/python3
'''view for Place'''

from api.v1.views import app_views
from flask import Blueprint, jsonify, abort, request
from models import storage
import json
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def all_places_reviews(place_id):
    ''' list all places in json format '''
    place_obj = storage.get('Place', place_id)
    if place_obj is None:
        abort(404)
    stored_reviews = storage.all('Review').values()
    review_list = []
    for review in stored_reviews:
        review_dict = review.to_dict()
        if review.place_id == place_id:
            review_list.append(review_dict)
    return jsonify(review_list)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def find_review(review_id):
    ''' match review_id to review '''
    review_obj = storage.get('Review', review_id)
    if review_obj is None:
        abort(404)
    return jsonify(review_obj.to_dict())


@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def post_review(place_id):
    '''POST Review'''
    place_obj = storage.get('Place', place_id)
    if place_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify("Not a JSON"), 400
    if 'user_id' not in data:
        return jsonify("Missing user_id"), 400
    if 'text' in data:
        value = storage.get('User', data['user_id'])
        if value is None:
            abort(404)
        if value is not None:
            new_review = Review(**data)
            setattr(new_review, 'place_id', place_id)
            new_review.save()
            return jsonify(new_review.to_dict()), 201
    else:
        return jsonify("Missing text"), 400


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    ''' deletes review '''
    value = storage.get('Review', review_id)
    if value is None:
        abort(404)
    review_storage = storage.all('Review')
    for review in review_storage.values():
        if review.id == review_id:
            storage.delete(review)
    return jsonify({}), 200


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    '''updates review object'''
    review_obj = storage.get('Review', review_id)
    if review_obj is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify('Not a JSON'), 400
    for key, value in data.items():
        if key != 'id' or key != 'created_at' or key != 'updated_at' or\
           key != 'user_id' or key != 'place_id':
            setattr(review_obj, key, value)
    review_obj.save()
    updated_review = review_obj.to_dict()
    return (jsonify(updated_review)), 200
