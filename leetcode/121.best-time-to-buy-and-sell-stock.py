#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        m = 10**6
        for x in prices:
            ret = max(ret, x-m)
            m = min(m, x)
        return ret
# @lc code=end

