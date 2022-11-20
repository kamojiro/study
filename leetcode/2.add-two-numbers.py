#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_up = 0
        l1 = ListNode(0, l1)
        l2 = ListNode(0, l2)
        ret = ListNode(0)
        ret_node = ret
        while l1.next or l2.next:
            s1 = s2 = 0
            if l1.next:
                s1 = l1.next.val
                l1 = l1.next
            if l2.next:
                s2 = l2.next.val
                l2 = l2.next
            addition = ListNode((s1+s2+carry_up)%10)
            carry_up = ((s1+s2+carry_up)//10)
            ret_node.next = addition
            ret_node = ret_node.next
        if carry_up == 1:
            ret_node.next = ListNode(1)
        return ret.next
# @lc code=end

