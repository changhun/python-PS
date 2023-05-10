from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []

        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                top = st.pop()
                if height[top] < h and len(st) > 0:
                    ans += (min(h, height[st[-1]]) - height[top]) * (i - st[-1] - 1)
            st.append(i)
        return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
ret = Solution().trap(height)
print(ret)