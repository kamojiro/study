#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i < n-1:
                    dp[i+1][j] += dp[i][j]
                if j < m-1:
                    dp[i][j+1] += dp[i][j]
        return dp[n-1][m-1]
# @lc code=end

