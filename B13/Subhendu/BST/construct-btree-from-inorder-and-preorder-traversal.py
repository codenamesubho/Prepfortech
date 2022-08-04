# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ### https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        def solve(preorder, inorder):
            if inorder:
                ind = inorder.index(preorder[0])
                preorder.pop(0)
                root = TreeNode(val=inorder[ind])
                root.left = solve(preorder, inorder[0:ind])
                root.right = solve(preorder, inorder[ind+1:])
                return root
        return solve(preorder, inorder)