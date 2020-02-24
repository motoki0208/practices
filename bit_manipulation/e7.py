
import unittest
from bit_manipulation.util import xor


def e7(original):
    idx = 0
    diff_dict = {}  # 奇数番目の数と偶数番目の数が異なるかどうかのフラグを保持する辞書
    original_copy = original  # originalはあとでマスク処理にて使うので、別途copyを作成
    while original_copy:
        # 2つずつセットで処理する
        odd = original_copy & 1  # 端の1ビットを取得(奇数番目)
        original_copy = original_copy >> 1
        even = original_copy & 1  # 1ビットずらして端の1ビットを取得(偶数番目)
        diff_dict[idx] = True if odd != even else False  # 奇数番目の数と偶数番目の数が異なればTrueを返す

        original_copy = original_copy >> 1
        idx += 1

    mask = 0
    for is_diff in diff_dict.values():
        mask = mask << 2
        if is_diff:
            mask += 0b11
        else:
            mask += 0b00

    ret = xor(original, mask)

    return ret


class TestE7(unittest.TestCase):
    def test_it(self):
        actual = e7(0b11011000)
        expected = 0b11100100
        self.assertEqual(bin(expected), bin(actual))
