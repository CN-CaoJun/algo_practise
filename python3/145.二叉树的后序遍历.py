#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder(root, result)
        return result
    
    def _postorder(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        # Traverse the left subtree
        self._postorder(node.left, result)
        # Traverse the right subtree
        self._postorder(node.right, result)
        # Visit the root node
        result.append(node.val)


# Construct a binary tree
#     1
#      \
#       2
#      /
#     3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output: [3, 2, 1]


# @lc code=end

