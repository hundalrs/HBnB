#!/usr/bin/python3
''' Starts a Flask web application
    Lists all state in corresponding HTML file in alphabetic order
'''

from flask import Flask
from flask import render_template
from models import storage, classes

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_html():
    '''displays states in html file'''
    state_objs = storage.all(classes["State"])
    return render_template('9-states.html', state_objs=state_objs,
                           state_list=None)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    '''displays states with id'''
    state_list = []
    state_objs = storage.all(classes["State"])
    key = "State." + str(id)
    if key in state_objs:
        state_list.append(state_objs[key])
    else:
        state_list = None
    return render_template('9-states.html', state_list=state_list,
                           state_objs=None)


@app.teardown_appcontext
def session_closer(session):
    ''' closes session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
