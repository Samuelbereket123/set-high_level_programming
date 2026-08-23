#!/usr/bin/python3
"""Unittests for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for testing the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test auto-incrementing id when no id is passed."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_custom_value(self):
        """Test assigning explicit custom id."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_mix_custom_and_auto(self):
        """Test combination of custom id and auto-increment."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_negative(self):
        """Test with negative integer id."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_zero(self):
        """Test with zero id."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_too_many_arguments(self):
        """Test passing more than one argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
