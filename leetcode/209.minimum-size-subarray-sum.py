#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        if sum(nums) < target:
            return 0
        ret = len(nums)
        s = 0
        for r, x in enumerate(nums):
            s += x
            while l <= r:
                if s - nums[l] < target:
                    break
                s -= nums[l]
                l += 1
            if s >= target:
                ret = min(ret, r-l+1)
        return ret
# @lc code=end

