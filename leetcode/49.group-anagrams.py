#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        d = dict()
        for x in strs:
            y = "".join(sorted(list(x)))
            if y in d:
                ret[d[y]].append(x)
            else:
                d[y] = len(ret)
                ret.append([x])
        return ret
# @lc code=end

