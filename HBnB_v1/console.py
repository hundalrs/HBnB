#!/usr/bin/python3
'''Console Module'''

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classname = {'BaseModel': BaseModel, 'User': User, 'State': State,
             'City': City, 'Amenity': Amenity, 'Place': Place,
             'Review': Review}


class HBNBCommand(cmd.Cmd):
    '''console methods'''

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        '''exit program'''
        print()
        return True

    def do_quit(self, arg):
        '''exit program'''
        return True

    def emptyline(self):
        '''do not execute anything'''
        pass

    def do_create(self, arg):
        '''creates a new instance of a specific class'''
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in classname:
            print("** class doesn't exist **")
        else:
            instance = classname[arg]()
            print(instance.id)
            instance.save()

    def do_show(self, arg):
        '''prints string representation of instance'''
        my_storage = models.storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in classname:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif commands[0] + "." + commands[1] not in my_storage:
            print("** no instance found **")
        else:
            print(my_storage[commands[0] + "." + commands[1]])

    def do_destroy(self, arg):
        '''deletes an instance based on the class and id'''
        my_storage = models.storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in classname:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif commands[0] + "." + commands[1] not in my_storage:
            print("** no instance found **")
        else:
            my_storage.pop(commands[0] + "." + commands[1])
            models.storage.save()

    def do_all(self, arg):
        '''prints all string representation of all instances'''
        final_list = []
        my_storage = models.storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for key, value in my_storage.items():
                final_list.append(value)
            print(final_list)
        elif commands[0] in classname:
            for key, value in my_storage.items():
                if key.partition('.')[0] == commands[0]:
                    final_list.append(value)
            print(final_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        '''updates an instance based on class name and id'''
        my_storage = models.storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in classname:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif commands[0] + "." + commands[1] not in my_storage:
            print("** no instance found **")
        elif len(commands) < 3:
            print("** attribute name missing **")
        elif len(commands) < 4:
            print("** value missing **")
        else:
            key = commands[0] + "." + commands[1]
            commands[3] = commands[3].replace('"', '')
            my_storage[key].__dict__[commands[2]] = commands[3]
            models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
