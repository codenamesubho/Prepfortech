# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ### https://leetcode.com/problems/search-in-a-binary-search-tree/
        def dfs(node):

            if not node:
                return

            if node.val == val:
                return node

            elif node.val < val:
                return dfs(node.right)
            else:
                return dfs(node.left)

        return dfs(root)