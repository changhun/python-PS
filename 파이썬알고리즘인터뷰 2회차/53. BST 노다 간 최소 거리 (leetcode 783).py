import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" sol1 """
"""
class Solution:
    ans = sys.maxsize
    prev = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            ans = min(self.ans, abs(self.prev - root.val))
            prev = root.val
            dfs(root.right)

        dfs(root)
        return self.ans
"""

""" sol2 """
class Solution:
    ans = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            left_min = left_max = root.val
            right_min = right_max = root.val
            if root.left:
                left_min, left_max = dfs(root.left)
                self.ans = min(self.ans, root.val - left_max)
            if root.right:
                right_min, right_max = dfs(root.right)
                self.ans = min(self.ans, right_min - root.val)
            return left_min, right_max

        dfs(root)
        return self.ans

