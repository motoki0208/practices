import unittest

from trees_and_graphs.tree import NodeWithParentReference


def detect_first_common_ancestor(node, another_node):
    # まずそれぞれの深さを確認する
    node_depth = _detect_depth(node)
    another_node_depth = _detect_depth(another_node)

    deeper_node = node if node_depth > another_node_depth else another_node
    shallower_node = another_node if node_depth > another_node_depth else node

    deeper_node_ancestor = deeper_node
    for _ in range(abs(node_depth - another_node_depth)):
        deeper_node_ancestor = deeper_node.parent

    shallower_node_ancestor = shallower_node

    while deeper_node_ancestor != shallower_node_ancestor:
        deeper_node_ancestor = deeper_node_ancestor.parent
        shallower_node_ancestor = shallower_node_ancestor.parent

    return deeper_node_ancestor


def _detect_depth(node):
    current = node
    depth = 0
    while current.has_parent:
        current = current.parent
        depth += 1

    return depth


class TestDetectFirstCommonAncestor(unittest.TestCase):
    def test_it(self):
        target = detect_first_common_ancestor

        node_a = NodeWithParentReference("a")
        node_b = NodeWithParentReference("b")
        node_c = NodeWithParentReference("c")
        node_d = NodeWithParentReference("d")
        node_e = NodeWithParentReference("e")
        node_f = NodeWithParentReference("f")
        node_g = NodeWithParentReference("g")
        node_h = NodeWithParentReference("h")
        node_i = NodeWithParentReference("i")

        node_a.left = node_b
        node_b.add_parent(node_a)

        node_a.right = node_c
        node_c.add_parent(node_a)

        node_b.left = node_d
        node_d.add_parent(node_b)

        node_b.right = node_e
        node_e.add_parent(node_b)

        node_c.left = node_f
        node_f.add_parent(node_c)

        node_c.right = node_g
        node_g.add_parent(node_c)

        node_d.left = node_h
        node_h.add_parent(node_d)

        node_d.right = node_i
        node_i.add_parent(node_d)

        self.assertEqual(target(node_b, node_c), node_a)
        self.assertEqual(target(node_h, node_g), node_a)
        self.assertEqual(target(node_h, node_e), node_b)
