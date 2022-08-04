# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ### https://leetcode.com/problems/add-two-numbers-ii/
        def reverse_list(node):
            if not node or not node.next:
                return node

            p = reverse_list(node.next)
            node.next.next = node
            node.next = None
            return p

        ptr1 = reverse_list(l1)
        ptr2 = reverse_list(l2)

        carry = 0

        sentinal = ListNode(0)
        ans = sentinal

        while ptr1 or ptr2 or carry:
            num1 = ptr1.val if ptr1 else 0
            num2 = ptr2.val if ptr2 else 0

            val = num1 + num2 + carry

            res = val % 10
            carry = 1 if val > 9 else 0
            ans.next = ListNode(res)
            ans = ans.next
            if ptr1:
                ptr1 = ptr1.next

            if ptr2:
                ptr2 = ptr2.next

        return reverse_list(sentinal.next)
