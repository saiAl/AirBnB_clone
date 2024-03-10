#!/usr/bin/python3

""" 9. More classes! """
from models.base_model import BaseModel


class City(BaseModel):
    """
        a class City that inherits from BaseModel

        Attribue:
            state_id (str): empty string
            name (str): empty string
    """

    state_id = ""
    name = ""
