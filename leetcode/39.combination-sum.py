#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ret = []
        self.dfs(n, candidates, target, [], ret, 0, 0)
        return ret

    def dfs(self, n: int, candidates: List[int], target: int, comp: List[int], ret: List[List[int]], s: int, index: int):
        if s == target:
            ret.append(deepcopy(comp))
            return
        if index >= n:
            return
        self.dfs(n, candidates, target, comp, ret, s, index+1)
        while s <= target:
            s += candidates[index]
            comp.append(candidates[index])
            self.dfs(n, candidates, target, comp, ret, s, index+1)
        while comp and comp[-1] == candidates[index]:
            s -= candidates[index]
            comp.pop()

            
# @lc code=end

