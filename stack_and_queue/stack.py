from stack_and_queue.node import Node


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        """ スタックの一番上からデータを削除する
        """
        if self.top is None:
            raise Exception
        ret = self.top.data
        self.top = self.top.next
        return ret

    def push(self, val):
        """ スタックの一番上にvalをデータとしてもつNodeを追加する
        """
        node = Node(val)
        node.next = self.top
        self.top = node

    def peek(self):
        """ スタックの一番上のNodeのデータを返す
        """
        if self.top is None:
            raise Exception
        return self.top.data

    @property
    def is_empty(self):
        """ スタックが空かどうかを返す
        """
        return self.top is None
