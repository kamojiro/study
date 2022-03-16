from fundamental_graph import Graph

def route_between_nodes(graph, start, goal):
    return (goal in graph.get_bfs_order(start)) or (start in graph.get_bfs_order(goal))

def test():
    adjacency_list = [[1,4,5], [3,4], [1], [2,4], [], []]
    graph = Graph()
    graph.make_from_adjacency_list(adjacency_list)
    print(route_between_nodes(graph, 0, 2))
    print(route_between_nodes(graph, 5, 2))

if __name__=='__main__':
    test()
