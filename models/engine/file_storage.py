#!/use/bin/python3

""" Store first object """

import json
import os


class FileStorage:
    """
        a class that serializes instances to a JSON file
            and deserializes JSON file to instances.

        Attributes:
            __file_path (str): path to the JSON file.
            __objects (dict): empty but will store all objects
                by <class name>.id.

        Methods:
            all(self) - returns the dictionary __objects.
            new(self, obj) - sets in __objects the obj
                with key <obj class name>.id.
            save(self): serializes __objects to the JSON file.
            reload(self): deserializes the JSON file to __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file """

        data = self.__objects.copy()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for key, value in data.items():
                data[key] = value.to_dict()
            f.write(json.dumps(data))

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        data = self.__objects
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.loads(f.read())
                if data != '':
                    for key, value in data.items():
                        self.new(eval(key.split('.')[0])(**value))
