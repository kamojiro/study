from cgi import MiniFieldStorage


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

def check_subtree(tree1, tree2):
    pre_order1 = extend_pre_order(tree1)
    pre_order2 = extend_pre_order(tree2)
    if len(pre_order1) > len(pre_order2):
        pre_order1, pre_order2 = pre_order2, pre_order1
    print(pre_order1, pre_order2)
    l1 = len(pre_order1)
    l2 = len(pre_order2)
    for i in range(l2-l1+1):
        if pre_order1 == pre_order2[i:i+l1]:
            return True
    return False

def extend_pre_order(tree):
    node = tree.root
    ret = []
    def pre_order(node):
        if node:
            ret.append(node.name)
        else:
            ret.append(None)
            return
        pre_order(node.left)
        pre_order(node.right)
    pre_order(node)
    return ret

def test():
    node2 = Node(2)
    node1 = Node(1)
    node3 = Node(3)
    node2.add_left_child(node1)
    node2.add_right_child(node3)
    node6 = Node(6)
    node5 = Node(5)
    node7 = Node(7)
    node6.add_left_child(node5)
    node6.add_right_child(node7)
    node4 = Node(4)
    node4.add_left_child(node2)
    node4.add_right_child(node6)
    tree1 = BinaryTree(node4)
    tree2 = BinaryTree(node2)
    print(check_subtree(tree1, tree2))
    node7 = Node(7)
    node7.add_left_child(node2)
    tree3 = BinaryTree(node7)
    print(check_subtree(tree1, tree3))

if __name__ == "__main__":
    test()






