# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ### https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        sentinal = ListNode(0, head)
        slow = fast = sentinal

        for i in range(1, n + 2):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return sentinal.next