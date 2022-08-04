# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ### https://leetcode.com/problems/merge-two-sorted-lists/
        sentinal = ListNode()
        p1 = list1
        p2 = list2
        k = sentinal

        while p1 and p2:
            if p1.val < p2.val:
                k.next = p1
                p1 = p1.next
            else:
                k.next = p2
                p2 = p2.next

            k = k.next
            k.next = None

        while p1:
            k.next = p1
            p1 = p1.next
            k = k.next
            k.next = None

        while p2:
            k.next = p2
            p2 = p2.next
            k = k.next
            k.next = None

        return sentinal.next
