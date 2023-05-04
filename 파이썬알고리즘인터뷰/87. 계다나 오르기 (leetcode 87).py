MAX_SIZE = 45
""" sol1 """
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0] * (MAX_SIZE + 1)
        ans[0] = 1
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]

        return ans[n]
"""

MAX_SIZE = 45
""" sol2 """
class Solution:

    def climbStairs(self, n: int) -> int:
        def do_climb_stairs(remain_count):
            if remain_count == 0:
                return 1
            elif remain_count < 0:
                return 0

            if memo[remain_count] != -1:
                return memo[remain_count]

            memo[remain_count] = do_climb_stairs(remain_count-1) + do_climb_stairs(remain_count - 2)
            return memo[remain_count]

        memo = [-1] * (MAX_SIZE + 1)

        return do_climb_stairs(n)