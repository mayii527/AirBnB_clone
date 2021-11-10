#!/usr/bin/python3
"""Air BnB console."""
import cmd
import re

class HBNBCommand(cmd.Cmd):
    """Define the air bnb command interpreter

    """
    prompt = "(hbnb) "
    def emptyline(self):
        """Define a function to handle empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
