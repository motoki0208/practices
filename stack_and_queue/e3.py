import math, unittest

from stack_and_queue.stack import Stack


class ExtendedStack(Stack):
    """ サイズを保持するスタック
    """
    def __init__(self):
        self.size = 0
        super().__init__()

    def push(self, val):
        super().push(val)
        self.size += 1

    def pop(self):
        val = super().pop()
        self.size -= 1
        return val

    def is_full(self, capacity):
        return self.size == capacity


class SetOfStacks:
    def __init__(self, capacity):
        self.stack_of_stack = ExtendedStack()
        self.list_of_stack = []
        self.capacity = capacity

        first_stack = ExtendedStack()
        self.stack_of_stack.push(first_stack)
        self.list_of_stack.append(first_stack)

    def push(self, val):
        current_stack = self.stack_of_stack.pop()
        if current_stack.is_full(self.capacity):
            # 取り出したstackのサイズが容量いっぱいになっていた場合
            # 取り出したstackを元に戻した上で、新規stackを作成し、それに値を詰める
            self.stack_of_stack.push(current_stack)
            next_stack = ExtendedStack()
            next_stack.push(val)
            self.stack_of_stack.push(next_stack)
            self.list_of_stack.append(next_stack)
        else:
            current_stack.push(val)
            self.stack_of_stack.push(current_stack)

    def pop(self):
        current_stack = self.stack_of_stack.pop()
        return self._pop(current_stack)

    def pop_at(self, index):
        try:
            target_stack = self.list_of_stack[index]
        except IndexError:
            raise Exception

        return self._pop(target_stack)

    def _pop(self, target_stack):
        """ 値を取り出した結果、stackが空となった場合、対象のstackをstackのlistからも削除し、stackのstackにも戻さない
        """
        val = target_stack.pop()

        if target_stack.is_empty:
            self.list_of_stack.remove(target_stack)
        else:
            self.stack_of_stack.push(target_stack)

        return val


class TestSetOfStacks(unittest.TestCase):
    def test_it(self):
        capacity = 3
        target = SetOfStacks(capacity=capacity)

        vals = [1, 2, 3, 4, 5, 6, 7, 8]
        for val in vals:
            target.push(val)

        # 投入する値の数 ÷ 容量 の結果を切り上げした数だけstackが内部に作成されること
        self.assertEqual(target.stack_of_stack.size, math.ceil(len(vals) / capacity))

        for i in range(2):
            target.pop()

        # stackが空になったら削除されること
        self.assertEqual(target.stack_of_stack.size, 2)

        # 1つ目のstackにアクセスして値を取得できること
        self.assertEqual(target.pop_at(0), 3)
