#!/usr/bin/python3

""" 9. More classes! """
from models.base_model import BaseModel


class Review(BaseModel):
    """
        a class Review that inherit from BaseModel

        Attribute:
            place_id (str): empty string
            user_id (str): empty string
            text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
