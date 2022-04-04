from collections import deque

def main():
    n = int(input())
    # For simplicity, we assume sizes of box are diffrenet.
    whd = [ tuple(map(int,input().split())) for _ in range(n)]
    edges = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if whd[i][0] <= whd[j][0] and whd[i][1] <= whd[j][1] and whd[i][2] <= whd[j][2]:
                edges[i].append(j)
    edges = topologically_sort(edges)
    dp = [1]*n
    for v in range(n):
        for w in edges[v]:
            dp[w] = max(dp[w], dp[v]+1)
    print(max(dp))

def topologically_sort(edges):
    n = len(edges)
    edge_map = [0]*n
    sink = [0]*n
    for i in range(n):
        for y in edges[i]:
            sink[y] += 1
    queue = deque()
    for i in range(n):
        if sink[i] == 0:
            queue.append(i)
    for i in range(n):
        v = queue.popleft()
        edge_map[v] = i
        for w in edges[v]:
            sink[w] -= 1
            if sink[w] == 0:
                queue.append(w)
    new_edges = [[] for _ in range(n)]
    for v in range(n):
        for w in edges[v]:
            new_edges[edge_map[v]].append(edge_map[w])
    return new_edges

if __name__=="__main__":
    main()