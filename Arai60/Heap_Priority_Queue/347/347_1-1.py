# 347. Top K Frequent Elements
# 1回目. 9分35秒

"""
以下回答終えて他の方のコードとコメントを見てメモ
・quickselectを知っておく
・heapの実装をしてみるべき

ありそうなコメント
・num_count より num_to_countの方がいいかも?
・同じくcount_bucketよりcount_to_numbersかも?
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # まずnumsを頭から見ていって、辞書で個数を数えていくことが思いつく
        # その後辞書を(キーではなくアイテム、つまり個数で)ソートして、上k個を取り出す
        # 組み込みソートだと時間計算量がO(nlogn)になるが、今回個数は0からlen(nums)に収まるのでbucket sortが問題なく使える(空間計算量がO(n)に収まる。).
        num_count = dict()
        # {数値: 数値の登場回数}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        # i番目の要素である配列には、登場回数iの数字が格納される.
        count_bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in num_count.items():
            count_bucket[count].append(num)

        result = []
        # count_bucketから登場回数が多い順にk個取り出して結果として返す
        for i in range(len(count_bucket) - 1, 0, -1):
            result.extend(count_bucket[i])
            # 今回必ずk個の回答があると保証されている
            if len(result) == k:
                return result

        # 別のアイデアとしては:
        # numsがソートされているなら、一種類の数字を見終わるたびに(個数,数値)をheapに入れていくことができ、
        # heapの大きさを常にk個以下にしておいて、最後にheapの中身を全て答えれば良い。ただソートするので上の解法より遅い。

        # heapqのheapに要素追加などする際の比較はtupleを渡してもできるのかな(自分でheapを作ればもちろん問題ない)
        # -> 先頭要素で比較がおこなわれる. その順序でheapに入れれば良い
