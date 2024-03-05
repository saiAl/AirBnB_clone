#!/usr/bin/python3
''' 3. BaseModel '''

from uuid import uuid4
from datetime import datetime


class BaseModel():
    '''
        BaseModel class that defines all common
            attributes/methods for other classes.

        Attributes:
            id (str): assign with an uuid when an instance is created.
            created_at (str): datetime - assign with the current datetime
                when an instance is created.
            updated_at (str): datetime - assign with the current datetime
                when an instance is created and it will be updated every
                time you change your object.

        Methods:
            __init__ - special method to initilize instances
                with public attributes.
            __str__ - special method that return custom string.
            save - updates the public instance attribute updated_at
                with the current datetime.
            to_dict - returns a dictionary containing all keys/values
                of __dict__ of the instance.
    '''

    def __init__(self, *args, **kwargs):
        '''
            initilize instances with public attributes.

            Attributes:
                id (str): assign with an uuid when an instance is created.
                created_at (str): datetime - assign with the current datetime
                    when an instance is created.
                updated_at (str): datetime - assign with the current datetime
                    when an instance is created and it will be updated every
                    time you change your object.

        '''

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            special method that return custom string.

            Returns: string [<class name>] (<self.id>) <self.__dict__>

        """
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        """
            updates updated_at with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
                of __dict__ of the instance.

            Returns:
                dicitonary contain all self.__dict__
                key __class__ with class name as its value
                created_at and updated_at converted to string object
                    in ISO format: %Y-%m-%dT%H:%M:%S.%f
        """

        new = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new.update({key: value.strftime("%Y-%m-%dT%H:%M:%S.%f")})
            else:
                new.update({key: value})
        new.update({"__class__": self.__class__.__name__})
        return new
