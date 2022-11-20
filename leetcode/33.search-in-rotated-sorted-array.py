#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while r - l > 1:
            m = (l+r)//2
            if nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
# @lc code=end

