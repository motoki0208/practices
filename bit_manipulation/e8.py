import unittest


def e8(screen, width, x1, x2, y):
    height = int(len(screen) * 8 / width) - 1

    count_for_each_row = int(width / 8)
    target_range_start = count_for_each_row * (height - y)

    start_idx_in_row, start_idx_in_byte = divmod(x1, 8)  # 商: 列の中の何番目の要素を操作すべきか 余り: バイトの何番目から1にすべきか
    end_idx_in_row, end_idx_in_byte = divmod(x2, 8)  # 商: 列の中の何番目の要素を操作すべきか 余り: バイトの何番目まで1にすべきか

    target_start_idx = target_range_start + start_idx_in_row
    target_end_idx = target_range_start + end_idx_in_row

    for i in range(target_start_idx, target_end_idx):
        # 操作対象の開始から、操作対象の終了の1つ前の要素までを全て1で埋める
        screen[i] = screen[i] | 0b11111111

    # 余りの分だけ右にずらす
    screen[target_start_idx] = screen[target_start_idx] >> start_idx_in_byte

    # 余りの分だけ累乗した数から1を引き、(8- 余り)だけ左にずらす(そうすることで余りの数だけ1が頭についた1バイトの数が生成される)
    screen[target_end_idx] = 2 ** end_idx_in_row - 1 << 8 - end_idx_in_byte

    return screen


class TestE7(unittest.TestCase):
    def test_it(self):
        screen_1 = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

        width_1 = 24
        x1_1 = 2
        x2_1 = 18
        y_1 = 2

        actual_1 = e8(screen_1, width_1, x1_1, x2_1, y_1)
        expected_1 = [0b00111111, 0b11111111, 0b11000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]
        self.assertEqual(expected_1, actual_1)
