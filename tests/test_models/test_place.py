#!/usr/bin/env python3
"""Tests for models/place.py """

import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Test place class."""

    @classmethod
    def setUpClass(self):
        self.obj = Place()

    def test_city_id(self):
        """Test city_id attribute."""
        self.assertEqual(type(self.obj.city_id), str)

    def test_user_id(self):
        """Test user_id attribute."""
        self.assertEqual(type(self.obj.user_id), str)

    def test_name(self):
        """Test name attribute."""
        self.assertEqual(type(self.obj.name), str)

    def test_description(self):
        """Test description attribute."""
        self.assertEqual(type(self.obj.description), str)

    def test_number_rooms(self):
        """Test number_rooms attribute."""
        self.assertEqual(type(self.obj.number_rooms), int)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute."""
        self.assertEqual(type(self.obj.number_bathrooms), int)

    def test_max_guest(self):
        """Test max_guest attribute."""
        self.assertEqual(type(self.obj.max_guest), int)

    def test_price_by_night(self):
        """Test price_by_night attribute."""
        self.assertEqual(type(self.obj.price_by_night), int)

    def test_latitude(self):
        """Test latitude attribute."""
        self.assertEqual(type(self.obj.latitude), float)

    def test_longitude(self):
        """Test longitude attribute."""
        self.assertEqual(type(self.obj.longitude), float)

    def test_amenities(self):
        """Test amenities attribute."""
        self.assertEqual(type(self.obj.amenity_ids), list)
