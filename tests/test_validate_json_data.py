import unittest
from unittest import TestCase

from easyvalid_data_validator.constraints import Constraint
from easyvalid_data_validator.validator import  validate_json_data


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
