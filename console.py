#!/usr/bin/python3

""" Console 0.0.1 """

import cmd
import json
import os
from models import storage, deserialize, cmd_tokenize, check_args, serialize
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        entry point of the command interpreter

        Attributes:
            prompt (str): a custom promp.
            _classes (list): list contain all the classes name.

        Methods:
            do_quit - Exit the program.
            do_EOF - End of file CTRL-D.
            do_help - Show help page to end user.
            do_create - Creates a new instances and saves it
                    (to the JSON file).
            do_show - Prints the string representation of an instance.
            do_destroy - Deletes an instance.
            do_all - Prints all string representation of all instances.
            do_update - Updates an instance

    """

    prompt = '(HBNB) '
    _classes = ["BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"]

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

    def do_create(self, *args):
        """
            create a new instance of BaseModel
                Ex: create BAseModel
        """

        if args[0] == '':
            print("** class name missing **")
        elif args[0] != '' and args[0] not in self._classes:
            print("** class doesn't exist **")
        else:
            def create_instances(idx):
                """ handle the instances creatation """

                if idx == 0:
                    instance = BaseModel()
                if idx == 1:
                    instance = User()
                if idx == 2:
                    instance = State()
                if idx == 3:
                    instance = City()
                if idx == 4:
                    instance = Amenity()
                if idx == 5:
                    instance = Place()
                if idx == 6:
                    instance = Review()
                return instance

            instance = create_instances(self._classes.index(args[0]))
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

    def do_all(self, *args):
        """ Prints all string representation of all instances """

        instances = []

        if os.path.isfile("file.json"):
            data = deserialize("file.json")
        try:
            if args[0] != '' and args[0] not in self._classes:
                print("** class doesn't exist **")

            for key, value in data.items():
                if args[0] != '' and args[0] in self._classes:
                    if key.split('.')[0] == args[0]:
                        instances.append(f"[{key.split('.')[0]}] ({key.split('.')[1]}) {value}")
                if args[0] == '':
                    instances.append(f"[{key.split('.')[0]}] ({key.split('.')[1]}) {value}")
            print(instances)
        except Exception:
            pass

    def help_all(self):
        """ print help message fro all() method """

        print("""Prints all string representation
        of all instances based or not on the class name.\n
        Ex: $ all BaseModel or $ all.  """)

    def do_destroy(self, *args):
        """ Deletes an instance """

        new = cmd_tokenize(args[0])
        if new is None:
            print("** class name missing **")
        if new is not None:
            if len(new) >= 1:
                if new[0] not in self._classes:
                    print("** class doesn't exist **")
                elif new[0] in self._classes and len(new) != 2:
                    print("** instance id missing **")
                else:
                    class_name, class_id = new
                    if os.path.isfile("file.json"):
                        data = deserialize("file.json")
                        for key, value in data.items():
                            if class_name == key.split('.')[0]:
                                if class_id == key.split('.')[1]:
                                    del data[key]
                                    break
                        else:
                            print("** no instance found **")

                        serialize("file.json", data)

    def help_destroy(self):
        """ print help message of destroy() method """

        print("""Deletes an instance based on the class name and id
        Ex: $ destroy BaseModel 1234-1234-1234.""")

    def do_update(self, line):
        """ Updates an instance based on the class name and id """

        new = cmd_tokenize(line)
        if new is None:
            print("** class name missing **")
        if new is not None:
            if len(new) == 1:
                if new[0] not in self._classes:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(new) == 2:
                print("** attribute name missing **")
            elif len(new) == 3:
                print("** value missing **")
            else:
                class_name, class_id, attr_name, attr_value = new
                if os.path.isfile("file.json"):
                    data = deserialize("file.json")
                    for key, value in data.items():
                        if class_name == key.split('.')[0]:
                            if class_id == key.split(".")[1]:
                                data[key].update({attr_name: str(attr_value)})
                                break
                    else:
                        print("** no instance found **")

                    serialize("file.json", data)

    def help_destroy(self):
        """ help message of update() method """

        print("""Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
