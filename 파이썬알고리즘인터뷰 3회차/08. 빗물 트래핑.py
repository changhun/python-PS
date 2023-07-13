from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        n = len(height)
        for i in range(n):
            while st and height[st[-1]] <= height[i]:
                bottom = height[st.pop()]
                if st:
                    ans += (i - st[-1] - 1) * (min(height[st[-1]], height[i]) - bottom)
            st.append(i)
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4, 2, 0, 3, 2, 5]
ans = Solution().trap(height)
print(ans)