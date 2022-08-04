# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ### https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
        def solve(preorder, inorder):
            if inorder:
                ind = inorder.index(postorder[-1])
                postorder.pop()
                root = TreeNode(val=inorder[ind])
                root.right = solve(postorder, inorder[ind + 1:])
                root.left = solve(postorder, inorder[0:ind])

                return root

        return solve(postorder, inorder)