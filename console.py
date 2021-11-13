#!/usr/bin/python3
"""Air BnB console."""
import cmd
import shlex
import models
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    """Define the air bnb command interpreter."""

    prompt = "(hbnb) "

    __classes = [
        "BaseModel", "User", "State",
        "City", "Place", "Amenity", "Review"]

    def emptyline(self):
        """Define a function to handle empty line."""
        pass

    def do_quit(self, arg):
        """Define a function to quit the program."""
        return True

    def do_EOF(self, arg):
        """Define a function to EOF signal."""
        print("")
        return True

    def do_create(self, arg):
        """Create a class instance"""
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            print(eval(arg_parse[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print a string with the class representation"""
        object_dictionary = storage.all()
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_parse) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_parse[0], arg_parse[1]) not in object_dictionary:
            print("** no instance found **")
        else:
            print(object_dictionary["{}.{}".format(arg_parse[0], arg_parse[1])])

    def do_destroy(self, arg):
        """Destroy a class instance"""
        object_dictionary = storage.all()
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_parse) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_parse[0], arg_parse[1]) not in object_dictionary:
            print("** no instance found **")
        else:
            del object_dictionary["{}.{}".format(arg_parse[0], arg_parse[1])]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
