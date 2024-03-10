#!/usr/bin/python3

""" 9. More classes! """
from models.base_model import BaseModel


class Place(BaseModel):
    """
        a class Place that inherit from BaseModel

        Attribute:
            city_id (str): empty string: it will be the City.id
            user_id (str): empty string: it will be the User.id
            name (str): empty string
            description (str): empty string
            number_rooms (int): 0
            number_bathrooms (int): 0
            max_guest (int): 0
            price_by_night (int): 0
            latitude (float): 0.0
            longitude (float): 0.0
            amenity_ids (list): empty list:
                                it will be the list of Amenity.id later

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
