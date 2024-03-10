#!/usr/bin/env python3
""" test for models/user.py """

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test user class."""

    @classmethod
    def setUpClass(self):
        """ test class """
        self.obj1 = User

    def test_email(self):
        """Test email attribute."""
        self.assertEqual(type(self.obj1.email), str)

    def test_password(self):
        """Test password attribute."""
        self.assertEqual(type(self.obj1.password), str)

    def test_first_name(self):
        """Test first_name attribute."""
        self.assertEqual(type(self.obj1.first_name), str)

    def test_last_name(self):
        """Test last_name attribute."""
        self.assertEqual(type(self.obj1.last_name), str)
