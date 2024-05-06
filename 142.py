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
        temp = head
        # headがNoneだった場合がどうなるか不安になるが、その場合は返すべきNoneを返すので頭で例外処理をしなくてもいい。が、それを明記した方がわかりやすいようにも思った
        while head:
            # 循環がなければheadがいつかNoneになり、あれば必ずhead in visited_nodesとなるので無限ループにならないことを確認する
            # headを進めていくのは連結リストの頭の情報を失うかもしれないと考えたが、pythonでは参照の値渡しをしているのでその不安がないことを後で確認した
            # https://note.com/crefil/n/n7a0d2dec929b
            if head in visited_nodes:
                break
            visited_nodes.add(head)
            head = head.next
        return head

    """
    https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E3%81%AE%E5%BE%AA%E7%92%B0%E6%A4%9C%E5%87%BA%E6%B3%95
    循環検出のアルゴリズムについて簡単に図を書いて計算を試みたが、slowとfastの差分がサイクルの長さの整数倍、と置くところが思い浮かばなかったので
    フロイドの循環検出法について調べた。
    疑似乱数列生成の例が挙げられていて、擬似乱数のページも読んだ。疑似乱数は生成法と内部状態が既知であれば確定的な計算で与えられ、予測ができるようになっている。
    """
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # slow、fastが出会った後にslowとheadが出会うように進めるということで二つwhileループを使うので、headがNoneの場合は最初に省いておくのがわかりやすいし確実と考えた
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # slowとfastが出会うまでは循環検出するだけの前問と同じ. ループの中で、循環を検出したかどうか検出すると書き方がややこしくなりそうだから、ループの後で行うことにする
        if not fast or not fast.next:
            return None

        while slow != head:
            head = head.next
            slow = slow.next

        return head