from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def do_operate(num1: int, num2: int, op: str) -> int:
            if op == '*':
                return num1 * num2
            elif op == "-":
                return num1 - num2
            elif op == '+':
                return num1 + num2

        def operate(nums: List[int], ops: List[str]):
            if not ops:
                return nums
            ans = []
            for i, op in enumerate(ops):
                ret1 = operate(nums[:i+1], ops[:i])
                ret2 = operate(nums[i+1:], ops[i+1:])
                for val1 in ret1:
                    for val2 in ret2:
                        ans.append(do_operate(val1, val2, op))
            return ans

        def split(expr: str) -> (list[int], list[str]):
            nums = []
            ops = []
            val = 0
            for char in expr:
                if char.isdigit():
                    val = val * 10 + int(char)
                else:
                    nums.append(val)
                    val = 0
                    ops.append(char)
            nums.append(val)

            return nums, ops

        nums, ops = split(expression)
        ans = operate(nums, ops)
        return ans


expr = "2-1-1"
expr = "2*3-4*5"
ret = Solution().diffWaysToCompute(expr)
print(ret)