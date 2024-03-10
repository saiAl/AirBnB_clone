#!/usr/bin/python3

""" 8. First User """
from models.base_model import BaseModel


class User(BaseModel):
    """
        a class User that inherits from BaseModel

        Attribue:
            email (str): empty string
            password (str): empty string
            first_name (str): empty string
            last_name (str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
