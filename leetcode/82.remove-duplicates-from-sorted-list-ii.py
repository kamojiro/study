#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        # now_node = head
        # while now_node.next:
        #     if now_node.val != now_node.next.val:
        #         break
        #     v = now_node.val
        #     while now_node.val == v:
        #         head = now_node.next
        #         now_node = head
        #         if head == None:
        #             return head
        list_node = ListNode(0, head)
        head = list_node
        prev_node = head
        while prev_node.next:
            if not prev_node.next.next:
                break
            if prev_node.next.val != prev_node.next.next.val:
                prev_node = prev_node.next
                continue
            v = prev_node.next.val
            while prev_node.next.val == v:
                prev_node.next = prev_node.next.next
                if prev_node.next == None:
                    break
        return head.next
        
        # testcase
        # [1,1], [1,1,2,2], [1,2,2,3,3], [1,1,2,3,3]

# @lc code=end

