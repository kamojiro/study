#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ret = []
        traversal = [root]
        while traversal:
            temp_traversal = []
            temp_ret = []
            for node in traversal:
                temp_ret.append(node.val)
                if node.left:
                    temp_traversal.append(node.left)
                if node.right:
                    temp_traversal.append(node.right)
            traversal = temp_traversal
            ret.append(temp_ret)
        return ret
# @lc code=end

