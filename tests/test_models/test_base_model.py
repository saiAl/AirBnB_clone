#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime

class testBaseMode(unittest.TestCase):
    """ """
    
    def test_unique_id(self):
        """ instaces have unique IDs """
        
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        """ created_at is an instance of datetime """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime.datetime)

    def test_updated_at(self):
        """ updated_at is an instance of datetime """
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime.datetime)
    
    
    def test_update_at_change(self):
        """ check if the updated_at change. """
        
        obj = BaseModel()
        old = obj.updated_at
        obj.save()
        self.assertNotEqual(old, obj.updated_at)

    def test_to_dict_id(self):
        """ if id exists """
        
        obj = BaseModel()
        new_dict = obj.to_dict()
        self.assertIn("id", new_dict)
    
    def test_to_dict_class(self):
        """ if __class__ exists """
        
        obj = BaseModel()
        new_dict = obj.to_dict()
        self.assertIn("__class__", new_dict)

    def test_to_dict_updated_at(self):
        """ if updated_at in iso format """
        
        obj = BaseModel()
        new_dict = obj.to_dict()
        self.assertEqual(new_dict["updated_at"], obj.updated_at.isoformat())

    def test_to_dict_updated_at(self):
        """ if created_at in iso format """
        
        obj = BaseModel()
        new_dict = obj.to_dict()
        self.assertEqual(new_dict["created_at"], obj.created_at.isoformat())

    
    def test_kwargs_not_empty(self):
        """ kwargs not empty """

        obj = BaseModel(name="Ali")
        attr = getattr(obj, "name")
        self.assertEqual("Ali", attr)
    
    def test_kwargs_created_at(self):
        """ created_at in iso format"""
        pass

if __name__ == '__main__':
    unittest.main()
