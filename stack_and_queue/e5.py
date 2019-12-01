import unittest

from stack_and_queue.stack import Stack


def sort_stack(stack):
    another_stack = Stack()
    while not stack.is_empty:
        tmp = stack.pop()
        if another_stack.is_empty:
            another_stack.push(tmp)
        else:
            if tmp < another_stack.peek():
                another_stack.push(tmp)
            else:
                another_tmp = another_stack.pop()
                another_stack.push(tmp)
                another_stack.push(another_tmp)

    return another_stack
