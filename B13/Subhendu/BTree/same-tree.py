# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ### https://leetcode.com/problems/same-tree/
        q = deque([p, q])

        while q:
            p1 = q.popleft()
            p2 = q.popleft()

            if not p1 and not p2:
                continue
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False

            q.append(p1.left)
            q.append(p2.left)
            q.append(p1.right)
            q.append(p2.right)

        return True