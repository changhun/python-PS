from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        root_index_in_inorder = inorder.index(root)
        root_node = TreeNode(root)
        root_node.left = self.buildTree(preorder[1:root_index_in_inorder + 1], inorder[0:root_index_in_inorder])
        root_node.right = self.buildTree(preorder[root_index_in_inorder + 1:], inorder[root_index_in_inorder + 1:])
        return root_node
