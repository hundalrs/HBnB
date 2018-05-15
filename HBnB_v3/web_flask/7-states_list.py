#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    my_storage = storage.all('State')
    state_list = []
    for key, val in my_storage.items():
        state_list.append(my_storage[key])
    return render_template('7-states_list.html', state_list=state_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
