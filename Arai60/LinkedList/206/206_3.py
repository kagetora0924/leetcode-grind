# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# cで解いた記憶がある
# 3回目: 3回書き直す. 覚えづらい場所は不自然な処理.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # list is empty or 1 node.
        if not head or not head.next:
            return head

        previous_node = None
        current_node = head

        # reverse current_node.next
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node
