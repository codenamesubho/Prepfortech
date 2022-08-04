# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ### https://leetcode.com/problems/palindrome-linked-list/
        if head is None:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node):
            if not node or not node.next:
                return node

            p = reverse(node.next)
            node.next.next = node
            node.next = None
            return p

        rev = reverse(slow)

        l1 = head
        l2 = rev

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True