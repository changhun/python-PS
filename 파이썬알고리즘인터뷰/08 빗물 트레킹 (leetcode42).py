#class Solution:
#    def trap(self, height: List[int]) -> int:

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


def trap_ref(height) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters

        stack.append(i)
    return volume


#height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
height = [1,2,3,2,2,2,1,3]
#ret = trap(height)
ret = trap_ref(height)
print(ret)