# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ### https://leetcode.com/problems/count-good-nodes-in-binary-tree/
        c = 0

        def solve(node, m):
            nonlocal c
            if not node:
                return

            if node.val >= m:
                c += 1
                m = node.val

            solve(node.left, m)
            solve(node.right, m)

        solve(root, float('-inf'))
        return c