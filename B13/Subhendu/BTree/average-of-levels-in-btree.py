# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ### https://leetcode.com/problems/average-of-levels-in-binary-tree/
        if not root:
            return []
        ans = []

        q = deque([root])

        while q:
            s = 0
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                s += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(s/size)

        return ans