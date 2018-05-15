#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    my_storage = storage.all('State')
    state_list = []
    for key, val in my_storage.items():
        state_list.append(my_storage[key])
    return render_template('9-states.html', state_list=state_list)


@app.route('/states/<id>', strict_slashes=False)
def match_id(id):
    my_storage = storage.all('State')
    my_id = id
    my_key = 'State.' + str(my_id)
    matching_list = []
    for key, val in my_storage.items():
        if my_key == key:
            matching_list.append(my_storage[key])
    return render_template('9-states.html', matching_list=matching_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
