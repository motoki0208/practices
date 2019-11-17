import unittest

from stack_and_queue.stack import Stack


def e1(iterable, stack_num):
    stacks = [Stack() for _ in range(stack_num)]
    length = len(iterable)

    idx = 0
    for i in range(length):
        if i >= (idx + 1) / stack_num * length:
            idx += 1
        stacks[idx].push(iterable[i])

    return stacks


class TestE1(unittest.TestCase):
    def test(self):
        input_list = [1, 2, 3, 4, 5, 6]
        input_stack_num = 3
        actual = e1(input_list, input_stack_num)
        self.assertEqual(len(actual), input_stack_num), "入力したstack_numの数だけstackが作成されている"
        for stack in actual:
            self.assertFalse(stack.is_empty), "作成されたstackは空ではない"

        expected = []
        for stack in actual:
            while not stack.is_empty:
                expected.append(stack.pop())

        self.assertEqual(sorted(expected), sorted(input_list)), "stackが保持するデータと入力したリストのデータが一致する"