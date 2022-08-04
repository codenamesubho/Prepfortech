# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ### https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
        if not preorder:
            return

        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] < preorder[0]:
                i += 1
            else:
                break

        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
