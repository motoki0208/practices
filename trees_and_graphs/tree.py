class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    @property
    def has_children(self):
        return bool(self.children)

    def add_child(self, node):
        self.children.append(node)


class NodeWithParentsReference(Node):
    """ 複数親への参照も持つNode
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


class NodeWithParentReference(Node):
    """ 1つしか親を持たないNode
    """
    def __init__(self, data):
        super().__init__(data=data)
        self.parent = None
        self.marked = False

    @property
    def has_parent(self):
        return bool(self.parent)

    def add_parent(self, node):
        self.parent = node


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None