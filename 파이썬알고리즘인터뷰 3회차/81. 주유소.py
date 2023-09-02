from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas += gas
        cost += cost

        s = 0
        cur_gas = 0
        for i in range(len(gas)):
            if i - s == n:
                return s
            if cur_gas + gas[i] < cost[i]:
                if i == n - 1:
                    return -1
                cur_gas = 0
                s = i + 1
            else:
                cur_gas += gas[i] - cost[i]
        return - 1