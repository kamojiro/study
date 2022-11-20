#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for t in s:
            d[t] += 1
        for i, x in enumerate(s):
            if d[x] == 1:
                return i
        return -1

# @lc code=end

