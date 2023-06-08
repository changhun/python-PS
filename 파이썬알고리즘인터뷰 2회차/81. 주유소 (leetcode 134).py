from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = 0
        _sum = 0
        diffs = [gas[i] - cost[i] for i in range(len(gas))]
        n = len(gas)
        diffs += diffs
        for r, diff in enumerate(diffs):
            if r - l == n:
                return l

            _sum += diff
            if _sum < 0:
                _sum = 0
                l = r + 1
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
ret = Solution().canCompleteCircuit(gas, cost)
print(ret)