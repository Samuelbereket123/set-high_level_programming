#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for testing Rectangle class methods."""

    def setUp(self):
        """Reset private object count before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_2_args(self):
        """Test Rectangle(1, 2) instantiation."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_3_args(self):
        """Test Rectangle(1, 2, 3) instantiation."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_4_args(self):
        """Test Rectangle(1, 2, 3, 4) instantiation."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_5_args(self):
        """Test Rectangle(1, 2, 3, 4, 5) instantiation."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_invalid_type_width(self):
        """Test Rectangle('1', 2) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_type_height(self):
        """Test Rectangle(1, '2') raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_type_x(self):
        """Test Rectangle(1, 2, '3') raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_type_y(self):
        """Test Rectangle(1, 2, 3, '4') raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        """Test Rectangle(-1, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Test Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Test Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Test Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Test Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area() method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__() representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_y(self):
        """Test display() without x and y."""
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        """Test display() without y."""
        r = Rectangle(2, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        """Test display() with x and y."""
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary() method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), d)

    def test_update_no_args(self):
        """Test update() without positional arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(r.id, 1)

    def test_update_1_arg(self):
        """Test update(89)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_2_args(self):
        """Test update(89, 1)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_3_args(self):
        """Test update(89, 1, 2)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_4_args(self):
        """Test update(89, 1, 2, 3)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_5_args(self):
        """Test update(89, 1, 2, 3, 4)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89})."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test update(**{'id': 89, 'width': 1})."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        """Test update(**{'id': 89, 'width': 1, 'height': 2})."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        """Test update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_id_width_height_x_y(self):
        """Test update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test Rectangle.create(**{'id': 89})."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1})."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_valid(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_not_exist(self):
        """Test Rectangle.load_from_file() when file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exist(self):
        """Test Rectangle.load_from_file() when file exists."""
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
