import unittest

from queue import Queue

from trees_and_graphs.tree import NodeWithParentsReference


class ExtendedNode(NodeWithParentsReference):
    """ 幅優先探索のためのmarked属性を持つNode
    """
    def __init__(self, data):
        super().__init__(data=data)
        self.parents = []
        self.marked = False

    @property
    def has_parents(self):
        return bool(self.parents)

    def add_parent(self, node):
        self.parents.append(node)


def detect_project_order(projects, dependencies):
    nodes_dict = {project: ExtendedNode(project) for project in projects}

    # 依存関係を処理する
    for d in dependencies:
        successor_node = nodes_dict.get(d[0])  # 後続作業
        predecessor_node = nodes_dict.get(d[1])  # 先行作業

        if not all([successor_node, predecessor_node]):
            raise Exception("依存関係に入力されたプロジェクトが存在しません")

        successor_node.add_parent(predecessor_node)
        predecessor_node.add_child(successor_node)

    root = ExtendedNode(None)

    # 親を持たないnodeをrootのchildrenとする
    for node in nodes_dict.values():
        if node.has_parents:
           continue
        root.add_child(node)

    queue = Queue()
    root.marked = True
    queue.put(root)

    output = []
    while not queue.empty():
        parent = queue.get()
        for child in parent.children:
            if child.marked:
                continue

            output.append(child.data)
            child.marked = True
            queue.put(child)

    return output


class TestDetectProjectOrder(unittest.TestCase):
    def test_it(self):
        target = detect_project_order
        projects = ["a", "b", "c", "d", "e", "f"]
        dependencies = [("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d")]

        actual = target(projects, dependencies)
        expected = ["e", "f", "b", "a", "d", "c"]

        self.assertEqual(expected, actual)
