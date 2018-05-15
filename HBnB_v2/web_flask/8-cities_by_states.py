#!/usr/bin/python3
''' Starts a Flask web application
    Lists all state in corresponding HTML file in alphabetic order
'''

from flask import Flask
from flask import render_template
from models import storage, classes

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_state_html():
    '''displays cities and states in html page'''
    state_objs = storage.all(classes["State"])
    state_city_val = {}
    for key, value in state_objs.items():
        city_val = value.cities
        state_city_val[value] = city_val
    return render_template('8-cities_by_states.html', sc=state_city_val)


@app.teardown_appcontext
def session_closer(session):
    ''' closes session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
