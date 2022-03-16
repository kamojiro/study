from queue import Queue

class Node:
    def __init__(self, name=None):
        self.name = name
        self.children = []
    def add_child(self, node):
        self.children.push(node)
    
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.push(node)

    def make_from_adjacency_list(self, adjacency_list):
        n = len(adjacency_list)
        self.nodes = [ Node(i) for i in range(n)]
        for v in range(n):
            for w in adjacency_list[v]:
                self.nodes[v].children.append(self.nodes[w])

    def get_dfs_order(self, start):
        n = len(self.nodes)
        visited = [False]*n
        visited[start] = True
        order = []
        def dfs(node):
            order.append(node.name)
            for next_node in node.children:
                if visited[next_node.name]:
                    continue
                visited[next_node.name] = True
                dfs(next_node)
        dfs(self.nodes[start])
        return order

    def get_bfs_order(self, start):
        n = len(self.nodes)
        queue = Queue()
        queue.push(self.nodes[start])
        visited = [False]*n
        visited[start] = True
        order = []
        while not queue.is_empty():
            node = queue.pop()
            order.append(node.name)
            for next_node in node.children:
                if visited[next_node.name]:
                    continue
                visited[next_node.name] = True
                queue.push(next_node)
        return order

def test():
    adjacency_list = [[1,4,5], [3,4], [1], [2,4], [], []]
    graph = Graph()
    graph.make_from_adjacency_list(adjacency_list)
    print("bfs order:",graph.get_bfs_order(0))
    print("dfs order:", graph.get_dfs_order(0))

if __name__=='__main__':
    test()

        
        
        
