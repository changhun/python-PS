from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if not root.left or root.left.val != root.val:
                left_depth = 0
            if not root.right or root.right.val != root.val:
                right_depth = 0
            self.longest = max(self.longest, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.longest