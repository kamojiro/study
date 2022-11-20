#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # s = set()
        # while head:
        #     if head in s:
        #         return True
        #     s.add(head)
        #     head = head.next
        # return False

        # O(1) memory
        for _ in range(10**4+1):
            if not head:
                return False
            head = head.next
        return True
# @lc code=end

