#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-1)
        m = 10**5
        M = -1
        descending = True
        before = 10**5
        ret = 0
        for x in prices:
            if descending:
                if before >= x:
                    m = min(m, x)
                else:
                    descending = False
                    M = x
            else:
                if before <= x:
                    M = max(M, x)
                else:
                    ret += M - m
                    descending = True
                    m = x
            before = x
        return ret

# @lc code=end

