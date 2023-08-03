from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_depth(root: Optional[TreeNode]):
            if not root:
                return 0

            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)
            self.ans = max(self.ans, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return self.ans
