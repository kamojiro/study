#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        n = len(nums)
        l = nums.index(0)
        for i in range(l+1, n):
            if nums[i] == 0:
                continue
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        return
# @lc code=end

