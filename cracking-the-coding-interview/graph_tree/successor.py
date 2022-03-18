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

def successor(node):
    if node.right or not node.parent:
        ret_node = node.right
        while ret_node.left:
            ret_node = ret_node.left
        return ret_node
    if node == node.parent.left:
        return node.parent
    ret_node = node
    while ret_node == ret_node.parent.right:
        ret_node = ret_node.parent
        if not ret_node.parent:
            return None
    return ret_node.parent

def test():
    node2 = Node(2)
    node2.add_left_child(Node(1))
    node2.add_right_child(Node(3))
    node6 = Node(6)
    node6.add_left_child(Node(5))
    node6.add_right_child(Node(7))
    node4 = Node(4)
    node4.add_left_child(node2)
    node4.add_right_child(node6)
    node = node2.left
    while node:
        node = successor(node)
        if node:
            print(node.name)
        else:
            print(node)

if __name__=='__main__':
    test()
