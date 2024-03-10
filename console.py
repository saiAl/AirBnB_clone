#!/usr/bin/python3

""" Console 0.0.1 """

import cmd
import json
import os
from models import storage, deserialize, cmd_tokenize, check_args, serialize
from models.base_model import BaseModel


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

    prompt = '(HBNB) '

    def do_quit(self, line):
        """ command to exit the program """
        quit()
    
    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """ end-of-file marker """
        return True

    def emptyline(self):
        """ overwrite the defualt behaviour """
        pass

    def do_create(self, arg):
        """
            create a new instance of BaseModel
                Ex: create BAseModel
        """
        
        if arg is None:
            print("** class name missing **")
        if arg != "BaseModel":
            print("** class doesn't exist **")
        
        instance = BaseModel()
        instance.save()
        print(instance.id)

    def help_create(self):
        """ print help message for do_create method """

        print("""Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id.
            Ex: create BaseModel""")


    def do_show(self, line):
        """
            Prints the string representation
            of an instance based on the class name and id
        """
         
        new = cmd_tokenize(line)
        
        try:
            class_name, class_id = check_args(new)
            if os.path.isfile("file.json"):
                data = deserialize("file.json")
                for key, value in data.items():
                    if class_id == key.split('.')[1]:
                        print(f"[{key.split('.')[0]}] ({key.split('.')[1]}) {value}")
                        break
                else:
                    print("** no instance found **")
        except Exception:
            pass

    def help_show(self):
        """ print help message for do_show method """
        
        print("""Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.""")


    def do_all(self, line):
        """ """
        
        instances = []
        new = cmd_tokenize(line)

        if os.path.isfile("file.json"):
            data = deserialize("file.json")
            if new is None or new[0] == "BaseModel":
                for key, value in data.items():
                    instances.append(f"[{key.split('.')[0]}] ({key.split('.')[1]}) {value}")
                print(instances)
            elif new[0] != "BaseModel":
                print("** class doesn't exist **")

    def help_all(self):
        """ """
        pass


    def do_destroy(self, line):
        """ Deletes an instance """
       
        new = cmd_tokenize(line)
        
        try:
            class_name, class_id = check_args(new)
            if os.path.isfile("file.json"):
                data = deserialize("file.json")
            
                for key, value in data.items():
                    if class_id == key.split('.')[1]:
                        del data[key]
                        break
                else:
                    print("** no instance found **")

            serialize("file.json", data)
        except Exception:
            pass

        
    def help_destroy(self):
        print("""Deletes an instance based on the class name and id
        Ex: $ destroy BaseModel 1234-1234-1234.""")


    def do_update(self, line):

        new = cmd_tokenize(line)
        try:
            class_name, class_id = check_args(new)
            attr_key = "first_name"
            attr_value = "ali"

            if os.path.isfile("file.json"):
                data = deserialize("file.json")
                for key, value in data.items():
                    if class_id == key.split('.')[1]:
                        data[key].update({attr_key: attr_value})
                        break
                else:
                    print("** no instance found **")
                serialize("file.json", data)
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
