# 347. Top K Frequent Elements
# 2回目 綺麗にする. ほぼ変更点なし.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # まずnumsを頭から見ていって、辞書で個数を数えていくことが思いつく
        # その後辞書を(キーではなくアイテム、つまり個数で)ソートして、上k個を取り出す
        # 組み込みソートだと時間計算量がO(nlogn)になるが、今回個数は0からlen(nums)に収まるのでbucket sortが問題なく使える(空間計算量がO(n)に収まる。).
        num_to_count = dict()
        # {数値: 数値の登場回数}
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1

        # i番目の要素である配列には、登場回数iの数字が格納される.
        count_to_nums = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_count.items():
            count_to_nums[count].append(num)

        result = []
        # count_to_numsから登場回数が多い順にk個取り出して結果として返す
        for i in range(len(count_to_nums) - 1, 0, -1):
            result.extend(count_to_nums[i])
            # 今回必ずk個の回答があると保証されている
            if len(result) == k:
                return result
