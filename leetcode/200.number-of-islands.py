#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.vertex = [ i for i in range(n)]
    def find(self, x):
        p = self.vertex[x]
        if p == x:
            return x
        a = self.find(p)
        self.vertex[x] = a
        return a
        
    def union(self, x, y):
        bx, by = self.find(x), self.find(y)
        if bx > by:
            bx, by = by, bx
        self.vertex[x] = bx
        self.vertex[by] = bx

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        tree = UnionFind(n*m)
        for i in range(n):
            for j in range(m-1):
                if grid[i][j] == "1" and grid[i][j+1] == "1":
                    tree.union(i*m+j, i*m+(j+1))
        for j in range(m):
            for i in range(n-1):
                if grid[i][j] == "1" and grid[i+1][j] == "1":
                    tree.union(i*m+j, (i+1)*m+j)
        ret = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ret.add(tree.find(i*m+j))
        return len(ret)


# @lc code=end

