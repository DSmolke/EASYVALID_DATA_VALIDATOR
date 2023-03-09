## Installation

You can install it directly from PyPi
```bash
  pip install easyvalid-data-validator
```
    
## Tests

All functions are fully tested

You are able to run tests on your own by using this command being in package directory

```bash
  poetry run python -m unittest discover -v
```
or
```bash
  poetry run pytest
```
# easyvalid-data-validator

It's a package developed mainly for validation of json dict that is created by using json.load().

Here is an example of json dict, that has name, age, and balance.
```
user = {
    "name": "ADAM",
    "age": 18,
    "balance": "2000.00"
}
```
We want to validate if:
- name contain only uppercase letters,
- age is greater or equal to 18,
- balance is valid for Decimal conversion


We need to prepare constraint dict which describes this rules as explained:

```
constraints = {
    "key_name1": {<ConstraintEnumObject>: *args},
    "key_name2": {<ConstraintEnumObject>: *args},
    "key_name3": {<ConstraintEnumObject>: *args}
}
```

So we create dict that stores dicts containing Constraint Objects as key that are indicators for validator of which case it's currently working on, and what datachecker it should use.
Value should be arguments that datachecker need:
- Constraint Object - Enum object
- datachecker - function that takes needed arguments and returns True or False if condition is mached
- validator - validator function that raises error when any of value is not valid, or returns data when it's valid
```
form ... import Constraint

constraints = {
    "name": {Constraint.STRING_REGEX: r'^[A-Z]+$},
    "age": {Constraint.INT_GE: 18},
    "balance": {Constraint.STRING_DECIMAL: None}
}
```

Validation is very easy now, we just need to provide validate_json_data() with json_data, and constraints:

```
form ... import validate_json_data

result = validate_json_data(user, constraints)

# result --> {"name": "ADAM", "age": 18, "balance": "2000.00"}
```

If we would change age of user to 17, validator would throw an error:

```
ValidationError("age": ["Invalid integer expression - isn't grater or equal to compare value"])
```

## Documentation link

[Click to read documentation](https://github.com/DSmolke/EASYVALID_DATA_VALIDATOR/edit/master/README.md)
