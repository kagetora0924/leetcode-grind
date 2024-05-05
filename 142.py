# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        temp = head
        while head:
            if head in visited_nodes:
                break
            visited_nodes.add(head)
            head = head.next
        return head

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        while slow != head:
            head = head.next
            slow = slow.next

        return head