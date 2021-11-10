#!/usr/bin/python3
"""Air BnB console."""
import cmd
import re

class HBNBCommand(cmd.Cmd):
    """Define the air bnb command interpreter."""
    prompt = "(hbnb) "
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
