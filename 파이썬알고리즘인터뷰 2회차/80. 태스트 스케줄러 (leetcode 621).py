from typing import List
import collections


""" sol1 """
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        ans = 0
        # counter
        while counts:
            sched_task = counts.most_common(n+1)
            if sched_task[0][1] == 0:
                break

            ans += n + 1
            for task, count in sched_task:

                counts[task] -= 1
                if counts[task] == 0:
                    del counts[task]

        ans -= n + 1 - len(sched_task)
        return ans
"""

""" sol2 """
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        ans = 0
        # counter
        while counts:
            sched_task = counts.most_common(n+1)
            ans += n + 1

            for task, count in sched_task:
                counts[task] -= 1
            counts += collections.Counter()

        ans -= n + 1 - len(sched_task)
        return ans



tasks = ["A","A","A","B","B","B"]
n = 0
tasks = ["A","A","A","B","B","B"]
n = 2
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
tasks = ["A","B","C","D","A","B","V"]
n = 3
ret = Solution().leastInterval(tasks, n)
print(ret)
