# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ### https://leetcode.com/problems/partition-list/
        h1 = s1 = ListNode(0)
        h2 = s2 = ListNode(0)

        curr = head
        while curr:
            if curr.val < x:
                h1.next = curr
                h1 = h1.next
            else:
                h2.next = curr
                h2 = h2.next
            curr = curr.next

        h2.next = None

        h1.next = s2.next

        return s1.next
