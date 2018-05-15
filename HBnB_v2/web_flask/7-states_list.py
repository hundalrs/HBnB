#!/usr/bin/python3
''' Starts a Flask web application
    Lists all state in corresponding HTML file in alphabetic order
'''

from flask import Flask
from flask import render_template
from models import storage, classes

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_html():
    '''displays states in html page'''
    state_objs = storage.all(classes["State"])
    state_values = []
    for key, value in state_objs.items():
        state_values.append(value)
    return render_template('7-states_list.html', states=state_values)


@app.teardown_appcontext
def session_closer(session):
    ''' closes session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
