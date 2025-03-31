#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder(root, result)
        return result
    def _preorder(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        # Visit the root node
        result.append(node.val)
        # Traverse the left subtree
        self._preorder(node.left, result)
        # Traverse the right subtree
        self._preorder(node.right, result)
        

# @lc code=end

