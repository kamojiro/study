#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10**5]*(n+1)
        for x in nums:
            index = bisect_left(dp, x)
            dp[index] = x
        return bisect_left(dp, 10**5)
# @lc code=end

