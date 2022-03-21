
def build_order(n, restriction):
    sink = [0]*n
    edges = [[] for _ in range(n)]
    for a, b in restriction:
        sink[ord(a) - ord("a")] += 1
        edges[ord(b) - ord("a")].append(ord(a) - ord("a"))
    queue = Queue()
    for v, c in enumerate(sink):
        if c == 0:
            queue.push(v)
    ret = []
    while not queue.is_empty():
        v = queue.pop()
        ret.append(v)
        for w in edges[v]:
            sink[w] -= 1
            if sink[w] == 0:
                queue.push(w)
    return [ chr(ord("a")+v) for v in ret]
    
def test():
    restriction = [("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d")]
    print(restriction)
    print(build_order(6, restriction))

if __name__=='__main__':
    test()