# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ### https://leetcode.com/problems/next-greater-node-in-linked-list/
        curr = head
        stack = []
        idx = 0
        while curr:
            idx += 1
            curr = curr.next

        res = [0] * (idx)

        idx = 0
        curr = head
        while curr:
            while stack and stack[-1][1] < curr.val:
                loc, _ = stack.pop()
                res[loc] = curr.val

            stack.append((idx, curr.val))
            curr = curr.next
            idx += 1
        return res
