import copy
import unittest

from queue import Queue

from trees_and_graphs.tree import BinaryTreeNode


def detect_base_list_from(root):
    queue = Queue()
    queue.put(root)

    rets = [[root.data]]
    while not queue.empty():
        new_rets = []
        parent = queue.get()
        additional_lists = []
        if parent.left:
            additional_lists.append(get_left_first_list(parent))
            queue.put(parent.left)
        if parent.right:
            additional_lists.append(get_right_first_list(parent))
            queue.put(parent.right)

        if not additional_lists:
            break

        if not rets:
            rets = additional_lists

        else:
            for ret in rets:
                for additional_list in additional_lists:
                    new_ret = copy.deepcopy(ret)
                    new_ret.extend(additional_list)
                    new_rets.append(new_ret)

            rets = new_rets

    return rets


# def func(rets, root):
#     new_rets = []
#     for ret in rets:
#         new_rets.append(ret.extend(get_right_first_list(root)))
#         new_rets.append(ret.extend(get_left_first_list(root)))
#
#     func(new_rets, root.right)
#     func(new_rets, root.left)
#
#     return new_rets


# def concat_lists(retsoriginal_lists, additional_lists):
#     ret = []
#     for original_list in original_lists:
#         for additional_list in additional_lists:
#             original_list.extend(additional_list)
#             ret.append(original_list)
#
#     return ret


def get_left_first_list(root):
    ret = []
    ret.append(root.left.data)
    ret.append(root.right.data)
    return ret


def get_right_first_list(root):
    ret = []
    ret.append(root.right.data)
    ret.append(root.left.data)
    return ret


class TestDetectBaseListFrom(unittest.TestCase):
    def test_it(self):
        node_a = BinaryTreeNode("a")
        node_b = BinaryTreeNode("b")
        node_c = BinaryTreeNode("c")
        node_d = BinaryTreeNode("d")
        node_e = BinaryTreeNode("e")
        node_f = BinaryTreeNode("f")
        node_g = BinaryTreeNode("g")
        node_h = BinaryTreeNode("h")
        node_i = BinaryTreeNode("i")

        node_a.left = node_b

        node_a.right = node_c

        node_b.left = node_d

        node_b.right = node_e

        node_c.left = node_f

        node_c.right = node_g

        node_d.left = node_h

        node_d.right = node_i

        target = detect_base_list_from
        actual = target(node_a)
        print(len(actual))
        print(actual)
