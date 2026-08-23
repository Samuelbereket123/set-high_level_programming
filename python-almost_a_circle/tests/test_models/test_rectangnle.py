#!/usr/bin/python3
"""Unittests for Rectangle model."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for testing Rectangle class methods."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_2_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_3_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_4_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_5_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_invalid_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_type_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_type_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_type_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_y(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), d)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(r.id, 1)

    def test_update_1_arg(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_2_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_3_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_4_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_5_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_valid(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_not_exist(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exist(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
