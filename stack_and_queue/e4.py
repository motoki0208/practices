import unittest

from stack_and_queue.stack import Stack


class MyQueue:
    def __init__(self):
        self.top = None
        self.main_stack = Stack()
        self.sub_stack = Stack()

    def add(self, val):
        if self.top is None:
            self.top = val
        self.main_stack.push(val)

    def remove(self):
        """ main_stackに入っているものを全てpopして、sub_stackに移したあと、sub_stackからpopする
        """
        while not self.main_stack.is_empty:
            self.sub_stack.push(self.main_stack.pop())

        val = self.sub_stack.pop()
        self.top = self.sub_stack.peek() if not self.sub_stack.is_empty else None

        while not self.sub_stack.is_empty:
            self.main_stack.push(self.sub_stack.pop())

        return val

    def peek(self):
        return self.top

    def is_empty(self):
        return self.main_stack.is_empty


class TestMyQueue(unittest.TestCase):
    def test_it(self):
        target = MyQueue()

        self.assertTrue(target.is_empty())

        for i in [1, 2, 3, 4, 5, 6]:
            target.add(i)

        self.assertFalse(target.is_empty())
        self.assertEqual(target.peek(), 1)

        for i in [1, 2, 3, 4, 5, 6]:
            self.assertEqual(target.remove(), i)
