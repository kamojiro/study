#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.rec(n,k,0)
    def rec(self, n: int, k: int, initial: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            if k == 1:
                return 0^initial
            else:
                return 1^initial
        half = pow(2, n-2)
        if k <= half:
            return self.rec(n-1, k, 0^initial)
        else:
            return self.rec(n-1, k-half, 1^initial)
# @lc code=end

