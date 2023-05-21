from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index_in_inorder = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_index_in_inorder+1], inorder[:root_index_in_inorder])
        root.right = self.buildTree(preorder[root_index_in_inorder+1:], inorder[root_index_in_inorder+1:])
        return root