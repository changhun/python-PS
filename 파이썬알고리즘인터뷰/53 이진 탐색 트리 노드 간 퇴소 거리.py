from typing import Optional
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # 인자로 root 는 None 을 받지 않는다.
        def get_max_val(root):
            if root.right:
                return get_max_val(root.right)

            return root.val

        def get_min_val(root):
            if root.left:
                return get_min_val(root.left)
            return root.val

        if not root:
            return

        if root.left:
            left_max_val = get_max_val(root.left)
            self.ans = min(self.ans, root.val - left_max_val)
            self.minDiffInBST(root.left)

        if root.right:
            right_min_val = get_min_val(root.right)
            self.ans = min(self.ans, right_min_val - root.val)
            self.minDiffInBST(root.right)

        return self.ans


root = TreeNode(92, None, None)
cur = TreeNode(12, None, None)
root.left = cur
cur.right = TreeNode(13, None, None)
cur = cur.right
cur.right = TreeNode(52, None, None)
cur = cur.right
cur.left = TreeNode(29, None, None)

ret = Solution().minDiffInBST(root)
print(ret)



