#!/usr/bin/python3

""" Console 0.0.1 """

import cmd


class HBNBCommand(cmd.Cmd):
    """
        entry point of the command interpreter

        Attributes:
            prompt (str): a custom promp.

        Methods:
            do_quit - exit the program
            do_EOF - end of file CTRL-D
            do_help - show help page to end user.


    """

    prompt = '(HBNB)'

    def do_quit(self, line):
        """ Quit command to exit the program """
        quit()

    def do_EOF(self, line):
        """ end-of-file marker """
        return True

    def emptyline(self):
        """ overwritten defualt behaviour """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
