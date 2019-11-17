import unittest

from stack_and_queue.stack import Stack


class MinimumReturnableStack(Stack):
    def __init__(self):
        super().__init__()
        self.minimum = None

    def push(self, val):
        if self.is_empty or val < self.minimum:
            self.minimum = val
        super().push(val)

    def min(self):
        if self.minimum is None:
            raise Exception
        return self.minimum


class TestMinimumReturnableStack(unittest.TestCase):
    def test(self):
        stack = MinimumReturnableStack()
        for i in [2, 3, 4]:
            stack.push(i)

        self.assertEqual(stack.min(), 2)
        stack.push(1)
        self.assertEqual(stack.min(), 1)


if __name__ == "__main__":
    unittest.main()
