#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i < n-1 and obstacleGrid[i+1][j] == 0:
                    dp[i+1][j] += dp[i][j]
                if j < m-1 and obstacleGrid[i][j+1] == 0:
                    dp[i][j+1] += dp[i][j]
        return dp[n-1][m-1]
# @lc code=end

