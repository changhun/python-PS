from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def list2tree(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])

            mid = (l + r)//2
            root = TreeNode(nums[mid], list2tree(l, mid-1), list2tree(mid+1, r))
            return root
        return list2tree(0, len(nums)-1)