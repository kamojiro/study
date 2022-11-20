#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mod = numRows-1
        two_mod = mod*2
        zigzag = [[] for _ in range(numRows)]
        for i, t in enumerate(s):
            if i%two_mod < mod:
                zigzag[i%mod].append(t)
            else:
                zigzag[mod - i%mod].append(t)
        return "".join(["".join(x) for x in zigzag])

# @lc code=end

