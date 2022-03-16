from fundamental_tree import Tree

def check_balanced(tree):
    nodes = [tree.root]
    lacking = 0
    for i in range(100):
        if len(nodes) == 0:
            return True
        s = 1<<i
        if len(nodes) < s:
            lacking += 1
        if lacking >= 2:
            return False
        new_nodes = []
        for node in nodes:
            new_nodes.extend(node.children)
        nodes = new_nodes

def test():
    adjacency_list = [[1,2], [3,4], [5,6], [7,8], [9], [], [], [], [], []]
    tree = Tree()
    tree.make_from_adjacency_list(adjacency_list)
    print(check_balanced(tree))
    adjacency_list = [[1], [2], []]
    tree.make_from_adjacency_list(adjacency_list)
    print(check_balanced(tree))


if __name__=='__main__':
    test()
