from unittest import TestCase

from easyvalid_data_validator.constraints import Constraint
from easyvalid_data_validator.validator import _validate_json_dict_member


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

    def test_with_empty_string_as_value(self) -> None:
        assert _validate_json_dict_member('A', {Constraint.IS_TYPE: str}, {'A': ""}) == []