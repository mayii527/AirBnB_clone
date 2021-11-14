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
        object_dict = storage.all()
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_parse) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_parse[0], arg_parse[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(arg_parse[0], arg_parse[1])])

    def do_destroy(self, arg):
        """Destroy a class instance"""
        object_dict = storage.all()
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_parse) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_parse[0], arg_parse[1]) not in object_dict:
            print("** no instance found **")
        else:
            del object_dict["{}.{}".format(arg_parse[0], arg_parse[1])]
            storage.save()

    def do_all(self, arg):
        """Print all instances"""
        arg_parse = shlex.split(arg)
        if len(arg) == 0:
            obj_list = []
            models.storage.reload()
            for index, objects in models.storage.all().items():
                obj_list.append(objects.__str__())
            print(obj_list)
        elif arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            models.storage.reload()
            for index, objects in models.storage.all().items():
                if objects.__class__.__name__ == arg_parse[0]:
                    obj_list.append(objects.__str__())
                print(obj_list)

    def do_update(self, arg):
        """Update a class instance with a id"""
        arg_parse = shlex.split(arg)
        if len(arg_parse) == 0:
            print("** class name missing **")
            return False
        if arg_parse[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_parse) == 1:
            print("** instance id missing **")
            return False
        else:
            models.storage.reload()
            object_dict = models.storage.all()
            for index, objects in object_dict.items():
                if objects.id == arg_parse[1] and \
                        objects.__class__.__name__ == arg_parse[0]:
                    if len(arg_parse) == 2:
                        print("** attribute name missing **")
                        return False
                    elif len(arg_parse) == 3:
                        print("** value missing **")
                        return False
                    else:
                        new_attribute = arg_parse[3]
                        if hasattr(objects, str(arg_parse[2])):
                            new_attribute = \
                                type(objects.__class__.__dict__[arg_parsel[2]])
                        objects.__dict__[arg_parse[2]] = new_attribute
                        models.storage.save()
                        return
            print("** no instance found **")

    def do_count(self, arg):
        """count the instances of a class"""
        arg_parse = shlex.split(arg)
        aux = 0
        if not arg:
            return
        for objects in storage.all().values():
            if arg_parse[0] == objects.__class__.__name__:
                aux += 1
        print(aux)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
