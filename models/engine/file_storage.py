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

        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """ deserializes the JSON file to __objects """

        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.loads(f.read())
                for key, value in data.items():
                    obj_name = key.split(".")[0]
                    self.new(eval(obj_name)(*value))
