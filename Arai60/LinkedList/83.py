class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 元々ソートされているので、かぶっている要素は連続して登場するのがわかる.
        # まずcurrが指したノードを保存しておき、次のノードnextが同じ値だったら、nextはリストから除外する.
        # その時nextは除外した次のノードを指すように変更すればいい
        # nextは予約されている名前?なので違う名前をつける.
        curr_node = head
        while curr_node and curr_node.next:
            next_node = curr_node.next
            # duplicateが二つでなく三つ以上の場合もあるのでループで処理する.
            # duplicateを処理していたらリストの最後に到達するかもしれないのでその場合も考慮する.
            while next_node and curr_node.val == next_node.val:
                next_node = next_node.next
                curr_node.next = next_node
            
        return head