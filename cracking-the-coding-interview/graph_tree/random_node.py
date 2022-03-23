class Node:
    def __init__(self, name=None, parent=None, left=None, right=None):
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
    def add_left_child(self, node):
        node.parent = self
        self.left = node
    def add_right_child(self, node):
        node.parent = self
        self.right = node

class BinaryTree:
    def __init__(self, node):
        self.root = node
