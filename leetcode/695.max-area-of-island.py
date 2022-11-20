#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ret = 0
        for i in range(n):
            for j in range(m):
                ret = max(ret, self.bfs(grid, i ,j, n, m))
        return ret
                
    def bfs(self, grid, i, j, n, m):
        if grid[i][j] == 0:
            return 0
        q = deque([(i,j)])
        ret = 0
        while q:
            i, j = q.popleft()
            if grid[i][j] == 0:
                continue
            grid[i][j] = 0
            ret += 1
            if i > 0 and grid[i-1][j] == 1:
                q.append((i-1,j))
            if i+1 < n and grid[i+1][j] == 1:
                q.append((i+1,j))
            if j > 0 and grid[i][j-1] == 1:
                q.append((i, j-1))
            if j+1 < m and grid[i][j+1] == 1:
                q.append((i, j+1))
        return ret
# @lc code=end
