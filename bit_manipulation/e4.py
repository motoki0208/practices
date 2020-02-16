import unittest
from bit_manipulation.util import count_bit


def e4(num):
    bit_count = count_bit(num)

    bigger = num + 1
    while count_bit(bigger) != bit_count:
        bigger += 1

    smaller = num - 1
    while count_bit(smaller) != bit_count:
        smaller -= 1

    return bigger, smaller


class TestE4(unittest.TestCase):
    def test_it(self):
        actual = e4(0b1100)
        expected = (0b10001, 0b1010)
        self.assertEqual(actual, expected)
