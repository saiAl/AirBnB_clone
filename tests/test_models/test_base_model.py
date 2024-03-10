#!/usr/bin/python3

""" test for models/base_model.py """
import unittest
from models.base_model import BaseModel
import datetime


class testBaseMode(unittest.TestCase):
    """ BaseModel tests """

    @classmethod
    def setUpClass(self):
        """ test class """

        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def test_instance(self):
        """ objects is instance of BaseModel() """
        self.assertTrue(isinstance(self.obj1, BaseModel))
        self.assertTrue(isinstance(self.obj2, BaseModel))
    
    def test_unique_id(self):
        """ instaces have unique IDs """
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_id_is_uuid4(self):
        """ id len == 36 """
        self.assertEqual(len(self.obj1.id), 36)
        self.assertEqual(len(self.obj2.id), 36)

    def test_id_is_str(self):
        """ IDs is a string """
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj2.id, str)
    
    def test_created_at(self):
        """ created_at is an instance of datetime """
        self.assertIsInstance(self.obj1.created_at, datetime.datetime)

    def test_updated_at(self):
        """ updated_at is an instance of datetime """
        self.assertIsInstance(self.obj1.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj2.updated_at, datetime.datetime)
    
    def test_update_at_change(self):
        """ if the updated_at change """
        
        old = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(old, self.obj1.updated_at)
        
        old = self.obj2.updated_at
        self.obj2.save()
        self.assertNotEqual(old, self.obj2.updated_at)

    def test_to_dict_id(self):
        """ id exists """
        
        new_dict = self.obj1.to_dict()
        self.assertIn("id", new_dict)
    
    def test_to_dict_class(self):
        """ __class__ exists """
        
        new_dict = self.obj1.to_dict()
        self.assertIn("__class__", new_dict)

    def test_to_dict_updated_at(self):
        """ updated_at in iso format """
        
        new_dict = self.obj1.to_dict()
        self.assertEqual(new_dict["updated_at"], self.obj1.updated_at.isoformat())

    def test_to_dict_updated_at(self):
        """ created_at in iso format """
        
        new_dict = self.obj1.to_dict()
        self.assertEqual(new_dict["created_at"], self.obj1.created_at.isoformat())

    def test_10(self):
        """ kwargs """
        
        new_obj = BaseModel(**self.obj1.to_dict())
        self.assertTrue(type(new_obj) is BaseModel)
        self.assertTrue(type(new_obj.created_at) is datetime.datetime)
        self.assertTrue(type(new_obj.updated_at) is datetime.datetime)
