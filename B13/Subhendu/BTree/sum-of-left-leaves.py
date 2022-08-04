# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ### https://leetcode.com/problems/sum-of-left-leaves/
        s = 0

        def solve(node):
            nonlocal s
            if not node: return

            if node.left and not node.left.left and not node.left.right:
                s += node.left.val
            solve(node.left)
            solve(node.right)

        solve(root)
        return s
