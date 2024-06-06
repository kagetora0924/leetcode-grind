# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1, head)
        node = sentinel
        while(node):
            # node.nextが重複の一部だった場合
            if node.next and node.next.next and node.next.val == node.next.next.val:
                # node.nextが重複の最後に到達するまでnode.nextを更新し続ける
                while node.next.next and node.next.val == node.next.next.val:
                    node.next = node.next.next
                # node.nextが今見ている重複から出る. node.nextが次の重複に含まれるかもしれないのでnodeは更新しない
                node.next = node.next.next
            # node.nextが重複の一部ではない場合、nodeを更新する
            else:
                node = node.next
        
        return sentinel.next
