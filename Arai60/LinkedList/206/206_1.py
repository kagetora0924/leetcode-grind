# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# cで解いた記憶がある
# 1回目: 7:31
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Noneから始めないと余分なNodeがくっついてしまう
        prev_node = None
        current_node = head
        # headがNoneの場合はNoneを返す
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            # prev_nodeはNoneから始めてるが特別扱い不要
            prev_node = current_node
            current_node = next_node
        return prev_node
