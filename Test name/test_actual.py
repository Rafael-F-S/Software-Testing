import unittest
from testingone import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # Test for 'testingone.py'.

    def test_first_last_name(self):
        # Do names like 'Bob Dylan' work?
        formatted_name = get_formatted_name("bob", "dylan")
        self.assertEqual(formatted_name, "Bob Dylan")

    def test_first_middle_last_name(self):
        # Do names like 'Bob Dylan' work?
        formatted_name = get_formatted_name("edgar", "poe", "allan")
        self.assertEqual(formatted_name, "Edgar Allan Poe")

    if __name__ == "__main__":
        unittest.main()
