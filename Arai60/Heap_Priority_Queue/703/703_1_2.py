# 703. Kth Largest Element in a Stream
# 1回目 Heap用いた解答見た後に見ずに実装
# TODO: heapそのものをどう実装するか確認する. heapqの実装を読む
# https://github.com/python/cpython/blob/3.12/Lib/heapq.py
import heapq


class KthLargest:
    # editorial読んだあとのretry
    # k番目に大きいものを常に与えられるようにしたく、要素を削除することはなく追加のみ.
    # なのでk番目までから外れたものは不要.削除してしまって良い
    # heapは最小か最大をO(1)時間で与えられ、要素の削除・追加をO(logN)で行える
    # min-heapを作成し、大きさがkを超えたらkになるまで最小の要素を取り除いていけば、いつでも今まででk番目に大きな要素をO(1)時間で得られる
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        if not self.nums:
            return
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums = [val]
        else:
            heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
