#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for t in wordDict:
                m = len(t)
                if i+m <= n and s[i:i+m] == t:
                    dp[i+m] = True
        return dp[n]
                    
# @lc code=end

