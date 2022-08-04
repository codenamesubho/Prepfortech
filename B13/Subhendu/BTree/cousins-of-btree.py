# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ### https://leetcode.com/problems/cousins-in-binary-tree/
        def solve(node, dep, par, val):
            if not node:
                return

            if node.val == val:
                return dep, par

            return solve(node.left, dep + 1, node, val) or solve(node.right, dep + 1, node, val)

        dx, parx = solve(root, 0, None, x)
        dy, pary = solve(root, 0, None, y)

        return dx == dy and parx != pary