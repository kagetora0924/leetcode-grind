# 703. Kth Largest Element in a Stream
# 3回目 3回書き直し
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # サイズというのは解き方から見たネーミングで、kというのは問題名から見たネーミングで、もっといい名前がある気がする
        # target_rankとか?長くなってしまう targetとかだろうか?
        self.size = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.size:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
