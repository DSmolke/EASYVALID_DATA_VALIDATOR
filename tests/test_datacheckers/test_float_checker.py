import unittest

from unittest import TestCase

from easyvalid_data_validator.datacheckers.float_checker import is_float_in_range, is_float_lower_than, is_float_le_than, is_float_equal, is_float_not_equal, is_float_grater_than, is_float_ge_than


class TestIsInRange(TestCase):
    """ Cases when function parameters are of invalid type are covered by auxiliary function validate_if_arg_is_of_type """

    def test_when_value_in_range(self) -> None:
        for value, r_min, r_max in [(1.0, 0.0, 2.0), (1.0, 1.0, 2.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0)]:
            with self.subTest(value=value, r_min=r_min, r_max=r_max):
                self.assertTrue(is_float_in_range(value, r_min, r_max))

    def test_when_value_not_in_range(self) -> None:
        for value, r_min, r_max in [(1.0, 2.0, 3.0), (1.0, -1.0, 0.0)]:
            with self.subTest(value=value, r_min=r_min, r_max=r_max):
                self.assertFalse(is_float_in_range(value, r_min, r_max))


class TestIsFloatLowerThan(TestCase):
    def test_when(self) -> None:
        self.assertTrue(is_float_lower_than(1.0, 2.0))

    def test_when_not(self) -> None:
        self.assertFalse((is_float_lower_than(1.0, 1.0)))


class TestIsFloatLeThan(TestCase):
    def test_when(self) -> None:
        self.assertTrue((is_float_le_than(1.0, 1.0)))

    def test_when_not(self) -> None:
        self.assertFalse((is_float_le_than(1.0, 0.99)))


class TestIsFloatEqual(TestCase):
    def test_when(self) -> None:
        self.assertTrue((is_float_equal(1.0, 1.0)))

    def test_when_not(self) -> None:
        self.assertFalse((is_float_equal(1.0, 1.00001)))


class TestIsFloatNotEqual(TestCase):
    def test_when(self) -> None:
        self.assertTrue(is_float_not_equal(1.0, 1.00001))

    def test_when_not(self) -> None:
        self.assertFalse(is_float_not_equal(1.0, 1.0))


class TestIsFloatGraterThan(TestCase):
    def test_when(self) -> None:
        self.assertTrue(is_float_grater_than(1.0, 0.0))

    def test_when_not(self) -> None:
        self.assertFalse(is_float_grater_than(0.0, 0.0))


class TestIsFloatGeThan(TestCase):
    def test_when(self) -> None:
        self.assertTrue(is_float_ge_than(1.0, 1.0))

    def test_when_not(self) -> None:
        self.assertFalse(is_float_ge_than(1.0, 1.1))


if __name__ == "__main__":
    unittest.main()
