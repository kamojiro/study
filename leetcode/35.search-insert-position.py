#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

from bisect import bisect_left

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ret = bisect_left(nums, target)
        return ret
# @lc code=end

