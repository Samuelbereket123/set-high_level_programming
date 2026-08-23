#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for testing Square class methods."""

    def setUp(self):
        """Reset private object count before each test."""
        Base._Base__nb_objects = 0

    def test_square_1_arg(self):
        """Test Square(1) instantiation."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_2_args(self):
        """Test Square(1, 2) instantiation."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_3_args(self):
        """Test Square(1, 2, 3) instantiation."""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_4_args(self):
        """Test Square(1, 2, 3, 4) instantiation."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_invalid_type_size(self):
        """Test Square('1') raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_invalid_type_x(self):
        """Test Square(1, '2') raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_invalid_type_y(self):
        """Test Square(1, 2, '3') raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_zero_size(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_x(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        """Test __str__() representation for Square."""
        s = Square(5, 2, 1, 7)
        self.assertEqual(str(s), "[Square] (7) 2/1 - 5")

    def test_to_dictionary(self):
        """Test to_dictionary() method in Square."""
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)

    def test_update_no_args(self):
        """Test update() without positional arguments."""
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(s.id, 1)

    def test_update_1_arg(self):
        """Test update(89)."""
        s = Square(5, 0, 0, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_2_args(self):
        """Test update(89, 1)."""
        s = Square(5, 0, 0, 1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_3_args(self):
        """Test update(89, 1, 2)."""
        s = Square(5, 0, 0, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_4_args(self):
        """Test update(89, 1, 2, 3)."""
        s = Square(5, 0, 0, 1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89})."""
        s = Square(5, 0, 0, 1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test update(**{'id': 89, 'size': 1})."""
        s = Square(5, 0, 0, 1)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        """Test update(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square(5, 0, 0, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_id_size_x_y(self):
        """Test update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square(5, 0, 0, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test Square.create(**{'id': 89})."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test Square.create(**{'id': 89, 'size': 1})."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_valid(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_not_exist(self):
        """Test Square.load_from_file() when file does not exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exist(self):
        """Test Square.load_from_file() when file exists."""
        Square.save_to_file([Square(1)])
        output = Square.load_from_file()
        self.assertEqual(len(output), 1)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
