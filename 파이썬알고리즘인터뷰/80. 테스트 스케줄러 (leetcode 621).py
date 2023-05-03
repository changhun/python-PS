import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        remain_task_num = len(tasks)
        ans = 0
        counter = collections.Counter(tasks)
        while counter:
            most_common = counter.most_common(n + 1)
            if most_common[0][1] == 1 and remain_task_num <= n:
                ans += len(most_common)
                remain_task_num -= len(most_common)
                break

            for key, value in most_common:
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]

            remain_task_num -= len(most_common)
            ans += (n + 1)
        return ans




tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

tasks = ["A","A","A","B","B","B"]
n = 2
ret = Solution().leastInterval(tasks, n)
print(ret)