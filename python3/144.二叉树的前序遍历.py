# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# Test cases
if __name__ == "__main__":
    # Test case 1: Simple binary tree
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    solution = Solution()
    print(solution.preorderTraversal(root1))  # Expected output: [1, 2, 3]

    # Test case 2: Empty tree
    root2 = None
    print(solution.preorderTraversal(root2))  # Expected output: []

    # Test case 3: Full binary tree
    root3 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solution.preorderTraversal(root3))  # Expected output: [1, 2, 3]

    # Test case 4: Left-skewed binary tree
    root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(solution.preorderTraversal(root4))  # Expected output: [1, 2, 3]

    # Test case 5: Right-skewed binary tree
    root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(solution.preorderTraversal(root5))  # Expected output: [1, 2, 3]