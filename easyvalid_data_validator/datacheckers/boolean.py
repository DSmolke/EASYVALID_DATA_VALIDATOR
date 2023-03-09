from easyvalid_data_validator.common import validate_if_arg_is_of_type


def is_true(value: bool) -> bool:
    value = validate_if_arg_is_of_type(value, bool, "value")
    return value is True


def is_false(value: bool) -> bool:
    value = validate_if_arg_is_of_type(value, bool, "value")
    return value is False
