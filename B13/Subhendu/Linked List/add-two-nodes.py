# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ### https://leetcode.com/problems/add-two-numbers/
        carry = 0
        sentinal = ListNode(0)
        op = sentinal

        while l1 or l2 or carry:
            val = getattr(l1, 'val', 0) + getattr(l2, 'val', 0) + carry
            res = val % 10

            carry = 1 if val > 9 else 0
            new_node = ListNode(res)
            op.next = new_node
            op = op.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return sentinal.next