import re
from typing import Callable

from easyvalid_data_validator.common import validate_if_arg_is_of_type, validate_if_arg_is_callable
from easyvalid_data_validator.customexceptions.string import ExpressionTypeError, RegexTypeError

def matches_regex(expression: str, regex: str) -> bool:
    """
    :param expression: valid string
    :param regex: valid string pattern
    :return: if expression matches pattern
    """
    if not isinstance(expression, str):
        raise ExpressionTypeError(f"Invalid expression type: {type(expression)}")
    if not isinstance(regex, str):
        raise RegexTypeError(f"Invalid regex type: {type(regex)}")
    return re.match(regex, expression)


def is_decimal_string(expression: str, regex_validator=matches_regex) -> bool:
    """ Checks if expression pattern indicates that it would be converted into Decimal object without causing errors"""
    expression: str = validate_if_arg_is_of_type(expression, str, 'expression')
    regex_validator: Callable[[str, str], bool] = validate_if_arg_is_callable(regex_validator, 'regex_validator')

    return bool(regex_validator(expression, r'^-?\d*\.?\d+$'))


