#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]
        l = 0
        r = n-1
        while r - l > 1:
            m = (l+r)//2
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        return min(nums[l], nums[r])
        
# @lc code=end

