import unittest
from bit_manipulation.util import count_bit


def xor(i, j):
    return ~(i & j) & (i | j)


def e6(i, j):
    diff_bit = xor(i, j)

    diff_bit_count = count_bit(diff_bit)

    return diff_bit_count


class TestE6(unittest.TestCase):
    def test_it(self):
        actual = e6(29, 15)
        expected = 2
        self.assertEqual(actual, expected)
