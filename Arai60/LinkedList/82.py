# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 18分経過し、分岐が複雑で詰まってしまいsolutionを確認した.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 前問との違いは、重複している数字は1つだけ残すのでなく全部削除するということ。
        # # prev, curr, nextと3つポインタを作ってcurrとnextを比較していく.
        # # 最初に重複があればheadを移動させるので、まずその処理を行う。

        # # ０もしくは1ノードの場合そのまま返す
        # if not head or not head.next:
        #     return head
        
        # while head and head.next:
        #     # headが重複の一部なら、重複を出るまで移動させる
        #     if head.val != head.next.val:
        #         # headが重複を脱しているのでbreak
        #         break
        #     prev_head_val = head.val
        #     while head:
        #         if head.val == prev_head_val:
        #             # headが元の値と異なる値になるまで移動させる.
        #             head = head.next
        #         else: 
        #             break
        #     else:
        #         #
        # else:
        #     # 重複を脱したら

        # # この時点で、headが重複の一部でないことが保証されている
        # prev_node = head
        # curr_node = head
        # while :
        #     next_node = curr_node.next
        #     while next_node and curr_node.val == next_node.val:
        #         next_node = next_node.next
        #     prev_node.next = next_node
        #     prev_node = prev_node.next

        # 18分経過し、分岐が複雑で詰まってしまいsolutionを確認した. fakeノードをheadの前につけることで、
        # headについて特別な処理をしなくてよくなることが多いという手法を思い出した.
        fake = ListNode(val=-1, next=head)
        prev = fake
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                # currの次があって、currと同じ値ということは重複なのでその最後までポインタを進める
                curr = curr.next
            if prev.next == curr:
                # prevとcurrが隣ということは、重複がなかったということなのでprevもcurrも進める
                prev = prev.next
                curr = curr.next
            else:
                # 重複があった場合は、重複部分を削除する.
                prev.next = curr.next
                curr = prev.next
        
        # リストの頭がどう移動していようと、fake.nextがリストの始まりになっている.
        return fake.next
