from enum import Enum, auto, unique


@unique
class Constraint(Enum):
    """ Enum stores available names of constraints"""
    # str
    STRING_REGEX = auto()
    STRING_IS_DECIMAL = auto()

    # int
    INT_BETWEEN = auto()
    INT_LOWER = auto()
    INT_LE = auto()
    INT_GRATER = auto()
    INT_GE = auto()
    INT_EQUAL = auto()
    INT_NOT_EQUAL = auto()

    # list
    ARRAY_MEMBERS_TYPE = auto()
    ARRAY_IS_LENGTH_OF = auto()

    # dict
    DICT_HAS_SAME_KEYS = auto()

    # bool
    BOOL_TRUE = auto()
    BOOL_FALSE = auto()

    # float
    FLOAT_LOWER = auto()
    FLOAT_LE = auto()
    FLOAT_EQUAL = auto()
    FLOAT_NOT_EQUAL = auto()
    FLOAT_GRATER = auto()
    FLOAT_GE = auto()

    # general
    IS_TYPE = auto()
