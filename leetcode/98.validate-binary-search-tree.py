#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRange(root, -(1<<32), 1<<32)
    def isValidBSTRange(self, root: Optional[TreeNode], minimum, maximum) -> bool:
        ret = True
        if root.left:
            ret &= minimum < root.left.val < min(root.val, maximum) and self.isValidBSTRange(root.left, minimum, min(root.val, maximum))
        if root.right:
            ret &= max(root.val, minimum) < root.right.val < maximum and self.isValidBSTRange(root.right, max(root.val, minimum), maximum)
        return ret
# @lc code=end

