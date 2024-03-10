#!/usr/bin/python3

"""

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()



def serialize(*args):
    """ """
    import json

    with open(args[0], "w", encoding="utf-8") as f:
        f.write(json.dumps(args[1]))

def deserialize(path):
    """ """
    import json


    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
        return json.loads(data)


def cmd_tokenize(token):
    """
    """

    if token == '':
        return None
    return token.split(' ')


def check_args(arg):
    """ """
    if arg is None:
        print("** class name missing **")
        return None
    elif arg[0] != "BaseModel":
        print("** class doesn't exist **")
        return None
    elif len(arg) == 1:
        print("** instance id missing **")
        return None
    else:
        return arg

