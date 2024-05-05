# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False

    def hasCycle2(self, head:Optional[ListNode]) -> bool:
        visited_nodes = set()
        temp = head
        while temp:
            if temp in visited_nodes:
                return True
            visited_nodes.add(temp)
            temp = temp.next
        
        return False