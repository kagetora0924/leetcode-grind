# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    前問で思い出した循環検出のアルゴリズムが頭にあったが、曖昧な記憶だったのでまずセットを使うことを考えた。
    """
    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        curr = head
        # headがNoneだった場合がどうなるか不安になるが、その場合は返すべきNoneを返すので頭で例外処理をしなくてもいい。が、それを明記した方がわかりやすいようにも思った
        while curr:
            # 循環がなければcurrがいつかNoneになり、あれば必ずcurr in visited_nodesとなるので無限ループにならないことを確認する
            # currを進めていくのは連結リストの頭の情報を失うかもしれないと考えたが、pythonでは参照の値渡しをしているのでその不安がないことを後で確認した
            # →headでなくcurrを進める
            # https://note.com/crefil/n/n7a0d2dec929b
            if curr in visited_nodes:
                # 循環が見つかった場合は明示的にここで返す
                return curr
            visited_nodes.add(curr)
            curr = curr.next
        # 循環が見つかっていないので明示的にNoneを返す
        return None

    """
    https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E3%81%AE%E5%BE%AA%E7%92%B0%E6%A4%9C%E5%87%BA%E6%B3%95
    循環検出のアルゴリズムについて簡単に図を書いて計算を試みたが、slowとfastの差分がサイクルの長さの整数倍、と置くところが思い浮かばなかったので
    フロイドの循環検出法について調べた。
    疑似乱数列生成の例が挙げられていて、擬似乱数のページも読んだ。疑似乱数は生成法と内部状態が既知であれば確定的な計算で与えられ、予測ができるようになっている。
    """
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # headがNoneを別で扱わなくて良いような処理にする
        slow = head
        fast = head
        while fast and fast.next:
            assert(slow)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # ループが正常終了した場合は循環が見つかっていないのでelseでreturn処理をする。見つかった場合はbreakしているので次に進む
        else:
            return None

        curr = head
        while slow != curr:
            curr = curr.next
            slow = slow.next

        return curr