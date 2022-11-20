#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, x in enumerate(nums):
            if target - x in map:
                return [map[target - x], i]
            map[x] = i
            
# @lc code=end

