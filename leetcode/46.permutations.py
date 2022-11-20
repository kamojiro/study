#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
# from itertools import permutations
from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        # for p in permutations(range(n)):
        #     ret.append([nums[p[i]] for i in range(n)])
        # return ret
        used = [False]*n
        comp = []
        self.dfs(n, used, nums, comp, ret)
        return ret

    def dfs(self, n: int, used: List[int], nums: List[int], comp: List[int], ret: List[List[int]]):
        if len(comp) == n:
            ret.append(deepcopy(comp))
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            comp.append(nums[i])
            self.dfs(n, used, nums, comp, ret)
            used[i] = False
            comp.pop()
# @lc code=end

