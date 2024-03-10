#!/usr/bin/env python3
""" tests for models/amenity.py """

import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test amenity class."""

    def test_name(self):
        """Test name attribute."""
        obj = Amenity()
        self.assertEqual(type(obj.name), str)
