#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time O(n)
        # memory O(n)
        d = defaultdict(int)
        s = 0
        d[0] = 1
        ret = 0
        for x in nums:
            s += x
            ret += d[s-k]
            d[s] += 1
        return ret

# @lc code=end

