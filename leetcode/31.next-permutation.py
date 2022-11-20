#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        m = 0
        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                m = nums[i]
                index = i+1
                break
        if index == 0:
            nums.sort()
            return
        s = min(map(lambda x: 101 if x <= m else x,nums[index:]))
        sindex = n-1-list(reversed(nums)).index(s)
        # print(index, s, sindex)
        nums[index-1], nums[sindex] = nums[sindex], nums[index-1]
        nums[index:] = sorted(nums[index:])

    
# @lc code=end

