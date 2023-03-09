# TODO 1 ZMIENIĆ assertEquals na assertEqual, bo był jakiś uppdate syntaxu
import unittest

from unittest import TestCase

""" Objects to tests imports"""
from easyvalid_data_validator.datacheckers.array import are_members_of_type, \
    is_array_length_of


class TestAreMembersTypeOf(TestCase):
    def test_when_members_of_one_type(self) -> None:
        """ Why not assertTrue? If func was badly implemented and return any object, object is interpreted as True"""
        self.assertEqual(are_members_of_type([1, 2, 3], int), True)

    def test_when_members_of_multiple_types(self) -> None:
        """ Why not assertFalse? If func was badly implemented and return None, None is interpreted as False"""
        self.assertEqual(are_members_of_type([1, '2', 3], int), False)

    def test_when_desired_type_is_not_class(self):
        with self.assertRaises(TypeError) as e:
            are_members_of_type([1], 1)
            self.assertRegex(e.exception.args[0], r'^Invalid .* argument type$')


class TestIsArrayLengthOf(TestCase):
    def test_when_lengths_match(self) -> None:
        self.assertEqual(is_array_length_of([1], 1), True)

    def test_when_lengths_do_not_match(self) -> None:
        self.assertEqual(is_array_length_of([1], 0), False)


if __name__ == "__main__":
    unittest.main()
