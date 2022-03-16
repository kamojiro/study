from fundamental_tree import Node, Tree
from queue import Queue

def minimal_tree(sorted_list):
    n = len(sorted_list)
    p = n.bit_length()
    nodes = []
    for i in range(1<<(p-1)):
        nodes.append((i*2, Node(sorted_list[i*2])) if i*2 < n else (i*2, None))
    for i in reversed(range(1,p)):
        new_nodes = []
        print(nodes)
        for j in range(0, 1<<i , 2):
            mean_i = (nodes[j][0] + nodes[j+1][0])//2
            if mean_i < n:
                parent = Node(sorted_list[mean_i])
                if j < n:
                    parent.add_child(nodes[j][1])
                if j+1 < n:
                    parent.add_child(nodes[j+1][1])
            else:
                parent = None
            new_nodes.append((mean_i, parent))
        nodes = new_nodes
    tree = Tree()
    tree.make_from_node(nodes[0][1])
    return tree

def test():
    sorted_list = [1,2,3,4,5,6,7]
    tree = minimal_tree(sorted_list)
    print("bfs order")
    tree.display_bfs_order_from_root()


if __name__=='__main__':
    test()
