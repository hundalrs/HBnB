# AirBnB Clone - The Console
This is the first part of Holberton School's AirBnb clone project that covers concepts we have learned in the higher level programming track so far. A command interpreter is created in this part of the project to manage objects for Holberton's AirBnB Clone project


## Installation
* Clone this repository with this command: ```https://github.com/hundalrs/AirBnB_clone.git```
* Access directory: ```cd AirBnb_clone```
* Run hbnb: ```./console.py``` and enter command

## Console
Example of use:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
9d371689-62c5-466b-ba86-c3c9010097dd
(hbnb) show BaseModel 9d371689-62c5-466b-ba86-c3c9010097dd
[BaseModel] (9d371689-62c5-466b-ba86-c3c9010097dd) {'created_at': datetime.datetime(2018, 2, 15, 7, 2, 3, 340726), 'id': '9d371689-62c5-466b-ba86-c3c9010097dd', 'updated_at': datetime.datetime(2018, 2, 15, 7, 2, 3, 419721)}
(hbnb) destroy BaseModel 9d371689-62c5-466b-ba86-c3c9010097dd
(hbnb) show BaseModel 9d371689-62c5-466b-ba86-c3c9010097dd
** no instance found **
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

# File Descriptions
* ```console.py``` - Contains the entry point of the command interpreter. The command capabilites are as follows.
  * ```quit```: exits console
  * ```create```: Creates a new instance of BaseModel, saves it to JSON file, and prints the id.
  * ```destroy```: Deletes an instance based on class name and id
  * ```show```: prints string representation of an instance
  * ```all```: prints all string representation of all instance based on class name
  * ```update```: updates an instance by adding or updating attribute

```models/``` directory contains:
* ```base_model.py```: The BaseModel class that all other classes inherit from
  * ```def __init__(self, *args, **kwargs)```: initialization of base model
  * ```def __str__(self)```: string representation of BaseModel class
  * ```def save(self)```: updates attribute updated_at with current datetime
  * ```def to_dict(self)```: returns a dictionary containing all keys and values of instance
  
* Classes that inherit from BaseModel
  * ```amenity.py```: Defines available amentities
  * ```city.py```: Defines name of city and state id
  * ```user.py```: Defines user attributes, email, password, first and last name
  * ```state.py```: Defines state name
  * ```review.py```: Defines place id, user id, and test description
  * ```place.py```: Defines price, city id, number of rooms

```/models/engine``` directory contains file storage class that handles JSON Serialization and Deserialization
* ```file_storage.py```: Serializes instances to a Json file & deserializes back to instances

# Bugs
No known bugs

# Testing
This code can be unit tested by running ```python3 -m unittest discover tests```


# Authors
**Daniel Ojeda** [Twitter](https://twitter.com/DanielC_Ojeda) | [Github](https://github.com/Danielo814)
**Raman Hundal** [Twitter](https://twitter.com/rshundal11) | [Github](https://github.com/hundalrs)