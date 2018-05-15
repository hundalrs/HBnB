#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return 'C %s' % text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
