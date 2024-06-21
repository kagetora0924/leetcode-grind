# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# cで解いた記憶がある
# 2回目: 綺麗にする.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 空もしくは１要素のリストの場合別で処理した方がわかりやすいし、無駄な処理がない
        if not head or not head.next:
            return head

        # prev_nodeはNoneから始めないと余分なNodeがくっついてしまう
        prev_node = None
        current_node = head
        while current_node:
            # current_nodeが進めるように保持しておく
            next_node = current_node.next
            current_node.next = prev_node
            # prev_nodeはNoneから始めてるが特別扱い不要
            prev_node = current_node
            current_node = next_node
        return prev_node
