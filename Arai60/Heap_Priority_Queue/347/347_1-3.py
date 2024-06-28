# 347. Top K Frequent Elements
# 3回目. 三回書き直す.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 各数字を数える
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1

        # 個数が多い順に並び替える
        count_to_nums = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_count.items():
            count_to_nums[count].append(num)

        # k番目までに多い数を答えとして返す
        result = []
        for i in range(len(count_to_nums) - 1, 0, -1):
            result.extend(count_to_nums[i])
            if len(result) == k:
                return result
