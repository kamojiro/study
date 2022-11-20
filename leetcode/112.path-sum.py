#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        queue = deque([(root, 0)])
        while queue:
            node, val = queue.popleft()

            if node == None:
                if val == targetSum:
                    return True
                else:
                    continue
            if node.left == None and node.right == None:
                queue.append((None, val+node.val))
            if node.left != None:
                queue.append((node.left, val+node.val))
            if node.right != None:
                queue.append((node.right, val+node.val))
        return False

# @lc code=end

