#!/usr/bin/python3
"""Unittests for Base model."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for testing Base class methods."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test Base() auto id assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_auto_id_increment(self):
        """Test Base() auto id increment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test Base(89) custom id assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string([{'id': 12}])."""
        d = [{'id': 12}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        """Test to_json_string returns a string type."""
        d = [{'id': 12}]
        res = Base.to_json_string(d)
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        """Test from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string('[]')."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test from_json_string('[{"id": 89}]')."""
        s = '[{"id": 89}]'
        self.assertEqual(Base.from_json_string(s), [{'id': 89}])

    def test_from_json_string_returns_list(self):
        """Test from_json_string returns a list type."""
        s = '[{"id": 89}]'
        res = Base.from_json_string(s)
        self.assertIsInstance(res, list)


if __name__ == '__main__':
    unittest.main()
