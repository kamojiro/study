#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MAX = 10**6
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
# @lc code=end

