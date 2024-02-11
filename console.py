#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print()  # Print a newline
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
