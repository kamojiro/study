#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)-1
        r = 10**8
        while r - l > 1:
            m = (l+r)//2
            on_conveyor = 0
            passed = 1
            for w in weights:
                if on_conveyor + w > m:
                    on_conveyor = w
                    passed += 1
                else:
                    on_conveyor += w
            if passed <= days:
                r = m
            else:
                l = m
        return r

# @lc code=end

