from collections import defaultdict
from itertools import chain
from typing import Any

from easyvalid_data_validator.common import is_type
from easyvalid_data_validator.constraints import Constraint
from easyvalid_data_validator.customexceptions.common import ValidationError
from easyvalid_data_validator.datacheckers.boolean import is_true, is_false
from easyvalid_data_validator.datacheckers.float import is_float_lower_than, is_float_le_than, is_float_equal, \
    is_float_not_equal, is_float_grater_than, is_float_ge_than
from easyvalid_data_validator.datacheckers.string import matches_regex, is_decimal_string
from easyvalid_data_validator.datacheckers.integer import is_in_range, is_lower_than, is_le_than, is_grater_than, \
    is_ge_than, is_equal, is_not_equal
from easyvalid_data_validator.datacheckers.array import is_array_length_of, are_members_of_type
from easyvalid_data_validator.datacheckers.dictionary import are_keys_same_as


def _validate_json_dict_member(key: str, constraint: dict[str, Any], validated_data: dict[str, Any]) -> list[tuple[str]]:
    """
        Validates if value represented by a key match provided constraints
    :param key: validated item key
    :param constraint: rules that value has to match
    :param validated_data: validated json dict
    :return: empty list or list of tuples containing key and error message
    """
    errors = []
    validated_value = validated_data.get(key, False)
    if key not in validated_data.keys():
        raise KeyError('Invalid key')

    for constraint_name, constraint_value in constraint.items():

        match constraint_name:
            case Constraint.STRING_REGEX:
                if not matches_regex(validated_value, constraint_value):
                    errors.append((key, "Invalid string expression - does not match regex"))
            case Constraint.STRING_IS_DECIMAL:
                if not is_decimal_string(validated_value):
                    errors.append((key, "Invalid string expression - isn't decimal string "))

            case Constraint.INT_BETWEEN:
                if not is_in_range(validated_value, *constraint_value):
                    errors.append((key, "Invalid integer expression - isn't in range"))
            case Constraint.INT_LOWER:
                if not is_lower_than(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - isn't lower than compare value"))
            case Constraint.INT_LE:
                if not is_le_than(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - isn't lower or equal than compare value"))
            case Constraint.INT_GRATER:
                if not is_grater_than(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - isn't grater than compare value"))
            case Constraint.INT_GE:
                if not is_ge_than(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - isn't grater or equal than compare value"))
            case Constraint.INT_EQUAL:
                if not is_equal(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - isn't equal to compare value"))
            case Constraint.INT_NOT_EQUAL:
                if not is_not_equal(validated_value, constraint_value):
                    errors.append((key, "Invalid integer expression - validated value and compare value are equal"))

            case Constraint.ARRAY_IS_LENGTH_OF:
                if not is_array_length_of(validated_value, constraint_value):
                    errors.append((key, "Invalid array - has different length than expected"))
            case Constraint.ARRAY_MEMBERS_TYPE:
                if not are_members_of_type(validated_value, constraint_value):
                    errors.append((key, "Invalid array - some or all members have unexpected type"))

            case Constraint.DICT_HAS_SAME_KEYS:
                if not are_keys_same_as(validated_value, constraint_value):
                    errors.append((key, "Invalid dictionary - keys are not the same"))

            case Constraint.FLOAT_LOWER:
                if not is_float_lower_than(validated_value, constraint_value):
                    errors.append((key, "Invalid float - isn't lower than compare value"))
            case Constraint.FLOAT_LE:
                if not is_float_le_than(validated_value, constraint_value):
                    errors.append((key, "Invalid float - isn't lower or equal than compare value"))
            case Constraint.FLOAT_EQUAL:
                if not is_float_equal(validated_value, constraint_value):
                    errors.append((key, "Invalid float - isn't equal to compare value"))
            case Constraint.FLOAT_NOT_EQUAL:
                if not is_float_not_equal(validated_value, constraint_value):
                    errors.append((key, "Invalid float - is equal to compare value"))
            case Constraint.FLOAT_GRATER:
                if not is_float_grater_than(validated_value, constraint_value):
                    errors.append((key, "Invalid float - isn't grater than compare value"))
            case Constraint.FLOAT_GE:
                if not is_float_ge_than(validated_value, constraint_value):
                    errors.append((key, "Invalid float - isn't grater or equal than compare value"))

            case Constraint.IS_TYPE:
                if not is_type(validated_value, constraint_value):
                    errors.append((key, "Invalid type - isn't same type like compare type"))

            case Constraint.BOOL_TRUE:
                if not is_true(validated_value):
                    errors.append((key, "Invalid boolean - isn't True"))

            case Constraint.BOOL_FALSE:
                if not is_false(validated_value):
                    errors.append((key, "Invalid boolean - isn't False"))

            case _:
                raise ValueError('Invalid constraint name')

    return errors


def validate_json_data(data: dict[str, Any], constraints: dict[str, dict[Constraint, Any]]) -> dict[str, list[tuple[str]]]:
    """ Validation of json dict with provided key, constraints dict, data """
    errors = list(
        chain(*[_validate_json_dict_member(key, constraint, data) for key, constraint in constraints.items()]))

    errors_by_key = defaultdict(list)
    for key, error_msg in errors:
        errors_by_key[key].append(error_msg)

    if len(errors_by_key) > 0:
        raise ValidationError(dict(errors_by_key))

    return data
