#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        ret = 0
        cal = "+"
        z = "0"
        s = s.strip()
        if len(s) == 0:
            return 0
        index = 0
        negative = False
        if s[0] == "+":
            index = 1
        elif s[0] == "-":
            index = 1
            negative = True
        digits = [str(i) for i in range(10)]
        for t in s[index:]:
            if t in digits:
                z += t
            else:
                break
        ret = int(z)
        if negative:
            ret = -ret
        if ret <= - (1<<31):
            return - (1<<31)
        elif 1<<31 <= ret:
            return (1<<31)-1
        return ret
        
                
# @lc code=end

