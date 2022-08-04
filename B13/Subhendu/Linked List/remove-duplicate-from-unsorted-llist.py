# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        ### https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/
        count = defaultdict(int)
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next

        curr = head
        sentinal = ListNode(-1)
        ans = sentinal
        while curr:
            if count[curr.val] > 1:
                curr = curr.next
            else:
                ans.next = curr
                curr = curr.next
                ans = ans.next
                ans.next = None

        return sentinal.next
