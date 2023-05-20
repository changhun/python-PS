from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def dfs(s, e):
            if s > e:
                return None

            m = (s + e)//2
            root = TreeNode(nums[m], dfs(s, m-1), dfs(m+1, e))
            return root

        root = dfs(0, len(nums)-1)
        return root
