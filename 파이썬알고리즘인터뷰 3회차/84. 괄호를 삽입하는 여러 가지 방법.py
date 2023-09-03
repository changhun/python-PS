from typing import List
class Solution:
    def calculate(self, operator, val1, val2):
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2

    def diff_ways_to_compute(self, nums, operators):
        if len(nums) == 1:
            return nums
        ans = []
        for i in range(len(operators)):
            ret1 = self.diff_ways_to_compute(nums[:i+1], operators[:i])
            ret2 = self.diff_ways_to_compute(nums[i+1:], operators[i+1:])
            for val1 in ret1:
                for val2 in ret2:
                    ans.append(self.calculate(operators[i], val1, val2))
        return ans

    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        operators = []
        num = ""
        for ch in expression:
            if ch in "+-*":
                nums.append(int(num))
                num = ""
                operators.append(ch)
            else:
                num += ch
        nums.append(int(num))

        ret = self.diff_ways_to_compute(nums, operators)
        return ret


expression = "2*3-4*5"
ret = Solution().diffWaysToCompute(expression)
print(ret)