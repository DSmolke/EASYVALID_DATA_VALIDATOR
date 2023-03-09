import unittest
from decimal import Decimal
from unittest import TestCase

from easyvalid_data_validator.datacheckers.string import matches_regex, is_decimal_string


class TestMatchingRegex(TestCase):
    def test_for_expression_matching_regex(self):
        self.assertTrue(matches_regex('ABC', r'^ABC$'))

    def test_for_expression_not_matching_regex(self):
        self.assertFalse(matches_regex('123', r'^12$'))

    def test_for_invalid_expression_type(self):
        for i in [(1,), (1.1,), ((1,),), ([1],), (Decimal("1"),)]:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as e:
                    matches_regex(i, r'^1$')
                    self.assertEqual(e.exception.args[0], f"Invalid expression type: {type(i)}")

    def test_for_invalid_regex_type(self):
        for i in [(1,), (1.1,), ((1,),), ([1],), (Decimal("1"),)]:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as e:
                    matches_regex('expression', i)
                    self.assertEqual(e.exception.args[0], f"Invalid expression type: {type(i)}")


class TestIsDecimalString(TestCase):
    """ Cases where provided argument or regex_validator have invalid type are covered by auxiliary functions"""
    def test_with_valid_argument(self):
        for d in ('0', '0.0', '.01', '-1.1'):
            with self.subTest(d=d):
                self.assertEqual(is_decimal_string(d), True)

    def test_with_invalid_argument(self):
        for d in ['--0', '1.1.1', 'b', '-.1.1']:
            with self.subTest(d=d):
                self.assertEqual(is_decimal_string(d), False)


if __name__ == "__main__":
    unittest.main()
