#!/usr/bin/env python3
"""Tests for models/review.py """

import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test review class."""

    def test_place_id(self):
        """Test place_id attribute."""
        obj = Review()
        self.assertEqual(type(obj.place_id), str)

    def test_user_id(self):
        """Test user_id attribute."""
        obj = Review()
        self.assertEqual(type(obj.user_id), str)

    def test_text(self):
        """Test text attribute."""
        obj = Review()
        self.assertEqual(type(obj.text), str)
