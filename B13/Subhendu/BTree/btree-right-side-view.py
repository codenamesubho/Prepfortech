# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ### https://leetcode.com/problems/binary-tree-right-side-view/
        if not root:
            return
        bfs = deque([root])
        res = []
        while bfs:
            lvl = []
            for i in range(len(bfs)):
                curr = bfs.popleft()
                lvl.append(curr)

                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)

            res.append(lvl)

        return [i[-1].val for i in res]