import unittest

from katas.kyu_7.nato_phonetic_alphabet import nato


class NATOTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(nato('babble'), 'Bravo Alpha Bravo Bravo Lima Echo')
