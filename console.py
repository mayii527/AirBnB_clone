#!/usr/bin/python3
"""Air BnB console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
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

    def parse(self, arg):
        special_chars = re.search(r"\{(.*?)\}", arg)
        special_chars1 = re.search(r"\[(.*?)\]", arg)
        if special_chars is None:
            if special_chars1 is None:
                return [index.strip(",") for index in split(arg)]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
