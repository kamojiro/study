from fundamental_tree import Tree

def list_of_depths(tree):
    ret = []
    nodes = [tree.root]
    while nodes:
        ret_s = []
        new_nodes = []
        for node in nodes:
            ret_s.append(node.name)
            new_nodes.extend(node.children)
        ret.append(ret_s)
        nodes = new_nodes
    return ret

def test():
    adjacency_list = [[1,2], [3,4], [5,6], [7,8], [9], [], [], [], [], []]
    tree = Tree()
    tree.make_from_adjacency_list(adjacency_list)
    print(list_of_depths(tree))

if __name__=='__main__':
    test()
