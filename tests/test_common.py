import unittest
from decimal import Decimal
from unittest import TestCase

from easyvalid_data_validator.common import validate_if_arg_is_of_type, validate_if_arg_is_callable, \
    evaluate_numeric_comparison, is_type


class TestValidateIfArgIsOfType(TestCase):
    def test_with_argument_matching_type(self) -> None:
        self.assertEqual(validate_if_arg_is_of_type(1, int, 'num1'), 1)

    def test_with_argument_not_matching_type(self) -> None:
        with self.assertRaises(TypeError) as e:
            validate_if_arg_is_of_type(1, str, 'num1')
            self.assertRegex(e.exception.args[0], r'^Invalid .* argument type$')


class TestValidateIfArgIsCallable(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        def func() -> None:
            pass

        cls.f = func

    def test_with_callable_argument(self):
        self.assertEqual(validate_if_arg_is_callable(self.f, 'f'), self.f)

    def test_with_not_callable_argument(self):
        with self.assertRaises(TypeError) as e:
            validate_if_arg_is_callable(self.f(), 'f')
            self.assertEqual(e.exception.args[0], "f is not callable object")


class TestEvaluate_NumericComparison(TestCase):
    def test_with_all_arguments_valid(self) -> None:
        for value1, value1_type, value2, value2_type, operator_ in [
            (1, int, 2, int, "<"), (1, int, 1, int, "<="), (1, int, 2, int, "<="),
            (2, int, 1, int, ">"), (1, int, 1, int, ">="), (2, int, 1, int, ">="),
            (1, int, 1, int, "=="), (1, int, Decimal('2'), Decimal, "!=")
        ]:
            with self.subTest(value1=value1, value1_type=value1_type, value2=value2, value2_type=value2_type,
                              operator_=operator_):
                self.assertEqual(evaluate_numeric_comparison(value1, value1_type, value2, value2_type, operator_),
                                  True)

    def test_with_comparison_invalid(self) -> None:
        for value1, value1_type, value2, value2_type, operator_ in [
            (1, int, 2, int, ">"), (1, int, 0, int, "<="),
            (2, int, 1, int, "<"), (0, int, 1, int, ">="),
            (1, int, 2, int, "=="), (1, int, 1, int, "!=")
        ]:
            with self.subTest(value1=value1, value1_type=value1_type, value2=value2, value2_type=value2_type,
                              operator_=operator_):
                self.assertEqual(evaluate_numeric_comparison(value1, value1_type, value2, value2_type, operator_),
                                  False)

    def test_when_comparison_operator_is_invalid(self) -> None:
        with self.assertRaises(ValueError) as e:
            evaluate_numeric_comparison(1, int, 2, int, 'equal')
            assert self.assertEqual(e.exception.args[0], 'Invalid comparison operator')

    def test_when_value_has_invalid_type(self) -> None:
        for value1, value1_type, value2, value2_type, operator_ in [('1', int, 1, int, "!="), (1, int, '1', int, "!="),
                                                                    ('1', int, '1', int, "!=")]:
            with self.assertRaises(TypeError) as e:
                evaluate_numeric_comparison(value1, value1_type, value2, value2_type, operator_)
                assert self.assertEqual(e.exception.args[0], 'One or both values have invalid type')


class TestIsType(TestCase):
    def test_when_value_type_match_desired_type(self) -> None:
        self.assertTrue(is_type(1, int))

    def test_when_value_type_doesnt_match_desired_type(self) -> None:
        self.assertFalse(is_type('1', int))

    def test_when_desired_type_is_non_json_type(self) -> None:
        with self.assertRaises(TypeError) as e:
            is_type({}, set)
            self.assertEqual(e.exception.args[0], "Invalid desired_type argument, has to be one of json standard type: int, float, str, list, dict, bool, None")


if __name__ == "__main__":
    unittest.main()
