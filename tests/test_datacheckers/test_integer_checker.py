import unittest
from unittest import TestCase

from easyvalid_data_validator.datacheckers.integer_checker import is_in_range, is_lower_than


class TestIsInRange(TestCase):
    """ Cases when function parameters are of invalid type are covered by auxiliary function validate_if_arg_is_of_type """

    def test_when_value_in_range(self) -> None:
        for value, r_min, r_max in [(1, 0, 2), (1, 1, 2), (1, 0, 1), (1, 1, 1)]:
            with self.subTest(value=value, r_min=r_min, r_max=r_max):
                self.assertTrue(is_in_range(value, r_min, r_max))

    def test_when_value_not_in_range(self) -> None:
        for value, r_min, r_max in [(1, 2, 3), (1, -1, 0)]:
            with self.subTest(value=value, r_min=r_min, r_max=r_max):
                self.assertFalse(is_in_range(value, r_min, r_max))


class TestIsLowerThan(TestCase):
    """ Cases when function parameters are of invalid type are covered by auxiliary function validate_if_arg_is_of_type """

    def test_when_value_lower(self) -> None:
        self.assertTrue(is_lower_than(1, 2))

    def test_when_value_ge(self) -> None:
        value = 1
        for compare_value in [1, 0, -1]:
            with self.subTest(compare_value=compare_value):
                self.assertFalse(is_lower_than(value, compare_value))


if __name__ == "__main__":
    unittest.main()
