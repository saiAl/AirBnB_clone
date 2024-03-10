#!/usr/bin/env python3
"""Tests for models/city.py """

import unittest
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """Test city class."""

    def test_name(self):
        """Test name attribute."""
        obj = City()
        self.assertEqual(type(obj.name), str)

    def test_state_id(self):
        """Test state_id attribute."""
        obj = City()
        self.assertEqual(type(obj.state_id), str)
