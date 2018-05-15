#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    my_storage = storage.all('State')
    city_list = []
    for key, val in my_storage.items():
        city_list.append(my_storage[key])
    return render_template('8-cities_by_states.html', city_list=city_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
