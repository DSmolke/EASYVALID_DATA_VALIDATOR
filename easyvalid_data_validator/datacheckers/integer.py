from easyvalid_data_validator.common import validate_if_arg_is_of_type, evaluate_numeric_comparison
from easyvalid_data_validator.customexceptions.integer import RangeError


def is_in_range(value: int, range_min: int, range_max: int) -> bool:
    """ Checks if value is in provided range"""
    value = validate_if_arg_is_of_type(value, int, "value")
    range_min = validate_if_arg_is_of_type(range_min, int, "range_min")
    range_max = validate_if_arg_is_of_type(range_max, int, "range_max")

    if range_min > range_max:
        raise RangeError('Invalid range')

    return range_min <= value <= range_max


def is_lower_than(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, "<")


def is_le_than(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, "<=")


def is_equal(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, "==")


def is_not_equal(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, "!=")


def is_grater_than(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, ">")


def is_ge_than(value: int, compare_value: int) -> bool:
    return evaluate_numeric_comparison(value, int, compare_value, int, ">=")
