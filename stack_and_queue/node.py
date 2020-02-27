class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendToTail(self, data):
        end = Node(data)
        current = self
        while current.next:
            current = current.next
        current.next = end
