from decimal import Decimal
from typing import Any, Callable

# from data_validator.data_validator.customexceptions.array import InvalidArgumentType
# from data_validator.data_validator.customexceptions.common import ArgumentNotCallableError, ComparisonOperatorError
from easyvalid_data_validator.customexceptions.array import InvalidArgumentType
from easyvalid_data_validator.customexceptions.common import ArgumentNotCallableError, ComparisonOperatorError


def validate_if_arg_is_of_type(argument: Any, type_: Any, arg_name: str) -> Any:
    """ Auxiliary function that raises TypeError if something is wrong with elements arg or returns it when everything is fine"""
    if not isinstance(argument, type_):
        raise InvalidArgumentType(f"Invalid {arg_name} argument type")
    return argument


def validate_if_arg_is_callable(argument: Callable, arg_name: str) -> Callable:
    """ Auxiliary function that raises TypeError if argument is not a callable object"""
    if not callable(argument):
        raise ArgumentNotCallableError(f"{arg_name} is not callable object")
    return argument


def evaluate_numeric_comparison(value1: int | float | Decimal, value1_type: Any,  value2: int | float | Decimal, value2_type: Any, comparison_operator: str) -> bool:
    """ Function takes 2 values and 2 info about their types as well as comparison operator that will be used for evaluating logical expression"""
    comparison_operator = validate_if_arg_is_of_type(comparison_operator, str, 'comparison_operator')
    value1 = validate_if_arg_is_of_type(value1, value1_type, "value1")
    value2 = validate_if_arg_is_of_type(value2, value2_type, "value2")

    if comparison_operator not in [">", ">=", "<", "<=", "==", "!="]:
        raise ComparisonOperatorError('Invalid comparison operator')
    return eval(f'{value1} {comparison_operator} {value2}')

def is_type(value: Any, desired_type: Any) -> bool:
    """ Function checks if provided value has type of desired_type argument """
    if desired_type not in {int, float, str, list, dict, bool, None}:
        raise TypeError(
            "Invalid desired_type argument, has to be one of json standard type: int, float, str, list, dict, bool, None")

    return isinstance(value, desired_type)

