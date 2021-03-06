import unittest

from katas.beta.sort_array_by_last_character import sort_me


class SortMeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sort_me(['acvd', 'bcc']), ['bcc', 'acvd'])

    def test_equals_2(self):
        self.assertEqual(sort_me([
            'asdf', 14, '13', 'asdf']), ['13', 14, 'asdf', 'asdf'])
