from typing import Optional

INF = int(1e9)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = INF
    prev = INF
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.ans = min(self.ans, abs(self.prev - root.val))
            self.prev = root.val
            dfs(root.right)
        dfs(root)
        return self.ans


root = TreeNode(1)
Solution().minDiffInBST(root)
