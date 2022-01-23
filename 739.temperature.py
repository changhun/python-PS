import collections


class Solution:


    def daily_temperature(self, temp:list) -> list:
        ret = [0] * len(temp)
        stack = []

        for i, cur in enumerate(temp):
            while stack and temp[stack[-1]] < cur:
                top = stack.pop()
                ret[top] = i - top
            stack.append(i)

        return ret

sol = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ret = sol.daily_temperature(temperatures)
print(ret)
