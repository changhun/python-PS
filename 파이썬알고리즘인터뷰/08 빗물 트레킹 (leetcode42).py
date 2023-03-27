#class Solution:
#    def trap(self, height: List[int]) -> int:


"""
def trap(height) -> int:
    ret = 0
    stack = [0] * 20001
    top = -1
    n = len(height)
    for i in range(n):
        while top >= 0 and height[stack[top]] < height[i]:
            prev = stack[top]
            top -= 1
            if top >= 0:
                ret += (i - prev) * (min(height[i], height[stack[top]]) - height[prev])
        if top < 0 or height[stack[top]] != height[i]:
            top += 1
            stack[top] = i

    return ret
"""

def trap(height) -> int:
    ret = 0
    stack = [0] * 20001
    top = -1
    n = len(height)
    for i in range(n):
        while top >= 0 and height[stack[top]] <= height[i]:
            prev = stack[top]
            top -= 1
            if top >= 0:
                ret += (i - stack[top] - 1) * (min(height[i], height[stack[top]]) - height[prev])

        top += 1
        stack[top] = i

    return ret


height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
ret = trap(height)
print(ret)