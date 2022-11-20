#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exists = defaultdict(int)
        ret = 0
        l = 0
        for i, x in enumerate(s):
            exists[x] += 1
            while self.more_one(exists):
                exists[s[l]] -= 1
                l += 1
            ret = max(ret, i+1-l)
        return ret
    def more_one(self, exists):
        for x in exists.values():
            if x >= 2:
                return True
        return False
# @lc code=end

