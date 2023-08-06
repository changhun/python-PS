from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> (bool, int):
            if not root:
                return (True, 0)
            balanced, left_depth = dfs(root.left)
            if not balanced:
                return (False, left_depth)
            balanced, right_depth = dfs(root.right)
            if not balanced:
                return (False, right_depth)
            balanced = abs(right_depth - left_depth) <= 1
            return (balanced, max(right_depth, left_depth) + 1)
        ret, depth = dfs(root)
        return ret