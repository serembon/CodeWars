import unittest

from katas.kyu_5.where_my_anagrams_at import anagrams


class AnagramsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']),
                         ['aabb', 'bbaa'])

    def test_equals_2(self):
        self.assertEqual(anagrams(
            'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']),
            ['carer', 'racer'])

    def test_equals_3(self):
        self.assertEqual(anagrams('laser', ['lazing', 'lazy', 'lacer']), [])
