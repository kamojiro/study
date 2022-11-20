#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        duplicate = set()
        duplicate.add((0,0))
        ret = []
        q = [(nums1[0]+nums2[0], 0, 0)]
        while k > 0 and q:
            k -= 1
            _, i, j = heappop(q)
            ret.append([nums1[i], nums2[j]])
            if i+1 < n1 and (i+1, j) not in duplicate:
                heappush(q, (nums1[i+1]+nums2[j], i+1, j))
                duplicate.add((i+1,j))
            if j+1 < n2 and (i, j+1) not in duplicate:
                heappush(q, (nums1[i]+nums2[j+1], i, j+1))
                duplicate.add((i,j+1))
        return ret

# @lc code=end

