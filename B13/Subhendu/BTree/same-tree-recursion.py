# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ### https://leetcode.com/problems/same-tree/
        def solve(n1, n2):
            if not n1 and not n2:
                return True

            if n1 and n2:
                return n1.val == n2.val and solve(n1.left, n2.left) and solve(n1.right, n2.right)
            return False

        return solve(p, q)
