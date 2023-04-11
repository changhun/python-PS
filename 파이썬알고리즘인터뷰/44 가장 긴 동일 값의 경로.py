from typing import Optional
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(root, prev_val):
            if not root:
                return 0

            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
            self.longest = max(self.longest, left + right)
            if root.val != prev_val:
                return 0

            return max(left, right) + 1

        dfs(root, sys.maxsize)
        return self.longest
