#!/usr/bin/env python3
"""Tests for models/state.py"""

import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test class."""

    def test_name(self):
        """Test name attribute."""
        obj1 = State()
        self.assertEqual(type(obj1.name), str)

