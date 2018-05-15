# AirBnB clone - Web framework

## Synopsis
This project covers:
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

## Requirements for Python scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* The first line of all files should be exactly `#!/usr/bin/python3`
* All files should end with a new line
* A `README.md` at the root of the folder of the project is mandatory
* Code should use the `PEP 8` style (version 1.7.*)
* All files must be executalbe
* All modules should have documentation
* Code should not be executed when imported (by using `if __name__ == "__main__":`)

## Requirements for HTML/CSS files
* All files should end with a new line
* Your code should be W3C compliant and validate with W3C-Validator
* All your CSS files should be in the `styles` folder
* All your images should be in the `images` folder
* You are not allowed to use `!important` or `id`
* All tags must be in uppercase
* No cross browsers

## Environment
The project was tested and compiled on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### __init__.py

Initializes directory as package

### 0-hello_route.py

Script that starts a Flask web application

### 1-hbnb_route.py

Script that starts a Flask web application with the option `strict_slashes=False`

### 2-c_route.py

Script that starts a Flask web application with the option `strict_slashes=False`

* display "C", followed by the value of the `text` variable
* replace underscore symbols with a space

### 3-python_route.py

Script that starts a Flask web application with the option `strict_slashes=False`

* display "C", followed by the value of the `text` variable
* display "Python", followed by the value of the `text` variable
* replace underscore symbols with a space

### 4-number_route.py

Script that starts a Flask web application with the option `strict_slashes=False`

* display "C", followed by the value of the `text` variable
* display "Python", followed by the value of the `text` variable
* replace underscore symbols with a space
* display "n is a number" only if `n` is an integer

### 5-number_template.py, templates/5-number.html

Script that starts a Flask web application with the option `strict_slashes=False`

* display "C", followed by the value of the `text` variable
* display "Python", followed by the value of the `text` variable
* replace underscore symbols with a space
* display "n is a number" only if `n` is an integer
* display a HTML page only if `n` is an integer
  * `H1` tag: "Number: `n`" inside the tag `BODY`

### 6-number_odd_or_even.py, templates/6-number_odd_or_even.html

Script that starts a Flask web application with the option `strict_slashes=False`

* display "C", followed by the value of the `text` variable
* display "Python", followed by the value of the `text` variable
* replace underscore symbols with a space
* display "n is a number" only if `n` is an integer
* display a HTML page only if `n` is an integer
  * `H1` tag: "Number: `n`" inside the tag `BODY`
* display a HTML page only if `n` is an integer
  * `H1` tag: "Number: `n` is `even|odd`" inside the tag `BODY`

### 7-states_list.py, templates/7-states_list.html

* uses `storage` to fetch data from storage engine
* after ach request you must remove the current SQLAlchemy Session
  * method to handle : `@app.teardown_appcontext`
  * calls in this method `storage.close()`
* Routes:
  * `/states_list`: display a HTML page inside `BODY`
    * `H1` tag: "States"
    * `UL` tag: with the list of all `State` objects present in	`DBStorage` soreted by `name`
      * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`

### 8-cities_by_states.py, 8-cities_by_states.html

* uses `storage` to fetch data from storage engine
* to load all cities of a `State`:
  * If storage engine is `DBStorage`, uses `cities` relationship
  * Otherwise, calls the public getter method `cities`
* after each request you must remove the current SQLAlchemy Session
  * method to handle : `@app.teardown_appcontext`
  * calls in this method `storage.close()`
* Routes:
  * `/cities_by_states`: display a HTML page inside `BODY`
    * `H1` tag: "States"
    * `UL` tag: with the list of all `State` objects present in	`DBStorage` soreted by `name`
      * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>` + `UL` tag: with the list of `City` objects linked to the `State` sorted by name
      	* `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`

### 9-states.py, 9-states.html

* uses `storage` to fetch data from storage engine
* to load all cities of a `State`:
  * If storage engine is `DBStorage`, uses `cities` relationship
  * Otherwise, calls the public getter method `cities`
* after each request you must remove the current SQLAlchemy Session
  * method to handle : `@app.teardown_appcontext`
  * calls in this method `storage.close()`
* Routes:
  * `/states`: display a HTML page inside `BODY`
    * `H1` tag: "States"
    * `UL` tag: with the list of all `State` objects present in	`DBStorage` soreted by `name`
      * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
  * `/states/<id>`: display a HTML page inside the `BODY`
    * If a `State` object is found with this `id`:
      * `H1` tag: "State"
      * `H3` tag: "Cities"
      * `UL` tag with the list of `City` objects linked to the `State` sorted by name
      	* `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
    * Otherwise:
      `H1` tag "Not found!"

### 10-hbnb_filters.py, 10-hbnb_filters.html

* uses `storage` to fetch data from storage engine
* to load all cities of a `State`:
  * If storage engine is `DBStorage`, uses `cities` relationship
  * Otherwise, calls the public getter method `cities`
* after each request you must remove the current SQLAlchemy Session
  * method to handle : `@app.teardown_appcontext`
  * calls in this method `storage.close()`
* Routes:
  * `hbnb_filters`: display a HTML page
    * Update `.popover` class to allow scrolling in the popover and a max height of 300 pixels.
    * Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
      * Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities by `&nbsp;`
    * `State, City, and Amenity` objects must be loaded from `DBStorage` and sorted by name