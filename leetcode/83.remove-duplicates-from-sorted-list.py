#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        now_head = head
        while now_head.next:
            if now_head.val == now_head.next.val:
                if now_head.next.next:
                    now_head.next = now_head.next.next
                    continue
                else:
                    now_head.next = None
                    break
            now_head = now_head.next
        return head
            
# @lc code=end

