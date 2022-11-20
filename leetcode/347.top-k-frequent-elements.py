#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        frequents = [(item, key) for key, item in d.items()]
        frequents.sort(reverse=True)
        return [ x[1] for x in frequents[:k]]
# @lc code=end

