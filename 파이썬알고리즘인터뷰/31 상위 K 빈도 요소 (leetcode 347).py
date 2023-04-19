import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = collections.Counter(nums)
        ans = [key for key, value in counter.most_common(k)]
        return ans


nums = [1,1,1,2,2,3]
k = 2
ret = Solution().topKFrequent(nums, k)
print(ret)