import unittest

from unittest import TestCase

from easyvalid_data_validator.constraints import Constraint
from easyvalid_data_validator.validator import _validate_json_dict_member, validate_json_data


class TestValidateJsonDictMember(TestCase):
    def test_expected_errors(self) -> None:
        """ keys are letters from A to L"""
        keys = [chr(i) for i in range(65, 65 + 12)]
        values = [
            "ABC",
            "ABC",
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            [1, 1],
            [1],
            {'A': 1}
        ]
        data_with_all_invalid_values = dict(zip(keys, values))

        ordered_constraints = [
            {Constraint.STRING_REGEX: r'^\d$'},
            {Constraint.STRING_IS_DECIMAL: None},
            {Constraint.INT_BETWEEN: (2, 3)},
            {Constraint.INT_LOWER: 0},
            {Constraint.INT_LE: 0},
            {Constraint.INT_GRATER: 2},
            {Constraint.INT_GE: 2},
            {Constraint.INT_EQUAL: 2},
            {Constraint.INT_NOT_EQUAL: 1},
            {Constraint.ARRAY_MEMBERS_TYPE: str},
            {Constraint.ARRAY_IS_LENGTH_OF: 2},
            {Constraint.DICT_HAS_SAME_KEYS: {'B'}},
        ]

        for i in range(0, 12):
            with self.subTest(iteration=i):
                self.assertNotEqual(
                    _validate_json_dict_member(keys[i], ordered_constraints[i], data_with_all_invalid_values), [])

    def test_with_non_existing_constraint_object(self) -> None:
        with self.assertRaises(ValueError) as e:
            _validate_json_dict_member('A', {'Constraint.MEAN': 1}, {'A': 1})
            self.assertEqual(e.exception.args[0], "Invalid constraint name")

    def test_with_invalid_key(self) -> None:
        with self.assertRaises(KeyError) as e:
            _validate_json_dict_member('B', {Constraint.INT_GE: 1}, {'A': 1})
            self.assertEqual(e.exception.args[0], "Invalid key")


class TestValidateJsonData(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_arguments = {
            'data': {
                'name': 'ADAM',
                'age': 18,
                'preferences': [1, 2, 3]
            },
            'constraints': {
                'name': {Constraint.STRING_REGEX: r'^[A-Z]+$'},
                'age': {Constraint.INT_GE: 18},
                'preferences': {Constraint.ARRAY_MEMBERS_TYPE: int, Constraint.ARRAY_IS_LENGTH_OF: 3}
            }
        }
        cls.invalid_arguments = {
            'data': {
                'name': '123',
                'age': 17,
                'preferences': [1, '2', 3, 4]
            },
            'constraints': {
                'name': {Constraint.STRING_REGEX: r'^[A-Z]+$'},
                'age': {Constraint.INT_GE: 18, Constraint.INT_GRATER: 18},
                'preferences': {Constraint.ARRAY_MEMBERS_TYPE: int, Constraint.ARRAY_IS_LENGTH_OF: 3}
            }
        }

    def test_with_valid_arguments(self) -> None:
        self.assertEqual(validate_json_data(**self.valid_arguments), self.valid_arguments['data'])

    def test_with_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            self.assertEqual(
                validate_json_data(**self.invalid_arguments),
                {
                    'name': ['Invalid string expression - does not match regex'],
                    'age': [
                        "Invalid integer expression - isn't grater or equal than compare value",
                        "Invalid integer expression - isn't grater than compare value"],
                    'preferences': [
                        'Invalid array - some or all members have unexpected type',
                        'Invalid array - has different length than expected']
                }
            )


if __name__ == "__main__":
    unittest.main()
