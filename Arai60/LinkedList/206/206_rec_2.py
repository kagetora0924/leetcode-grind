# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# 再帰的に実装、綺麗にした

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 再帰的に解くには, head.nextから始まるリストをreverseし、そのリストの最後の要素の.nextをheadにする
        # 最初のノードと最後のノード両方へのポインタを返す
        # 再帰呼び出しの終了は単一ノードの時。最初も最後もそのノードに対するポインタとして返す。
        if not head:
            return None

        def reverse_list_helper(head: ListNode):
            # 単一ノードに到達した
            if not head.next:
                return head, head

            new_head, new_tail = reverse_list_helper(head.next)
            new_tail.next = head
            new_tail = head
            return new_head, new_tail

        new_head, new_tail = reverse_list_helper(head)
        # こうしないと、元々のheadからhead.nextへのポインタが残っていて循環する
        # helper内では行わなくても問題ないし、無駄な処理を減らせる
        new_tail.next = None
        return new_head
