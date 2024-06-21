# 703. Kth Largest Element in a Stream
# 1回目 16:03
# Heapを使う実装はわからず解答例を読んでから次のファイルに書き直した

class KthLargest:
    # 素直に毎回降順にソートして、k番目を返せば実現できる
    # 毎回ソートすると毎回O(nlogn)の時間がかかり流石に無駄なので、追加する時は挿入ソート的に行えば少しマシで、そうすれば追加はO(n)
    # Heapを使うとうまく追加できそうだけど、何も見ずに書け無いので一旦素直な実装をやる
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums = [val]
            return val

        # 新たなvalは最大
        if val > self.nums[0]:
            self.nums.insert(0, val)
        # 新たなvalは最小
        elif val < self.nums[-1]:
            self.nums.append(val)
        # 最小、最大ではない
        else:
            # i番以下で、i+1番以上になる位置を探す
            for i in range(len(self.nums) - 1):
                if val <= self.nums[i] and val >= self.nums[i + 1]:
                    self.nums.insert(i + 1, val)
                    break

        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
