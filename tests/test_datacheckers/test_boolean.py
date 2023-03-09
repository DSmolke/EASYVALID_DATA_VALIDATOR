import unittest

from unittest import TestCase

from easyvalid_data_validator.datacheckers.boolean import is_true, is_false

class TestIsTrue(TestCase):
    def test_when_valid_value(self) -> None:
        self.assertTrue(is_true(True))

    def test_when_invalid_value(self) -> None:
        self.assertFalse(is_true(False))

class TestIsFalse(TestCase):
    def test_when_valid_value(self) -> None:
        self.assertTrue(is_false(False))

    def test_when_invalid_value(self) -> None:
        self.assertFalse(is_false(True))


if __name__ == "__main__":
    unittest.main()
