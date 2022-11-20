#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        for x in range(1<<n):
            t = x
            comp = []
            for i in range(n):
                if t%2 == 1:
                    comp.append(nums[i])
                t //= 2
            ret.append(comp)
        return ret

# @lc code=end

