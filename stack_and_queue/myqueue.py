from stack_and_queue.node import Node


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, val):
        node = Node(val)
        if self.last:
            self.last.next = node
        self.last = node

        if not self.first:
            self.first = node

    def remove(self):
        if not self.first:
            raise Exception

        val = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return val

    def peek(self):
        if not self.first:
            raise Exception

        return self.first.data

    def is_empty(self):
        return self.first is None
