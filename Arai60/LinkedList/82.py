# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 18分経過し、分岐が複雑で詰まってしまいsolutionを確認した.

class Solution:
    # fakeノードをheadの前につけることで例外的処理を省く手法は、Linked Listにノードを追加したり削除したりする関数の実装でも使っていたことを思い出した。
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(-1, head)
        prev = fake
        curr = head
        # リストの最後に到達するときは必ずここの判定を通る.
        while curr:
            while curr.next and curr.val == curr.next.val:
                # currが重複の一部であるなら、その端まで到達させる.
                curr = curr.next

            # この時点で、currがNoneでないと保証されている.

            if prev.next == curr:
                # duplicateがなかったので、今見ているcurrは取り除く必要がないと確定し、prevも進めて良い.
                prev = prev.next
                curr = curr.next
            else:
                # duplicateがあったので、今見ているcurrは取り除かれる必要がある.
                # 新しいcurrについてはduplicateかわからないので、prev自体は進めない.
                prev.next = curr.next
                curr = prev.next
        
        return fake.next
