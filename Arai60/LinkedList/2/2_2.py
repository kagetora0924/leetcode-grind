"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
一年前Cで解いたような記憶がある.
"""
# 2回目 綺麗にする


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 答えに使うリストを指し示すsentinelと、答えの最上位桁を指し示すnode
        sentinel = ListNode(val=0, next=None)
        node = sentinel

        # 繰り上がりを保持する
        carry = 0
        while l1 or l2:
            # l1, l2がNoneかどうかの分岐をまとめて見やすくした
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
            node.next = ListNode(val=digit_sum % 10, next=None)
            node = node.next
            carry = digit_sum // 10

        # 最上位桁にも繰り上がりがある場合桁数が一つ増える
        if carry == 1:
            node.next = ListNode(val=1, next=None)

        return sentinel.next
