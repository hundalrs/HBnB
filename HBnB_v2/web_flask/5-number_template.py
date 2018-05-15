#!/usr/bin/python3
''' Starts Flask web app and listens on 0.0.0.0 on port 5000
    Renders a template
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Prints message Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Print HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''displays C followed by value of text variable'''
    spaced_text = text.replace('_', ' ')
    return 'C % s' % spaced_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    '''displays Python followed by value of text variable'''
    spaced_text = text.replace('_', ' ')
    return 'Python % s' % spaced_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    '''displays 'n is a number only if n is an integer'''
    return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_display_num(n):
    '''displays HTML page when n is an int'''
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
