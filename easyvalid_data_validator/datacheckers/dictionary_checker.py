from typing import Any

from easyvalid_data_validator.common import validate_if_arg_is_of_type


def are_keys_same_as(data: dict[Any, Any], desired_keys: set) -> bool:
    """ Checks if provided dict object has same keys as desired ones """
    data: dict = validate_if_arg_is_of_type(data, dict, 'data')
    desired_keys: set = validate_if_arg_is_of_type(desired_keys, set, 'desired_keys')
    return set(data.keys()) == desired_keys
