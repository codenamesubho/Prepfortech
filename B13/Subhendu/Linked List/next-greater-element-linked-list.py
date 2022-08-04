# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        ### https://binarysearch.com/problems/Next-Greater-Element-of-a-Linked-List
        stack = []
        head = node
        while node:
            while stack and stack[-1].val < node.val:
                stack[-1].val = node.val
                stack.pop()
            stack.append(node)
            node = node.next

        while stack:
            stack[-1].val = 0
            stack.pop()

        return head