from typing import Any

from easyvalid_data_validator.common import validate_if_arg_is_of_type
from easyvalid_data_validator.customexceptions.array import InvalidArgumentType


def are_members_of_type(elements: list[Any], desired_type: Any) -> bool:
    """ Function takes list of elements and tries to find out if all their members are of desired type provided as an arg """
    elements = validate_if_arg_is_of_type(elements, list, 'elements')
    """ 
    Although list comprehension might be faster, the for loop gives the ability to return outcome
    of func once it finds out about braking logical condition 
    """
    try:
        for el in elements:
            if not isinstance(el, desired_type):
                return False
    except TypeError:
        raise InvalidArgumentType("Invalid desired_type argument type")
    return True


def is_array_length_of(elements: list[Any], desired_length: int) -> bool:
    """ Checks if elements have desired length, raises exceptions if types of arguments are wrong"""
    elements = validate_if_arg_is_of_type(elements, list, 'elements')
    desired_length = validate_if_arg_is_of_type(desired_length, int, 'desired_length')
    return len(elements) == desired_length
