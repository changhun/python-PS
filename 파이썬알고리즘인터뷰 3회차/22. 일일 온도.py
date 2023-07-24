class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        st = []

        for i, temperature in enumerate(temperatures):
            while st and temperatures[st[-1]] < temperature:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans

