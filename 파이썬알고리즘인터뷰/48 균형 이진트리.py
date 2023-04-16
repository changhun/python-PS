from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(root) -> (bool, int):
            if not root:
                return True, 0

            left_balanced, left_height = get_height(root.left)
            right_balanced, right_height = get_height(root.right)
            is_balanced = abs(left_height - right_height) <= 1
            if not left_balanced or not right_balanced:
                is_balanced = False

            return is_balanced, max(left_height, right_height) + 1

        is_balanced, height = get_height(root)
        return is_balanced
