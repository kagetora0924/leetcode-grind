# 703. Kth Largest Element in a Stream
# 2回目
# Heapを使う実装を綺麗に書き直し
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # numsが空配列の場合に不要な場合分けをしていた. Noneでなく空配列が来るならその場合分け不要
        # heapqの実装を読む。
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # 一つずつの追加なのでpopは1回しか起こらない
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
