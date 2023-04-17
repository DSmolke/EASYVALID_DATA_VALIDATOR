from easyvalid_data_validator.common import validate_if_arg_is_of_type, evaluate_numeric_comparison
from easyvalid_data_validator.customexceptions.integer import RangeError


def is_float_in_range(value: float, range_min: float, range_max: float) -> bool:
    """ Checks if value is in provided range"""
    value = validate_if_arg_is_of_type(value, float, "value")
    range_min = validate_if_arg_is_of_type(range_min, float, "range_min")
    range_max = validate_if_arg_is_of_type(range_max, float, "range_max")

    if range_min > range_max:
        raise RangeError('Invalid range')

    return range_min <= value <= range_max

def is_float_lower_than(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, "<")


def is_float_le_than(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, "<=")


def is_float_equal(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, "==")


def is_float_not_equal(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, "!=")


def is_float_grater_than(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, ">")


def is_float_ge_than(value: float, compare_value: float) -> bool:
    return evaluate_numeric_comparison(value, float, compare_value, float, ">=")
