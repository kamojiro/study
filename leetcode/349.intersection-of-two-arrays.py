#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time O(n1+n2)
        # memory O(n1)
        d = dict()
        for x in nums1:
            d[x] = 1
        ret = []
        for x in nums2:
            if x in d and d[x] == 1:
                ret.append(x)
                d[x] = 2
        return ret
# @lc code=end

