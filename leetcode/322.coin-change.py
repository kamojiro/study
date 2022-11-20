#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**5]*(amount+1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] == 10**5:
                continue
            for x in coins:
                if i+x <= amount:
                    dp[i+x] = min(dp[i+x], dp[i]+1)
        return dp[amount] if dp[amount] < 10**5 else -1

# @lc code=end

