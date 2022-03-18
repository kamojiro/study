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

def first_common_ancestor(node1, node2):
    if node1 == node2:
        return node1
    node1_ancestors = [node1]
    node2_ancestors = [node2]
    node1_s = node1
    node2_s = node2
    while node1_s.parent:
        node1_s = node1_s.parent
        node1_ancestors.append(node1_s)
    while node2_s.parent:
        node2_s = node2_s.parent
        node2_ancestors.append(node2_s)
    node1_ancestors.reverse()
    node2_ancestors.reverse()
    l = min(len(node1_ancestors), len(node2_ancestors))
    for i in reversed(range(l)):
        if node1_ancestors[i] == node2_ancestors[i]:
            return node1_ancestors[i]
    
    
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
    print(f"{first_common_ancestor(node1, node2).name=}")
    print(f"{first_common_ancestor(node1, node3).name=}")
    print(f"{first_common_ancestor(node1, node5).name=}")
    print(f"{first_common_ancestor(node4, node5).name=}")

if __name__=='__main__':
    test()
