from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" ver 1: using max_depth """
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def get_max_depth(root):
            if not root:
                return 0
            left = get_max_depth(root.left)
            right = get_max_depth(root.right)
            #ans[0] = max(ans[0], left + right + 1)
            ans[0] = max(ans[0], left + right)
            return max(left, right) + 1

        get_max_depth(root)
        return ans[0]

