# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ### https://leetcode.com/problems/binary-tree-level-order-traversal/
        if not root:
            return []
        ans = []

        q = deque([root])

        while q:
            lvl = []

            for i in range(len(q)):
                curr = q.popleft()
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(lvl)

        return ans
