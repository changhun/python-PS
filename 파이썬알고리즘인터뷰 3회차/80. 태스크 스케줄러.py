from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        total = len(tasks)
        ans = 0

        while True:
            cur_tasks = counter.most_common(n+1)
            if len(cur_tasks) == total:
                ans += len(cur_tasks)
                break
            ans += n+1
            for task in cur_tasks:
                counter[task[0]] -= 1
                #counter.subtract(task[0])
            # 개수가 0 이 된 거는 counter 에서 빼줘야 하나?
            counter += collections.Counter()
            total -= len(cur_tasks)
        return ans


tasks = ["A","A","A","B","B","B"]
n = 2
ret = Solution().leastInterval(tasks, n)
print(ret)


