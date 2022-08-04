# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ### https://leetcode.com/problems/symmetric-tree/
        def solve(r1, r2):
            if not r1 and not r2:
                return True
            if r1 and r2:
                a = r1.val == r2.val
                b = solve(r1.left, r2.right)
                c = solve(r1.right, r2.left)
                return a and b and c
            return False

        if not root:
            return root
        return solve(root.left, root.right)
