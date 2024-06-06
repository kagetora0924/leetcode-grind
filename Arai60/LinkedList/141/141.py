# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        """
        循環を検出するという問題については、二つのポインタを用意してそれぞれ1つ、2つずつ進ませてあげると
        循環の開始位置を突き止められるアルゴリズムがあったなあ、ということが頭に浮かぶ
        
        循環の開始位置を決めるには、少し計算をしたらわかる他の作業があった記憶があるが、循環があるかどうか
        見つけるだけであればそれを気にしなくていいな、と考える
        """
        # if not head:
        #     return False
        # slow, fastを定義する時点でheadがNoneでないと確かめないといけないことに気づく

        # headがNoneの場合を特別扱いしないためにfastの初期値をheadに変更。そもそもこちらが自然だったと感じる
        slow = head
        fast = head

        # slowを進めるにはslowがNoneではいけない、fastを進めるにはfastがNoneではもちろんいけないが、fast.nextもNoneではいけない
        # この判定文では判定する要素を減らせそうだが、わかりやすさのために3つとも含めておくのが良いと思った
        # headがNoneの場合、fastがまずFalse判定されるのでfast.nextを判定しようとしてエラーにならないのかな？と思った
        while fast and fast.next:
            assert(slow)
            # 無限ループに陥らないか不安になる。循環がなければfastかfast.nextがNoneになるし、循環があれば必ずfastがslowに追いつくから陥らない。
            slow = slow.next
            fast = fast.next.next
            # slowとfastを同じ場所で始めるなら、進めてから判定しないと常にTrueになってしまう
            if slow == fast:
                return True

        return False

    def hasCycle2(self, head:Optional[ListNode]) -> bool:
        """
        特殊なアルゴリズムを使わなくても検出できるはずだ、循環があるということは一度参照したものをまた参照するという意味だから、
        辞書やセットを使えばいいだろうと考える。セットの方が直感的なのでセットを使う。
        """
        visited_nodes = set()
        # tempという名前は実際使われるべきでないと感じつつ、いい名前が思い浮かばなかった。node_pointerなどでしょうか？
        temp = head
        while temp:
            # 無限ループにならないか注意。循環がなければtempがNoneに至り、循環があれば必ずtemp in visited_nodesとなって終了することを確認。
            if temp in visited_nodes:
                return True
            visited_nodes.add(temp)
            temp = temp.next
        
        return False