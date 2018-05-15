#!/usr/bin/python3
'''module that returns JSON status "OK"'''

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    '''returns JSON status'''
    return (jsonify({'status': 'OK'}))


@app_views.route('/stats')
def stats():
    ''' return number of objects for each class '''
    return jsonify({"amenities": storage.count('Amenity'),
                    "cities": storage.count('City'),
                    "places": storage.count('Place'),
                    "reviews": storage.count('Review'),
                    "states": storage.count('State'),
                    "users": storage.count('User')})
