# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# 再帰的に実装してみる

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 再帰的に解くには, head.nextから始まるリストをreverseし、そのリストの最後の要素の.nextをheadにする
        # 最初のノードと最後のノード両方へのポインタを返す
        # 再帰呼び出しの終了は単一ノードの時。最初も最後もそのノードに対するポインタとして返す。
        if not head:
            return None

        def helper_reverseList(head: ListNode):
            # 単一ノードに到達した
            if not head.next:
                return head, head

            reversed_head, reversed_tail = helper_reverseList(head.next)
            reversed_tail.next = head
            reversed_tail = head
            reversed_tail.next = None
            return reversed_head, reversed_tail

        reversed_head, _ = helper_reverseList(head)
        return reversed_head
