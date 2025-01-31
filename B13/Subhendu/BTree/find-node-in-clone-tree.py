# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ### https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
        def helper(n1, n2):
            if not n1:
                return

            if n1 is target:
                return n2

            return helper(n1.left, n2.left) or helper(n1.right, n2.right)

        return helper(original, cloned)
