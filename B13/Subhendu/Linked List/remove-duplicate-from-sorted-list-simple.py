# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        curr = head
        sentinal = ListNode(0, head)
        ans = sentinal
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            ans.next = curr
            ans = ans.next
            curr = curr.next

        return sentinal.next
