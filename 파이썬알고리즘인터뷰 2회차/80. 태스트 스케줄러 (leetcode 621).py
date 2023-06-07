from typing import List
import collections

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
            sched_task_len = 0
            for task, count in sched_task:
                if count > 0:
                    counts[task] -= 1
                    sched_task_len += 1
        #ans -= n + 1 - len(sched_task)
        ans -= n + 1 - sched_task_len
        return ans


tasks = ["A","A","A","B","B","B"]
n = 0
tasks = ["A","A","A","B","B","B"]
n = 2
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

ret = Solution().leastInterval(tasks, n)
print(ret)
