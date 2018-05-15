#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def cities_list():
    state_storage = storage.all('State')
    amenity_storage = storage.all('Amenity')
    city_list = []
    amenity_list = []
    for key, val in state_storage.items():
        city_list.append(state_storage[key])
    for key, val in amenity_storage.items():
        amenity_list.append(amenity_storage[key])
    return render_template('10-hbnb_filters.html', city_list=city_list, amenity_list=amenity_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
