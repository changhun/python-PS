from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            left_depth = dfs(root.left)
            if not root.left or root.val != root.left.val:
                left_depth = 0
            right_depth = dfs(root.right)
            if not root.right or root.val != root.right.val:
                right_depth = 0

            self.ans = max(self.ans, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return self.ans

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
left = root.left
left.left = TreeNode(4)
left.right = TreeNode(4)
right = root.right
right.right = TreeNode(5)
ret = Solution().longestUnivaluePath(root)
print(ret)
