from queue import Queue

from fundamental_tree import Node, Tree


def validate_bst(tree):
    queue = Queue()
    queue.push((tree.root, -1, 1000))
    while not queue.is_empty():
        node, l, r = queue.pop()
        if not ( l < node.name and node.name < r):
            return False
        for child in node.children:
            if child.name == node.name:
                return False
            elif child.name < node.name:
                queue.push((child, l, node.name))
            else:
                queue.push((child, node.name, r))
    return True

def test():
    node4 = Node(4)
    node4.add_child(Node(2))
    node4.add_child(Node(6))
    node10 = Node(10)
    node10.add_child(Node(20))
    node8 = Node(8)
    node8.add_child(node4)
    node8.add_child(node10)
    tree = Tree()
    tree.make_from_node(node8)
    print(validate_bst(tree))
    node4 = Node(4)
    node4.add_child(Node(2))
    node4.add_child(Node(12))
    node10 = Node(10)
    node10.add_child(Node(20))
    node8 = Node(8)
    node8.add_child(node4)
    node8.add_child(node10)
    tree = Tree()
    tree.make_from_node(node8)
    print(validate_bst(tree))

if __name__=='__main__':
    test()

            
