#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for t in s:
            if t == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif t == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif t == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(t)
        if stack:
            return False
        else:
            return True
# @lc code=end

