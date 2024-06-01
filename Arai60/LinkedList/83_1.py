class Solution:
    # next_nodeを使わずに書く
    # 重複があるかないかを別で処理する
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            # nodeとnode.nextが重複しなくなるまでnode.nextを進める
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head