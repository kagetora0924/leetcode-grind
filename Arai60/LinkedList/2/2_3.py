"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
一年前Cで解いたような記憶がある.
"""
# 3回目 三回連続ですらすらとacceptされる


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        node = sentinel
        carry = 0

        while l1 or l2:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            digit_sum = l1_val + l2_val + carry
            node.next = ListNode(digit_sum % 10)
            node = node.next
            carry = digit_sum // 10

        if carry == 1:
            node.next = ListNode(1)

        return sentinel.next
