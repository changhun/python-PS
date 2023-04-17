class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans
