import unittest

from unittest import TestCase

from easyvalid_data_validator.datacheckers.dictionary import are_keys_same_as


class TestAreKeysSameAs(TestCase):
    """ Cases when arguments provided are of wrong type are covered by auxiliary function """
    def test_when_keys_match(self) -> None:
        self.assertEqual(are_keys_same_as({'A': 1, 'B': 2}, {'A', 'B'}), True)

    def test_when_keys_dont_match(self) -> None:
        self.assertEqual(are_keys_same_as({'A': 1, 'B': 2}, {'A'}), False)

    def test_when_data_or_desired_keys_are_empty(self) -> None:
        """ Cases where one of argument is valid type but empty should not raise exceptions """
        for data, desired_keys in [({}, {'A'}), ({'A': 1}, set())]:
            with self.subTest(data=data, desired_keys=desired_keys):
                self.assertEqual(are_keys_same_as(data, desired_keys), False)

    def test_when_data_and_desired_keys_are_empty(self) -> None:
        """ Sometimes there might be a need of checking if data argument isn't just empty dict"""
        self.assertEqual(are_keys_same_as({}, set()), True)


if __name__ == "__main__":
    unittest.main()
