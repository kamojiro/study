#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [set() for _ in range(n+1)]
        dp[0].add("")
        dp[1].add("()")
        for i in range(1, n):
            for p in dp[i]:
                dp[i+1].add("(" + p + ")")
            for k in range(1, i+1):
                for q in dp[k]:
                    for r in dp[i+1-k]:
                        dp[i+1].add(q+r)
        return list(dp[n])

                    
            
# @lc code=end

