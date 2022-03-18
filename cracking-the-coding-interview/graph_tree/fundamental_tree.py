from queue import Queue

class Node:
    def __init__(self, name=None):
        self.name = name
        self.children = []
    def add_child(self, node):
        self.children.append(node)
    
class Tree:
    def __init__(self, name=None):
        self.root = Node(name)

    def make_from_node(self, node):
        self.root = node
        
    def make_from_adjacency_list(self, adjacency_list):
        # Assume 0-indexed
        self.root = Node(0)
        n = len(adjacency_list)
        used = [False]*n
        used[0] = True
        queue = Queue()
        queue.push((0, self.root))
        while not queue.is_empty():
            v, node = queue.pop()
            for w in adjacency_list[v]:
                if used[w]:
                    continue
                used[w] = True
                next_node = Node(w)
                node.children.append(next_node)
                queue.push((w, next_node))

    def display_dfs_order_from_root(self):
        def dfs(node):
            print(node.name)
            for next_node in node.children:
                dfs(next_node)
        dfs(self.root)

    def display_bfs_order_from_root(self):
        queue = Queue()
        queue.push(self.root)
        while not queue.is_empty():
            node = queue.pop()
            print(node.name)
            for next_node in node.children:
                queue.push(next_node)

def test():
    adjacency_list = [[1,2], [0,3,4,5], [0,6, 7], [1], [1], [1], [2,8],[2],[6]]
    tree = Tree()
    tree.make_from_adjacency_list(adjacency_list)
    print("bfs order")
    tree.display_bfs_order_from_root()
    print("dfs order")
    tree.display_dfs_order_from_root()

if __name__=='__main__':
    test()
