#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        index = 0
        for x in s:
            exist = False
            for i in range(index, n):
                if x == t[i]:
                    exist = True
                    index = i+1
                    break
            if not exist:
                return False
        return True



# @lc code=end

