#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = 0
        s = 0
        ret = nums[0]
        for x in nums:
            s += x
            ret = max(ret, s-m)
            m = min(m, s)
        return ret
# @lc code=end

