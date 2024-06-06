"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
一年前Cで解いたような記憶がある.
"""
# 1回目
# 解答時間8分19秒。最後の桁の繰り上がりのケースが漏れていて、30秒ほどで修正した.


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
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            digit_sum = l1_val + l2_val + carry
            node.next = ListNode(val=digit_sum % 10, next=None)
            node = node.next
            carry = digit_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # 最上位桁にも繰り上がりがある場合桁数が一つ増える
        if carry == 1:
            node.next = ListNode(val=1, next=None)

        return sentinel.next
