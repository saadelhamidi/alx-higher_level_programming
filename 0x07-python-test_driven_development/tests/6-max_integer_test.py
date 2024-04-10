#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_beginning(self):
        """max at the beginning
        """
        self.assertEqual(max_integer([98, 1, 4, 3]), 98)

    def test_max_at_the_missle(self):
        """max in the middle
        """
        self.assertEqual(max_integer([1, 2, 98, 3]), 98)

    def test_max_at_the_end(self):
        """max at the end
        """
        self.assertEqual(max_integer([2, 1, 4, 98]), 98)

    def test_one_num_is_negative_(self):
        """one number is negative
        """
        self.assertEqual(max_integer([6, 98, -4, 3]), 98)

    def test_all_nums_are_negative(self):
        """all numbers are negative
        """
        self.assertEqual(max_integer([-98, -1, -4, -3]), -1)

    def test_negative_and_zero(self):
        """test negative number vs zero
        """
        self.assertEqual(max_integer([0, -1]), 0)

    def test_one_number_in_list(self):
        """list contain one number
        """
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """empty list should return None
        """
        self.assertEqual(max_integer([]), None)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        with self.assertRaises(TypeError):
            max_integer(["1", 3, 9])

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError
        """
        with self.assertRaises(TypeError):
            max_integer(7)

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_strings(self):
        """Test with a list of strings: should return the first string
        """
        self.assertEqual(max_integer(["alx", "School"]), "alx")

    def test_float(self):
        """test list with floats
        """
        self.assertEqual(max_integer([1.0, 1.2, 1.3]), 1.3)


if __name__ == "__main__":
    unittest.main()
